# Instruksjoner for kodeagenter

Dette repoet er et verktøy for personlige konferansenotater i markdown, publisert med Jekyll på GitHub Pages. Konvensjonene – mappestruktur, filformat, statusvokabular, tag-vokabular og arbeidsflyt – er dokumentert i [README.md](README.md). Les den før du endrer noe.

## Arbeidsflyter (kanoniske instruksjoner)

De kanoniske, testede arbeidsflytene ligger som instruksjonsfiler i `.claude/skills/<navn>/SKILL.md`. De er skrevet for Claude Code (der de kjøres som `/kommando`), men er ren markdown og skal følges av enhver agent: når brukeren ber om noe som matcher en arbeidsflyt, les den relevante `SKILL.md`-filen og følg stegene til punkt og prikke i stedet for å improvisere. Kommandonavnene i README-ens «Skills»-seksjon tilsvarer mappenavnene – f.eks. «registrer et foredrag» → `.claude/skills/nytt-foredrag/SKILL.md`, «nullstill forken» → `.claude/skills/nullstill/SKILL.md`.

## Harde regler

- Aldri commit eller push uten at brukeren ber om det.
- Aldri overskriv brukerens egne notater (`**Notater fra konferansen:**`-blokkene) – de er brukerens stemme.
- Konferanse-README-enes lister er fasit for deltatt/ønskeliste. Hold README, talk-filer og `program.md` i synk begge veier; SKILL.md-filene beskriver hvordan (navigasjonskjeder, ⏳-markører, 📝-lenker, badge-tall).
- Destruktive operasjoner (sletting, nullstilling) krever eksplisitt bekreftelse etter fremvist plan – oppdraget i seg selv er ikke bekreftelse.
- Svar brukeren på norsk.
