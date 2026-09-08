"""Felles lesing av notatrepoet for sjekk.py og konferanse-stats.py. Kjøres fra repo-roten."""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATUS_RE = re.compile(r'^(Video ikke publisert ennå – se \[|Individuell video ikke publisert ennå – se \[|Inngår i \[.*individuell video forventet senere)')
COMMENT_RE = re.compile(r'<!--.*?-->', re.S)

def read(path):
    return open(path, encoding='utf-8').read()

def conferences():
    """[(navn, år, mappe)] for hver <Konferanse>/<År>/ med README.md og talks/."""
    out = []
    for readme in sorted(glob.glob(os.path.join(ROOT, '*', '*', 'README.md'))):
        d = os.path.dirname(readme)
        if os.path.isdir(os.path.join(d, 'talks')) and not os.path.basename(os.path.dirname(d)).startswith(('_', '.')):
            out.append((os.path.basename(os.path.dirname(d)), os.path.basename(d), d))
    return out

def readme_lists(conf_dir):
    """{'attended': {fil: har_⏳}, 'wishlist': {fil: har_⏳}} fra konferanse-README-ens to lister."""
    text = COMMENT_RE.sub('', read(os.path.join(conf_dir, 'README.md')))
    res = {'attended': {}, 'wishlist': {}}
    section = None
    for line in text.split('\n'):
        if line.startswith('## '):
            h = line.lower()
            section = 'attended' if 'gikk på' in h else 'wishlist' if 'vil se opptak' in h else None
        elif section:
            for m in re.finditer(r'\]\(talks/([^)#]+\.md)\)', line):
                res[section][m.group(1)] = line.rstrip().endswith('⏳')
    return res

def talk_files(conf_dir):
    return sorted(f for f in os.listdir(os.path.join(conf_dir, 'talks')) if f.endswith('.md'))

def talk_info(path):
    """Nøkkelfakta om én talk-fil."""
    t = read(path); lines = t.split('\n')
    video = [l for l in lines if l.startswith('**📹**')]
    v = video[0][len('**📹**'):].strip() if video else ''
    has_link = bool(re.match(r'\[[^\]]+\]\(https?://', v))
    return {
        'title': lines[0].lstrip('# ').strip() if lines else '',
        'video_lines': len(video), 'video_text': v, 'has_video': has_link,
        'status_ok': bool(STATUS_RE.match(v)) if not has_link else None,
        'tags': re.findall(r'`([^`]+)`', next((l for l in lines if l.startswith('**Tags:**')), '')),
        'tag_lines': sum(1 for l in lines if l.startswith('**Tags:**')),
        'placeholder': '*(Sammendrag fylles inn senere' in t,
        'marker': '*(Sammendrag basert på programomtalen' in t,
        'notes': '**Notater fra konferansen:**' in t,
        'template_left': bool(re.search(r'<(Tittel|HHMM|slug|Konferanse|ÅÅÅÅ|Taler\(e\)|Dag / dato)>', t)),
        'last': next((l for l in reversed(lines) if l.strip()), ''),
        'program_anchor': (re.search(r'\]\(\.\./program\.md#([^)]+)\)', t) or [None, None])[1],
        'text': t,
    }

def md_files():
    """Alle markdown-filer i repoet utenom bygg-/avhengighetsmapper."""
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in ('_site', 'vendor', '.git', '.jekyll-cache', 'node_modules', 'worktrees')]
        out += [os.path.join(dp, f) for f in fns if f.endswith('.md')]
    return sorted(out)
