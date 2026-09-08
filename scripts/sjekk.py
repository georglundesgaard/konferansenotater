#!/usr/bin/env python3
"""Konsistens- og stilsjekk for notatrepoet. Erstatter den manuelle kvalitetssjekken i /avslutt-konferanse
og gjennomlesningen etter store endringer, uten at en agent må lese alle filene.

Bruk: scripts/sjekk.py [--stil] [--stil-alle] [--stille]
  (ingen flagg)  strukturell sjekk: README-lister vs talks/, ⏳ vs 📹-status, filformat, lenker, programankere, badges
  --stil         språkregler («Stil» i rot-README) på blogg/*.md: tankestrek, semikolon, fremmedord
  --stil-alle    samme stilsjekk på talk-filer, README-er og index.md også (mange treff i eldre tekst)
Avslutter med kode 1 ved strukturelle funn; stilfunn er rådgivende.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import repo

FREMMEDORD = {'proveniens': 'kilde/kildemarkør', 'kodifiser': 'skrevet ned', 'baseline': 'referansekjøring',
              'abstract': 'programomtale', 'feature': 'funksjon', 'artefakt': 'resultat'}

def rel(p): return os.path.relpath(p, repo.ROOT)

def strukturell():
    funn = []
    total_talks = 0
    confs = repo.conferences()
    for name, year, d in confs:
        lists = repo.readme_lists(d)
        listed = {**lists['attended'], **lists['wishlist']}
        files = repo.talk_files(d)
        total_talks += len(files)
        for f in files:
            if f not in listed: funn.append(f'{name} {year}: talks/{f} er ikke listet i README')
        for f in listed:
            if f not in files: funn.append(f'{name} {year}: README lenker til talks/{f} som ikke finnes')
        program = repo.read(os.path.join(d, 'program.md')) if os.path.exists(os.path.join(d, 'program.md')) else None
        for f in files:
            info = repo.talk_info(os.path.join(d, 'talks', f)); p = f'{name} {year}: talks/{f}'
            if info['video_lines'] != 1: funn.append(f'{p}: {info["video_lines"]} 📹-linjer (skal være 1)')
            if info['tag_lines'] != 1: funn.append(f'{p}: {info["tag_lines"]} Tags-linjer (skal være 1)')
            if info['template_left']: funn.append(f'{p}: mal-plassholder igjen')
            if info['status_ok'] is False: funn.append(f'{p}: 📹-status utenfor vokabularet: «{info["video_text"][:60]}»')
            if f in listed:
                if listed[f] and info['has_video']: funn.append(f'{p}: ⏳ i README, men filen har video-lenke')
                if not listed[f] and not info['has_video']: funn.append(f'{p}: mangler ⏳ i README (status uten opptak)')
            if f in lists['wishlist'] and '](../README.md)' not in info['last']:
                funn.append(f'{p}: ønskeliste-fil slutter ikke med tilbakelenke til README')
            if f in lists['attended'] and not re.search(r'\]\((?:[^)]*\.md)\)', info['last']):
                funn.append(f'{p}: attended-fil mangler navigasjonslinje sist')
            if program is not None and info['program_anchor'] and f'id="{info["program_anchor"]}"' not in program:
                funn.append(f'{p}: programanker #{info["program_anchor"]} finnes ikke i program.md')
    root = repo.read(os.path.join(repo.ROOT, 'README.md'))
    for badge, n in (('konferanser', len(confs)), ('foredrag', total_talks)):
        m = re.search(rf'badge/{badge}-(\d+)-', root)
        if m and int(m.group(1)) != n: funn.append(f'README.md: badge {badge}-{m.group(1)}, faktisk {n}')
    for f in repo.md_files():
        if '/.claude/' in f or '/_mal/' in f: continue  # instruksjoner og maler: lenkene er formateksempler
        text = re.sub(r'`[^`]*`', '', repo.COMMENT_RE.sub('', repo.read(f)))  # kodespenn er formateksempler
        for m in re.finditer(r'\]\(([^)\s]+)\)', text):
            t = m.group(1)
            if t.startswith(('http://', 'https://', 'mailto:', '#')) or '<' in t: continue
            base, _, anchor = t.partition('#')
            target = os.path.normpath(os.path.join(os.path.dirname(f), base))
            if not os.path.exists(target): funn.append(f'{rel(f)}: død lenke {t}')
            elif anchor and base.endswith('program.md') and f'id="{anchor}"' not in repo.read(target):
                funn.append(f'{rel(f)}: anker #{anchor} finnes ikke i {base}')
    return funn, confs, total_talks

def prosa(lines):
    """Bare prosalinjene teller: overskrifter, metadata-/navigasjonslinjer, 📹-/Tags-linjer, brukerens
    notatpunkter, samt lenketekster og «siterte titler» holdes utenfor (linjenumre beholdes)."""
    out = []; i_notes = False; i_code = False
    for l in lines:
        s = l.strip()
        if s.startswith('```'): i_code = not i_code; out.append(''); continue
        if i_code: out.append(''); continue
        if i_notes and s.startswith('- '): out.append(''); continue
        i_notes = s.startswith('**Notater fra konferansen:**')
        if s.startswith(('#', '**📹**', '**Tags:**', '*[', '*(', '|', '<')) or re.match(r'^\*(Dag \d|\d{1,2}\. )', s) or i_notes:
            out.append(''); continue
        l = re.sub(r'`[^`]*`', '``', l)  # kodespenn er formateksempler
        l = re.sub(r'&\w+;|&#\d+;', '', l)  # HTML-entiteter (&amp; o.l.) er ikke semikolon
        l = re.sub(r'«[^»]*»', '«»', l)
        l = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', '[]()', l)
        # Strukturelle tankestreker er greie: listeskille etter fet term eller lenke («**Tittel** — Taler»,
        # «- [Lenke]() – forklaring») og tallområder («2.–3. september», «10–15»).
        if re.match(r'^\s*- \*\*\[\]\(\)\*\*', l): out.append(''); continue  # talk-listelinje (tittel, taler, ⏳) er struktur
        l = re.sub(r'^(\s*(?:\d+\.|-)\s+(?:\*\*[^*]+\*\*|\[\]\(\)).*?)\s[–—]\s', r'\1 ', l)
        l = re.sub(r'(\d\.?)[–—](\d)', r'\1-\2', l)
        l = re.sub(r'^(\s*(?:\d+\.|-)\s+)\*\*[^*]+\*\*', r'\1', l)  # fet tittel først i et listepunkt er en tittel
        out.append(l)
    return out

def stil(alle):
    files = [f for f in repo.md_files() if os.path.basename(os.path.dirname(f)) == 'blogg']
    if alle:
        files = [f for f in repo.md_files() if '/_mal/' not in f and '/.claude/' not in f and '/_notater/' not in f and not f.endswith('program.md')]  # _notater/ er brukerens ordrette notater
    rapport = []
    for f in files:
        text = repo.COMMENT_RE.sub('', repo.read(f))
        lines = prosa(text.split('\n'))
        dash = [i for i, l in enumerate(lines, 1) if '–' in l or '—' in l]
        semi = [i for i, l in enumerate(lines, 1) if ';' in l.replace('TL;DR', '').replace('&lt;', '').replace('&gt;', '')]
        ord_ = {w: [i for i, l in enumerate(lines, 1) if re.search(r'(?<!ikke )' + w, l, re.I)] for w in FREMMEDORD}
        ord_ = {w: v for w, v in ord_.items() if v}
        if dash or semi or ord_:
            parts = []
            if dash: parts.append(f'tankestrek på {len(dash)} linjer' + (f' ({", ".join(map(str, dash[:8]))})' if len(dash) <= 8 else ''))
            if semi: parts.append(f'semikolon på linje {", ".join(map(str, semi))}')
            for w, v in ord_.items(): parts.append(f'«{w}» (bruk {FREMMEDORD[w]}) på linje {", ".join(map(str, v[:6]))}')
            rapport.append(f'{rel(f)}: ' + '; '.join(parts))
    return rapport, len(files)

def main():
    args = sys.argv[1:]
    funn, confs, n = strukturell()
    if '--stille' not in args or funn:
        print(f'Strukturell sjekk: {len(confs)} konferanser, {n} foredrag. ' + ('Alt konsistent.' if not funn else f'{len(funn)} funn:'))
        for x in funn: print('  -', x)
    if '--stil' in args or '--stil-alle' in args:
        rapport, k = stil('--stil-alle' in args)
        print(f'Stilsjekk ({k} filer): ' + ('ingen avvik.' if not rapport else f'{len(rapport)} filer med avvik:'))
        for x in rapport: print('  -', x)
    sys.exit(1 if funn else 0)

if __name__ == '__main__':
    main()
