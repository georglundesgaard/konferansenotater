---
name: nytt-foredrag
description: Use when the user wants to register a new conference talk — either one they attended or one they want to watch later. Walks them through a short Norwegian interview and produces the per-talk markdown file plus updates the conference README index.
---

# nytt-foredrag

Interviews the user for a single talk, then writes the file and updates the conference README. Everything user-facing in Norwegian.

## When to use

- User types `/nytt-foredrag` (or asks in Norwegian to "registrere et foredrag", "legge til en talk", "notere en sesjon")
- User wants to add a talk during or right after a conference

## Steps

1. **Finn konferansen.**
   - Hvis `pwd` er inne i `<Konferanse>/<År>/`, bruk den. Meld: `Konferanse: <navn> <år>`.
   - Ellers: bruk `AskUserQuestion` med eksisterende `<Konferanse>/<År>/`-mapper som valg, pluss "Ny konferanse". Ved "Ny konferanse": kjør `/ny-konferanse`-skillen (den setter opp mappen, README og programcache), og fortsett deretter her.

2. **Spør om selve foredraget** (én åpen prompt):
   `Beskriv foredraget – noen stikkord holder (tittel, taler, tid, tema … jeg matcher mot programmet).`
   Argumenter gitt direkte til skillen (`/nytt-foredrag <beskrivelse>`) brukes som svar uten å spørre på nytt.

3. **Match mot programmet.** Sjekk først om `<Konferanse>/<År>/program.md` finnes (lokal cache – foretrukket, fungerer offline). Hvis ikke: finn programlenken i konferansens `README.md` (under Kilder, f.eks. `kotlinconf.com/talks/`, `2026.javazone.no/program`) og WebFetch den. Match brukerens beskrivelse mot foredragene – fuzzy på tittel, taler og tema. Bruk match til å fylle inn eksakt tittel, taler(e) og starttid (HHMM).
   - Én klar match: vis den kort (`Fant: <tid> <tittel> — <taler>`) og fortsett.
   - Flere kandidater: `AskUserQuestion` med toppkandidatene.
   - Ingen match (eller programmet er utilgjengelig): fall tilbake til manuell parsing av beskrivelsen – første `\d{4}` er tid, split på ` — ` eller ` - ` for taler, resten er tittel. Ved hull, still én kort oppfølging.

4. **Dag.** Avgjør endags/flerdags fra konferansens `README.md`: dekker datolinjen i ingressen mer enn én dag (f.eks. «2.–3. september»), er den flerdags. Ikke tell filer i `talks/` – katalogen kan være tom. For flerdags: bruk dagen fra program-matchen hvis den er kjent; ellers anta dagens dato hvis den faller innenfor konferansedagene (meld kort hvilken dag som ble antatt, f.eks. `Antar dag 1 (onsdag)`); ellers spør `AskUserQuestion`.

5. **Attended eller interest?** `AskUserQuestion` med to valg: `attended` / `interest`.

6. **Notater.** Spør: `Notater? (bare lim inn, tomt hvis ingen)`. Konverter linjeskift til `- `-liste. Hopp over blokken hvis tomt eller hvis interest.

7. **Tags.** Spør: `Tags? (kommaseparert – eller tomt for å hoppe over)`. Wrap hver i `` ` `` og join med ` · `.

8. **Video-status.** Spør: `Video-lenke? (tomt hvis ikke publisert)`. Hvis tomt, bruk konferansens standard-fallback (finn ved å skumme README, f.eks. `Video ikke publisert ennå – se [smidig.no](https://www.smidig.no/)`).

9. **Slug + filsti.**
   - Slug: lowercase, ikke-alfanumerisk → `-`, kollaps, trim, kutt til 40 tegn.
   - Filnavn: `dayN-HHMM-<slug>.md` for flerdags, `HHMM-<slug>.md` for endags.
   - Sti: `<Konferanse>/<År>/talks/<filnavn>`.

10. **Skriv fil.** Bruk skjelettet fra `_mal/talks/HHMM-slug.md` (kanonisk kilde – les den, ikke gjenskap fra hukommelsen). Fyll inn tittel, metadata-linje, notater (kun attended), tags og 📹-linje. Behold placeholder-linjen `*(Sammendrag fylles inn senere – bruk /berik-foredrag når opptaket er publisert.)*` som sammendrag – den er signalet `/berik-foredrag` ser etter.

11. **Oppdater konferanse-README.** Åpne `<Konferanse>/<År>/README.md`. Under enten `## Foredrag jeg gikk på` eller `## Foredrag jeg vil se opptak av`, i riktig dag-underseksjon, sett inn (sortert på tid):
    `- **[<HHMM> <Tittel>](talks/<filnavn>)** — <Taler(e)>`

12. **Bekreft og loop.** Meld: `Registrert: <filnavn>`. Spør så: `Ett til? (beskriv neste foredrag, eller tomt for å avslutte)`. Ved nytt svar: gå til steg 3 med samme konferanse og dag-kontekst. Ikke commit – la brukeren gjøre det når de er klare.

## Ikke gjør

- Ikke lag et fyldig sammendrag på egen hånd – dette er en råregistrering. Bruk `/berik-foredrag` senere.
- Ikke commit eller push – bare skriv filer.
- Ikke overskriv en fil som allerede eksisterer. Meld heller: `<filnavn> finnes fra før – rediger direkte eller kjør /berik-foredrag`.
