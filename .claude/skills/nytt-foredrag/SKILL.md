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
   - Ellers: bruk `AskUserQuestion` med eksisterende `<Konferanse>/<År>/`-mapper som valg, pluss "Ny konferanse". Ved "Ny konferanse", spør om navn og år og opprett fra `_mal/` (kopier README.md og en tom `talks/`).

2. **Spør om selve foredraget** (én åpen prompt):
   `Fortell meg om foredraget – tid (HHMM), tittel, og taler(e). Kan skrives fritt, jeg tolker.`
   Parse: første `\d{4}` er tid, split på ` — ` eller ` - ` for taler, resten er tittel. Ved usikkerhet, still én kort oppfølging.

3. **Hvis konferansen er flerdags** (finn ut ved å telle `day1-`/`day2-` filer under `talks/` eller sjekke README), spør `AskUserQuestion`: hvilken dag (Dag 1 / Dag 2 / ...).

4. **Attended eller interest?** `AskUserQuestion` med to valg: `attended` / `interest`.

5. **Notater.** Spør: `Notater? (bare lim inn, tomt hvis ingen)`. Konverter linjeskift til `- `-liste. Hopp over blokken hvis tomt eller hvis interest.

6. **Tags.** Spør: `Tags? (kommaseparert – eller tomt for å hoppe over)`. Wrap hver i `` ` `` og join med ` · `.

7. **Video-status.** Spør: `Video-lenke? (tomt hvis ikke publisert)`. Hvis tomt, bruk konferansens standard-fallback (finn ved å skumme README, f.eks. `Video ikke publisert ennå – se [smidig.no](https://www.smidig.no/)`).

8. **Slug + filsti.**
   - Slug: lowercase, ikke-alfanumerisk → `-`, kollaps, trim, kutt til 40 tegn.
   - Filnavn: `dayN-HHMM-<slug>.md` for flerdags, `HHMM-<slug>.md` for endags.
   - Sti: `<Konferanse>/<År>/talks/<filnavn>`.

9. **Skriv fil** etter dette skjelettet:

```markdown
# <Tittel>

*[← <Konferanse> <År>](../README.md) · <Dag / dato> · kl <HH:MM> · <Taler(e)>*

*(Sammendrag fylles inn senere – bruk `/berik-foredrag` når opptaket er publisert.)*

**Notater fra konferansen:**       (kun hvis attended og notater finnes)
- ...

**Tags:** ...

**📹** <video-linje>
```

10. **Oppdater konferanse-README.** Åpne `<Konferanse>/<År>/README.md`. Under enten `## Foredrag jeg gikk på` eller `## Foredrag jeg vil se opptak av`, i riktig dag-underseksjon, sett inn (sortert på tid):
    `- **[<HHMM> <Tittel>](talks/<filnavn>)** — <Taler(e)>`

11. **Bekreft.** Meld: `Registrert: <filnavn>`. Ikke commit – la brukeren gjøre det når de er klare.

## Ikke gjør

- Ikke lag et fyldig sammendrag på egen hånd – dette er en råregistrering. Bruk `/berik-foredrag` senere.
- Ikke commit eller push – bare skriv filer.
- Ikke overskriv en fil som allerede eksisterer. Meld heller: `<filnavn> finnes fra før – rediger direkte eller kjør /berik-foredrag`.
