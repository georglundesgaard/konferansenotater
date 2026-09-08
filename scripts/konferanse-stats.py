#!/usr/bin/env python3
"""Nøkkeltall på tvers av konferansene (datagrunnlaget for /konferanse-stats).
Bruk: scripts/konferanse-stats.py [--tags N]   Skriver en markdown-tabell og topp-N tags (standard 10)."""
import os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import repo

def main():
    top = int(sys.argv[sys.argv.index('--tags') + 1]) if '--tags' in sys.argv else 10
    rows = []; tags = Counter(); tot = Counter()
    for name, year, d in repo.conferences():
        lists = repo.readme_lists(d)
        files = repo.talk_files(d)
        infos = {f: repo.talk_info(os.path.join(d, 'talks', f)) for f in files}
        att = sum(1 for f in files if f in lists['attended']); wl = sum(1 for f in files if f in lists['wishlist'])
        vid = sum(1 for i in infos.values() if i['has_video'])
        wait = sum(1 for i in infos.values() if i['placeholder'] or i['marker'])
        for i in infos.values():
            tags.update(t.strip() for t in i['tags'])
        rows.append((f'{name} {year}', len(files), att, wl, vid, wait))
        for k, v in zip(('talks', 'att', 'wl', 'vid', 'wait'), (len(files), att, wl, vid, wait)): tot[k] += v
    print('| Konferanse | Foredrag | Deltatt | Ønskeliste | Med opptak | Venter på beriking |')
    print('|---|---:|---:|---:|---:|---:|')
    for r in rows:
        print(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} ({r[4]*100//max(r[1],1)} %) | {r[5]} |')
    print(f'| **Sum** | {tot["talks"]} | {tot["att"]} | {tot["wl"]} | {tot["vid"]} ({tot["vid"]*100//max(tot["talks"],1)} %) | {tot["wait"]} |')
    print(f'\nTopp {top} tags: ' + ' · '.join(f'`{t}` {n}' for t, n in tags.most_common(top)))

if __name__ == '__main__':
    main()
