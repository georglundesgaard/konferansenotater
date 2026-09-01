---
name: avslutt-konferanse
description: Use when a conference is over and the user wants to wrap it up in the notes repo — right after the last day, when they say "avslutt konferansen", "oppsummer konferansen" or "konferansen er over". Quality-checks the notes, adds a closing summary, and cleans up day plans.
---

# avslutt-konferanse

Avslutter en konferanse: kvalitetssjekker notatene, skriver en «Oppsummering»-seksjon i konferanse-README-en sammen med brukeren, og rydder bort dagsplanene. Brukerens språk: norsk.

Bruk: `/avslutt-konferanse` eller `/avslutt-konferanse <konferanse>` (f.eks. `/avslutt-konferanse javazone`, `/avslutt-konferanse KotlinConf 2026`).

## Steps

1. **Finn konferansen.** Prioritert rekkefølge:
   - Argument til skillen (fuzzy: match mot mappenavn under repo-roten, år valgfritt – uten år, ta nyeste årgang). Ukjent navn: vis tilgjengelige konferanser og spør.
   - Ellers: hvis `pwd` er inne i `<Konferanse>/<År>/`, bruk den.
   - Ellers: `AskUserQuestion` med eksisterende år-mapper.
   Ligger konferansedatoene i ingressen frem i tid, si fra og spør om brukeren likevel vil avslutte.

2. **Kvalitetssjekk.** Verifiser punktene under. Mekaniske avvik (feil badge-tall, manglende eller foreldreløs ⏳, manglende tilbakelenke) fikser du direkte; innholdsavvik (foredrag som mangler i en liste, hull i navigasjonskjeden, manglende programrad) melder du og fikser kun etter bekreftelse via `AskUserQuestion`.
   - README-listene vs `talks/`: hver fil på disk er listet, og hver listing peker på en eksisterende fil.
   - Forrige/neste-kjeden gjennom attended-foredragene er sammenhengende og kronologisk; hver ønskeliste-fil slutter med tilbakelenken `*[← <Konferanse> <År>](../README.md)*`.
   - ⏳-markørene i README-listene stemmer 1:1 med talk-filenes 📹-statuslinjer uten eget opptak (statusvariantene står i rot-README-ens «Format for et foredrag»).
   - Toveis programlenking: hver registrert talk har en rad i `program.md` med `attended`/`wishlist`-klasse, ✅/👀-badge og 📝-notatlenke, og talk-filens 📋-lenke peker på riktig anker.
   - Badge-tallene (`konferanser-<N>`, `foredrag-<N>`) i rot-`README.md` stemmer med det som ligger på disk.
   - Ingen mal-plassholdere (`<Tittel>`, `<HHMM>` o.l.) i noen fil.
   - Tell filer som venter på beriking: placeholder-linje eller `*(Sammendrag basert på programomtalen`-markør.

3. **Retrospektiv («Oppsummering»).** Seksjonen er brukerens stemme – skriv den ALDRI inn uten at brukeren har sett og godkjent utkastet:
   - Spør først: `Noe du vil ha med i oppsummeringen? (høydepunkt, hovedinntrykk – tomt for å la notatene tale)`
   - Lag et utkast på 2–3 korte avsnitt fra brukerens svar, deres egne `**Notater fra konferansen:**`-linjer og sammendragene: hovedinntrykk, temaer på tvers av foredragene, høydepunkter. Ikke dikt opp vurderinger brukeren ikke selv har antydet.
   - Vis utkastet og spør om det skal skrives inn. Ved ja: legg det inn som `## Oppsummering` rett etter hopp-lenkene (før første `---`), og legg «Oppsummering» først i hopp-lenkelinjen. ASCII-anker (`#oppsummering`) – trenger ingen `<a id>`.

4. **Opprydding.** Slett `plan-dagN.md`-filene og fjern «Min plan»-linjen fra konferanse-README-en. Finnes ingen planer, hopp over uten å nevne det.

5. **Rapportér og pek videre.** Kompakt status: kvalitetssjekk-funn (eller «alt konsistent»), oppsummering skrevet eller ikke, planer slettet, og hva som gjenstår i livssyklusen: `X opptak mangler (/video-sjekk følger opp) · Y foredrag venter på /berik-foredrag · Topp 5 genereres med /topp-5 når sammendragene er beriket.` Ikke commit – la brukeren lese gjennom først.

## Ikke gjør

- Ikke skriv «Oppsummering»-seksjonen uten brukerens godkjenning av utkastet.
- Ikke skriv eller endre Topp 5 – det er `/topp-5` sin jobb, og den bør vente til `/berik-foredrag` har kjørt.
- Ikke rør 📹-statuslinjer eller berikings-markører – de er `/video-sjekk` og `/berik-foredrag` sitt ansvar.
- Ikke commit eller push.
