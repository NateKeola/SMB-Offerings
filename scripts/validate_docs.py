#!/usr/bin/env python3
"""Dependency-free structural and public-content checks; no network or writes."""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
links = 0
external = set()
files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts)

def require(condition, message):
    if not condition:
        errors.append(message)

# Vendored templates retain their source formatting and future-install links.
# Their exact bytes and scope are checked instead of pretending they are active docs.
vendored = {}
upstream_manifest = ROOT/'software-factory/UPSTREAM.json'
if upstream_manifest.exists():
    upstream = json.loads(upstream_manifest.read_text())
    for entry in upstream['files']:
        relative = entry['path']
        require(relative.startswith('software-factory/upstream/') and '..' not in Path(relative).parts, 'Invalid vendored path')
        require(relative not in vendored, 'Duplicate vendored path')
        vendored[relative] = entry
        target = ROOT/relative
        require(target.is_file() and not target.is_symlink(), relative+': missing or symlinked upstream file')
        if target.is_file():
            data = target.read_bytes()
            actual = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            require(actual == entry['gitBlobSha'], relative+': upstream byte mismatch')
            require(len(data) == entry['bytes'], relative+': upstream size mismatch')
    actual_paths = {str(p.relative_to(ROOT)) for p in (ROOT/'software-factory/upstream').rglob('*') if p.is_file()}
    require(actual_paths == set(vendored), 'Vendored tree differs from reviewed manifest')
    require(len(vendored) == 31, 'Expected 31 portable upstream files')
    require(not any('/reference/' in p or p.endswith('/check-drift.sh') for p in vendored), 'Excluded upstream reference material present')
    require(sum('/doctrine/' in p for p in vendored) == 6, 'Expected six doctrine documents')
    skill_paths = [p for p in vendored if p.endswith('/SKILL.md')]
    require(len(skill_paths) == 7, 'Expected seven dormant skill templates')
    require(sum('/template/claude/commands/' in p for p in vendored) == 3, 'Expected three dormant command templates')
    for relative in skill_paths:
        source = (ROOT/relative).read_text()
        require(source.startswith('---\n') and '\nname:' in source and '\ndescription:' in source, relative+': missing skill frontmatter')

def slug(text):
    text = re.sub(r'[`*]', '', text).lower().strip()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')

patterns = {
    'private document URL': r'https?://(?:docs\.google\.com|drive\.google\.com|chatgpt\.com/(?:c|g|share)|codex\.openai\.com)/',
    'local absolute path': r'/(?:Users|home)/[^\s/]+/',
    'email address': r'(?<![\w/])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    'credential-shaped string': r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)',
    'internal thread identifier': r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b',
}

for path in files:
    rel = path.relative_to(ROOT)
    require(not any(part in {'private', '.local', 'exports', 'node_modules', '__pycache__'} for part in rel.parts), f'{rel}: excluded directory')
    require(path.suffix not in {'.db', '.sqlite', '.sqlite3', '.zip', '.pdf', '.pptx', '.xlsx'}, f'{rel}: unexpected binary/private artifact')
    text = path.read_text(encoding='utf-8')
    is_vendored = str(rel) in vendored
    if not is_vendored:
        require(text.endswith('\n'), f'{rel}: missing final newline')
        require(not any(line.rstrip() != line for line in text.splitlines()), f'{rel}: trailing whitespace')
    if path.parent.name != 'scripts':
        for label, pattern in patterns.items():
            require(not re.search(pattern, text), f'{rel}: possible {label}; review before publishing')
    if path.suffix == '.json':
        try:
            json.loads(text)
        except ValueError as exc:
            errors.append(f'{rel}: invalid JSON: {exc}')
    if path.suffix == '.md' and not is_vendored:
        require(text.startswith('# '), f'{rel}: missing H1')
        require(len(re.findall(r'^```', text, re.M)) % 2 == 0, f'{rel}: unbalanced code fences')
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            links += 1
            parsed = urlsplit(target)
            if parsed.scheme:
                require(parsed.scheme == 'https' and not parsed.username and not parsed.password, f'{rel}: unsafe link {target}')
                external.add(target)
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(dest.is_relative_to(ROOT), f'{rel}: link escapes repository: {target}') if hasattr(dest, 'is_relative_to') else require(str(dest).startswith(str(ROOT)+'/') or dest == ROOT, f'{rel}: link escapes repository')
            require(dest.exists(), f'{rel}: broken local link {target}')
            if dest.exists() and dest.is_file() and parsed.fragment and dest.suffix == '.md':
                headings = {slug(h) for h in re.findall(r'^#+\s+(.+)$', dest.read_text(), re.M)}
                require(unquote(parsed.fragment) in headings, f'{rel}: unresolved anchor {target}')

snapshot = json.loads((ROOT/'research/reference-snapshots.json').read_text())
refs = snapshot['references']
require(len(refs) == 15, 'Expected 15 historical public references')
require(len({x['id'] for x in refs}) == 15, 'Duplicate reference IDs')
require(len({x['source']['url'] for x in refs}) == 15, 'Duplicate source URLs')
require({t: sum(x['source']['type'] == t for x in refs) for t in ('reel','youtube','website')} == {'reel':7,'youtube':5,'website':3}, 'Reference source counts changed')
for ref in refs:
    for metric in ref['popularity'].values():
        if metric['status'] in {'unknown', 'unavailable', 'hidden'}:
            require(metric['value'] is None, ref['id']+': missing metric became a number')

manifest = json.loads((ROOT/'status/provenance.json').read_text())
require(len(manifest['projects']) == 5, 'Expected five source projects')
for project in manifest['projects']:
    require(bool(re.fullmatch(r'[0-9a-f]{40}', project['commit'])), 'Invalid pinned source commit')
    require(bool(re.fullmatch(r'[0-9a-f]{40}', project['tree'])), 'Invalid source tree')
    require(project['draft'] and not project['merged'], 'Historical source status changed without review')

for filename, count in [('research/market-price-observations.csv',17),('offerings/economic-scenarios.csv',24)]:
    with (ROOT/filename).open(newline='') as handle:
        rows = list(csv.DictReader(handle))
    require(len(rows) == count, filename+': unexpected row count')
    require(all(None not in row for row in rows), filename+': inconsistent CSV shape')
seo_ids = re.findall(r'^\| (S\d{2}) \|', (ROOT/'seo/source-register.md').read_text(), re.M)
require(len(seo_ids) == 62 and len(set(seo_ids)) == 62, 'Expected 62 unique SEO source IDs')
market_ids = re.findall(r'^\| ([RPTIS]\d+) \|', (ROOT/'research/market-source-register.md').read_text(), re.M)
require(len(market_ids) == 26 and len(set(market_ids)) == 26, 'Expected 26 unique market source IDs')
require((ROOT/'offerings/prototype-directions.md').read_text().count('**Stable cluster ID:**') == 6, 'Expected six original prototype directions')
require('Email sending is on hold' in (ROOT/'README.md').read_text(), 'README must retain email hold')

if errors:
    print('\n'.join('FAIL: '+error for error in errors))
    sys.exit(1)
print(f'PASS: {len(files)} text files; {links} Markdown links; {len(external)} unique external links recorded.')
print('PASS: local targets, JSON/CSV shapes, source counts, pinned provenance, whitespace and public-content pattern checks.')
if vendored:
    print(f'PASS: {len(vendored)} byte-identical upstream files; six doctrines, seven dormant skills and three dormant commands. No upstream code executed.')
print('External links were recorded, not fetched. Manual public-content and factual review remain necessary.')
