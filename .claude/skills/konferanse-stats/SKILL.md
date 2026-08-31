---
name: konferanse-stats
description: Use when the user asks for statistics or an overview across their conference notes — talk counts, tag distribution, attended vs interest, video coverage.
---

# konferanse-stats

Regner ut nøkkeltall på tvers av konferansene og presenterer dem kompakt. Brukerens språk: norsk.

## Steps

1. **Samle data.** For hver `<Konferanse>/<År>/`: tell filer i `talks/`, klassifiser attended (har `**Notater fra konferansen:**`) vs interest, tell talks med video-lenke vs «ikke publisert», og hent alle `**Tags:**`-linjer.

2. **Presenter.** Kompakt tabell per konferanse (talks totalt, attended, interest, videodekning) pluss en topp-10 tagliste på tvers (normaliser case, slå sammen åpenbare duplikater som `AI`/`KI`).

3. **Valgfritt.** Hvis brukeren ber om det: skriv resultatet til en fil eller publiser som Artifact-side. Ellers bare vis i terminalen – ingen filer endres.

## Ikke gjør

- Ikke endre notatfiler.
- Ikke commit.
