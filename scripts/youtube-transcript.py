#!/usr/bin/env python3
"""Henter transkripsjonen (undertekstsporet) til en YouTube-video headless, via yt-dlp.

Bruk: scripts/youtube-transcript.py <url-eller-video-id> [-l språk] [-o fil] [--list]

Krever yt-dlp (`brew install yt-dlp`, eller sett YTDLP=<sti til binær>). Direkte
kall mot Innertube-API-et blokkeres nå fra vanlige nett («Precondition check
failed» / «Sign in to confirm you're not a bot»), mens yt-dlp holder tritt.
Skriver «hh:mm:ss tekst» per linje med header (tittel, kanal, spor). Kontroller
alltid tittelen i headeren mot foredraget før transkripsjonen brukes.
Foretrekker manuelle spor foran autogenererte på ønsket språk.
"""
import argparse, json, os, shutil, subprocess, sys, urllib.request

def ytdlp():
    exe = os.environ.get("YTDLP") or shutil.which("yt-dlp")
    if not exe:
        sys.exit("yt-dlp mangler. Installer med `brew install yt-dlp` (eller sett YTDLP=<sti>).")
    return exe

def info(url):
    r = subprocess.run([ytdlp(), "-J", "--skip-download", "--no-warnings", url], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"yt-dlp feilet: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else r.returncode}")
    return json.loads(r.stdout)

def tracks(d):
    out = []
    for kind, key in (("manuelt", "subtitles"), ("autogenerert", "automatic_captions")):
        for code, fmts in (d.get(key) or {}).items():
            j3 = [f for f in fmts if f.get("ext") == "json3"]
            if j3:
                out.append((code, kind, j3[0]["url"]))
    return out

def pick(tr, lang):
    base = lang.split("-")[0]
    def key(t):
        code, kind, _ = t
        return (0 if code == lang else 1 if code.split("-")[0] == base else 2, 0 if kind == "manuelt" else 1)
    return sorted(tr, key=key)[0]

def hms(ms):
    s = ms // 1000
    return f"{s//3600:02d}:{s%3600//60:02d}:{s%60:02d}"

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("-l", "--lang", default="en"); ap.add_argument("-o", "--out")
    ap.add_argument("--list", action="store_true", help="bare list tilgjengelige spor")
    a = ap.parse_args()
    url = a.video if a.video.startswith("http") else f"https://www.youtube.com/watch?v={a.video}"
    d = info(url)
    tr = tracks(d)
    if a.list:
        for code, kind, _ in tr:
            print(f"{code}\t{kind}")
        return
    if not tr:
        sys.exit(f"Ingen undertekstspor for «{d.get('title')}».")
    code, kind, u = pick(tr, a.lang)
    data = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60))
    lines = [f"# {d.get('title', '?')}", f"# Kanal: {d.get('uploader', '?')} · Video: {d.get('webpage_url', url)}",
             f"# Spor: {code} ({kind})", ""]
    n = 0
    for ev in data.get("events", []):
        text = "".join(seg.get("utf8", "") for seg in ev.get("segs", [])).replace("\n", " ").strip()
        if text:
            lines.append(f"{hms(ev.get('tStartMs', 0))} {text}"); n += 1
    if n == 0:
        sys.exit("Sporet var tomt.")
    out = "\n".join(lines) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(out)
        print(f"{n} linjer → {a.out}\n{lines[0]}\n{lines[2]}")
    else:
        sys.stdout.write(out)

if __name__ == "__main__":
    main()
