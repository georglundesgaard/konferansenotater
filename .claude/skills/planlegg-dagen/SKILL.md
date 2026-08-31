---
name: planlegg-dagen
description: Use when the user wants to plan which talks to attend on an upcoming conference day — the evening before or the morning of. Presents the day's program, lets the user pick, and writes a personal schedule.
---

# planlegg-dagen

Lager en personlig timeplan for én konferansedag ut fra programmet. Brukerens språk: norsk.

## Steps

1. **Finn konferanse og dag.** Konferanse fra `pwd` eller `AskUserQuestion`. Dag: anta dagens dato hvis den er en konferansedag (eller morgendagen hvis kvelden før); ellers spør.

2. **Hent programmet.** Foretrekk lokal cache `<Konferanse>/<År>/program.md`; fall tilbake til WebFetch av programlenken i konferansens README.

3. **Presenter og velg per tidsluke.** Gruppér dagens foredrag på starttid. For hver tidsluke med flere parallelle valg: bruk `AskUserQuestion` (multiSelect ved behov) med de mest relevante kandidatene som valg – tittel, rom og taler i labelen. Ta hensyn til brukerens interesser fra tidligere konferanser (tags i talk-filene) når kandidatene sorteres. Brukeren kan hoppe over en luke (pause/mingling).

4. **Kollisjoner → interest.** Når brukeren nevner at flere i samme luke frister, tilby å registrere taperne i «Foredrag jeg vil se opptak av»-listen med én gang (samme filformat som `/nytt-foredrag`, med placeholder-sammendrag).

5. **Skriv timeplanen.** Lag/oppdater `<Konferanse>/<År>/plan-dag<N>.md`:

   ```markdown
   # Min plan – <Konferanse> dag <N> (<dato>)

   | Tid | Rom | Foredrag | Taler(e) |
   |-----|-----|----------|----------|
   | 09:00 | Room 5 | ... | ... |
   ```

   Lenk planen fra konferansens README (egen linje under ingressen, f.eks. `Min plan: [dag 1](plan-dag1.md) · [dag 2](plan-dag2.md)`).

6. **Bekreft.** Vis planen kort. Ikke commit.

## Ikke gjør

- Ikke velg for brukeren – presenter kandidater, la dem bestemme.
- Ikke commit.
