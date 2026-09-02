---
name: planlegg-dagen
description: Use when the user wants to plan which talks to attend on an upcoming conference day — the evening before or the morning of. Presents the day's program, lets the user pick, and writes a personal schedule.
---

# planlegg-dagen

Lager en personlig timeplan for én konferansedag ut fra programmet. Brukerens språk: norsk.

Bruk: `/planlegg-dagen` eller `/planlegg-dagen <konferanse>` (f.eks. `/planlegg-dagen javazone`, `/planlegg-dagen KotlinConf 2026`).

## Steps

1. **Finn konferanse og dag.** Konferanse i prioritert rekkefølge:
   - Argument til skillen (fuzzy: match mot mappenavn under repo-roten, år valgfritt – uten år, ta nyeste årgang). Ukjent navn: vis tilgjengelige konferanser og spør.
   - Ellers: fra `pwd` hvis den er inne i `<Konferanse>/<År>/`.
   - Ellers: `AskUserQuestion`.
   Dag: anta dagens dato hvis den er en konferansedag (eller morgendagen hvis kvelden før); ellers spør. Endagskonferanser er dag 1.

2. **Hent programmet.** Foretrekk lokal cache `<Konferanse>/<År>/program.md`; fall tilbake til WebFetch av programlenken i konferansens README.

3. **Presenter og velg per tidsluke.** Gruppér dagens foredrag på starttid. For hver tidsluke med flere parallelle valg: bruk `AskUserQuestion` (multiSelect ved behov) med de mest relevante kandidatene som valg – tittel, rom og taler i labelen. Ta hensyn til brukerens interesser fra tidligere konferanser (tags i talk-filene) når kandidatene sorteres. Brukeren kan hoppe over en luke (pause/mingling).

4. **Kollisjoner → interest.** Når brukeren nevner at flere i samme luke frister, tilby å registrere taperne i «Foredrag jeg vil se opptak av»-listen med én gang. Følg da `/nytt-foredrag` steg 9–11a (les skillen – ikke gjenskap formatet fra hukommelsen): fil fra `_mal/talks/`-skjelettet med placeholder-sammendrag, 📋/🌐-lenker i metadata-linjen, README-indekslinje sortert på tid, og programraden markert `wishlist` med 👀-badge og 📝-lenke. Avslutt med badge-oppdateringen fra `/nytt-foredrag` steg 13 hvis noen ble registrert.

5. **Skriv timeplanen.** Lag/oppdater `<Konferanse>/<År>/plan-dag<N>.md` (endagskonferanser: `plan-dag1.md`):

   ```markdown
   # Min plan – <Konferanse> dag <N> (<dato>)

   | Tid | Rom | Foredrag | Taler(e) |
   |-----|-----|----------|----------|
   | 09:00 | Room 5 | ... | ... |
   ```

   Lenk planen fra konferansens README (egen linje under ingressen, f.eks. `Min plan: [dag 1](plan-dag1.md) · [dag 2](plan-dag2.md)`).

6. **Bekreft.** Vis planen kort. Ikke commit. Minn brukeren på at en pushet dagsplan forteller offentlig hvor de kommer til å være – vent med push til dagen er i gang.

## Underveis i dagen

Hopper brukeren over et planlagt foredrag («jeg hopper over neste foredrag», «dropper 15:40»): fjern raden fra `plan-dag<N>.md` og registrer foredraget som interest etter `/nytt-foredrag` steg 9–11b og 13 (talk-fil med placeholder, 👀-programrad med 📝-lenke, sortert README-ønskelistelinje med ⏳, tilbakelenke, badge). Rader for gjennomførte foredrag blir stående i planen – bare hoppede fjernes.

## Ikke gjør

- Ikke velg for brukeren – presenter kandidater, la dem bestemme.
- Ikke commit.
