# Instruksjoner for kodeagenter

Dette repoet er et verktøy for personlige konferansenotater i markdown, publisert med Jekyll på GitHub Pages. Konvensjonene (mappestruktur, filformat, statusvokabular, tag-vokabular og arbeidsflyt) er dokumentert i [README.md](README.md). Les den før du endrer noe.

## Arbeidsflyter (kanoniske instruksjoner)

De kanoniske, testede arbeidsflytene ligger som instruksjonsfiler i `.claude/skills/<navn>/SKILL.md`. De er skrevet for Claude Code (der de kjøres som `/kommando`), men er ren markdown og skal følges av enhver agent: når brukeren ber om noe som matcher en arbeidsflyt, les den relevante `SKILL.md`-filen og følg stegene til punkt og prikke i stedet for å improvisere. Kommandonavnene i README-ens «Skills»-seksjon tilsvarer mappenavnene, f.eks. «registrer et foredrag» → `.claude/skills/nytt-foredrag/SKILL.md`, «nullstill forken» → `.claude/skills/nullstill/SKILL.md`.

## Skript

Rutineoppgaver ligger som skript i `scripts/` (se «Skript» i README). Bruk dem framfor å skrive egne kommandoer: `scripts/sjekk.py` for konsistenssjekk, `scripts/konferanse-stats.py` for nøkkeltall, `scripts/vimeo-videos.sh` for nye opptak på Vimeo, `scripts/youtube-transcript.py` for YouTube-transkripsjoner og `scripts/vimeo-transcript.js` med tilhørende shell-skript for Vimeo-transkripsjoner via nettleseren.

## Harde regler

- Aldri commit eller push uten at brukeren ber om det.
- Aldri overskriv brukerens egne notater (`**Notater fra konferansen:**`-blokkene). De er brukerens stemme.
- Konferanse-README-enes lister er fasit for deltatt/ønskeliste. Hold README, talk-filer og `program.md` i synk begge veier. SKILL.md-filene beskriver hvordan (navigasjonskjeder, ⏳-markører, 📝-lenker, badge-tall).
- Destruktive operasjoner (sletting, nullstilling) krever eksplisitt bekreftelse etter fremvist plan. Oppdraget i seg selv er ikke bekreftelse.
- Svar brukeren på norsk, og følg «Stil» i README for all prosa du skriver inn i repoet.
