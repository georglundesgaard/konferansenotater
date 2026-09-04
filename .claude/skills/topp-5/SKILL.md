---
name: topp-5
description: Use when the user wants to generate, refresh or regenerate the "Anbefalt: Topp 5" recommendations in a conference README — typically after /berik-foredrag has enriched wishlist summaries, or on "oppdater topp 5", "regenerer topp 5", "foreslå topp 5".
---

# topp-5

Foreslår eller regenererer «Anbefalt: Topp 5 fra ønskelisten» i en konferanse-README. Dette er den kanoniske Topp 5-logikken – `/berik-foredrag` og `/avslutt-konferanse` delegerer hit i stedet for å ha egne varianter. Brukerens språk: norsk.

Bruk: `/topp-5` eller `/topp-5 <konferanse>` (f.eks. `/topp-5 javazone`, `/topp-5 KotlinConf 2026`).

## Steps

1. **Finn konferansen.** Prioritert rekkefølge:
   - Argument til skillen (fuzzy: match mot mappenavn under repo-roten, år valgfritt – uten år, ta nyeste årgang). Ukjent navn: vis tilgjengelige konferanser og spør.
   - Ellers: hvis `pwd` er inne i `<Konferanse>/<År>/`, bruk den.
   - Ellers: `AskUserQuestion` med eksisterende år-mapper.
   Har README-en ingen Topp 5-seksjon (enkeltsporede konferanser, som SmidigDig): meld «<Konferanse> <År> er enkeltsporet og har ingen Topp 5-seksjon – ingenting å gjøre.» og stopp.

2. **Velg kandidater.** Fra «Foredrag jeg vil se opptak av»-listen, kun foredrag med publisert eget opptak (📹-linje med lenke til selve opptaket). Foredrag med ⏳/statuslinje utelates – listen er en «se disse opptakene»-anbefaling. Noter hvor mange som ble utelatt av den grunn, til rapporten i steg 5.

3. **Ranger etter brukerens faktiske interesser.** Les `**Notater fra konferansen:**`-linjene i attended-filene – eller `<År>/_notater/<slug>.md` for talks der notatene alt er arkivert etter verifisert beriking (vurderingene er da også vevd inn i sammendragene) – pluss tagsene: positive notater («interessant», «nyttig») er sterke signaler for temaet, negative («traff ikke») er motsignaler. Velg de fem ønskeliste-foredragene som best spinner videre på temaene brukeren fulgte tett, og skriv én setnings begrunnelse per foredrag forankret i det faktiske sammendraget – ikke funnet på. Formatet er README-ens eksisterende: nummerert liste, `**[<Tittel>](talks/<fil>.md)** — <Taler>. <Begrunnelse>.`, mest relevant først. Oppdater intro-setningen hvis temaene har endret seg.

4. **Vis gammel → ny og spør – ALLTID.** Vis eksisterende seksjon og forslaget side om side (ved tom seksjon: bare forslaget) og spør via `AskUserQuestion` om det skal skrives inn. Dette gjelder uansett hvordan brukeren formulerte oppdraget: «regenerer», «oppdater» eller «bare fiks listen» er IKKE forhåndsgodkjenning av et konkret innhold – brukeren skal se hva som ryker ut og hva som kommer inn før noe skrives. Ikke skriv først og vis etterpå.

5. **Skriv ved ja og rapportér.** Behold seksjonsoverskrift og anker uendret. Meld kort: hva som ble byttet ut, og eventuelt «Y ønskeliste-foredrag mangler fortsatt opptak og ble ikke vurdert – kjør /topp-5 igjen etter /video-sjekk.» Ikke commit.

## Ikke gjør

- Ikke skriv listen uten at brukeren har sett gammel → ny og sagt ja – «oppdraget var å regenerere» er ikke et unntak.
- Ikke anbefal foredrag uten publisert opptak.
- Ikke endre noe annet i README-en enn Topp 5-seksjonen.
- Ikke commit eller push.
