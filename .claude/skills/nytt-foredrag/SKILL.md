---
name: nytt-foredrag
description: Use when the user wants to register a new conference talk — either one they attended or one they want to watch later. Walks them through a short Norwegian interview and produces the per-talk markdown file plus updates the conference README index.
---

# nytt-foredrag

Interviews the user for a single talk, then writes the file and updates the conference README. Everything user-facing in Norwegian.

## When to use

- User types `/nytt-foredrag` (or asks in Norwegian to "registrere et foredrag", "legge til en talk", "notere en sesjon")
- User wants to add a talk during or right after a conference
- User skips a planned talk («jeg hopper over neste foredrag») → follow «Underveis i dagen» in `/planlegg-dagen` (fjern planraden, registrer som interest)

## Steps

1. **Finn konferansen.**
   - Hvis `pwd` er inne i `<Konferanse>/<År>/`, bruk den. Meld: `Konferanse: <navn> <år>`.
   - Ellers: bruk `AskUserQuestion` med eksisterende `<Konferanse>/<År>/`-mapper som valg, pluss "Ny konferanse". Ved "Ny konferanse": kjør `/ny-konferanse`-skillen (den setter opp mappen, README og programcache), og fortsett deretter her.

2. **Spør om selve foredraget** (én åpen prompt):
   `Beskriv foredraget – noen stikkord holder (tittel, taler, tid, tema … jeg matcher mot programmet).`
   Argumenter gitt direkte til skillen (`/nytt-foredrag <beskrivelse>`) brukes som svar uten å spørre på nytt. NB: argumentet er en foredragsbeskrivelse, ikke et konferansenavn (ulikt `/video-sjekk` og `/berik-foredrag`). Ligner argumentet kun på et konferansenavn (f.eks. `/nytt-foredrag javazone`), avklar med brukeren i stedet for å fuzzy-matche det mot foredragstitler.

3. **Match mot programmet.** Sjekk først om `<Konferanse>/<År>/program.md` finnes (lokal cache – foretrukket, fungerer offline). Hvis ikke: finn programlenken i konferansens `README.md` (under Kilder, f.eks. `kotlinconf.com/talks/`, `2026.javazone.no/program`) og WebFetch den. Match brukerens beskrivelse mot foredragene – fuzzy på tittel, taler og tema. Bruk match til å fylle inn eksakt tittel, taler(e) og starttid (HHMM).
   - Én klar match: vis den kort (`Fant: <tid> <tittel> — <taler>`) og fortsett.
   - Flere kandidater: `AskUserQuestion` med toppkandidatene.
   - Ingen match (eller programmet er utilgjengelig): fall tilbake til manuell parsing av beskrivelsen – første `\d{4}` er tid, split på ` — ` eller ` - ` for taler, resten er tittel. Ved hull, still én kort oppfølging.

4. **Dag.** Avgjør endags/flerdags fra konferansens `README.md`: dekker datolinjen i ingressen mer enn én dag (f.eks. «2.–3. september»), er den flerdags. Ikke tell filer i `talks/` – katalogen kan være tom. For flerdags: bruk dagen fra program-matchen hvis den er kjent; ellers anta dagens dato hvis den faller innenfor konferansedagene (meld kort hvilken dag som ble antatt, f.eks. `Antar dag 1 (onsdag)`); ellers spør `AskUserQuestion`.

5. **Attended eller interest?** `AskUserQuestion` med to valg: `attended` / `interest`.

6. **Notater.** Åpent innspill – egner seg IKKE som `AskUserQuestion` (den krever minst to reelle valg, og notater har bare ett: lim inn). Si i stedet, sammen med status/tags-spørsmålet: «notater limer du bare inn etterpå». Når notater kommer (nå eller senere i samtalen): konverter linjeskift til `- `-liste. Hopp over blokken hvis interest eller ingen notater.

7. **Tags.** Spør: `Tags? (kommaseparert – eller tomt for å hoppe over)`. Wrap hver i `` ` `` og join med ` · `.

8. **Video-status.** Under konferansen er opptaket aldri ute – ikke spør, bare meld at standard-fallbacken brukes (finn den ved å skumme README, f.eks. `Video ikke publisert ennå – se [smidig.no](https://www.smidig.no/)`) og la brukeren overstyre med en lenke hvis de har en. Deler brukeren en lysbilde-lenke (eller QR-kode til en): legg den bakerst på 📹-linjen som ` Lysbilder: [<kilde>](<url>).` – statusfrasen først på linjen må bestå.

9. **Slug + filsti.**
   - Slug: lowercase, ikke-alfanumerisk → `-`, kollaps, trim, kutt til 40 tegn.
   - Filnavn: `dayN-HHMM-<slug>.md` for flerdags, `HHMM-<slug>.md` for endags.
   - Sti: `<Konferanse>/<År>/talks/<filnavn>`.

10. **Skriv fil.** Bruk skjelettet fra `_mal/talks/HHMM-slug.md` (kanonisk kilde – les den, ikke gjenskap fra hukommelsen). Fyll inn tittel, metadata-linje, notater (kun attended), tags og 📹-linje. Behold placeholder-linjen `*(Sammendrag fylles inn senere – bruk /berik-foredrag når opptaket er publisert.)*` som sammendrag – den er signalet `/berik-foredrag` ser etter. (Notatblokken bor i talk-filen frem til `/berik-foredrag` verifiserer den mot opptaket, fletter den inn i sammendraget og arkiverer rånotatene i `_notater/`.)
    - Hvis `program.md` finnes og talken ble matchet der: legg til ` · 📋 [i programmet](../program.md#<anker>)` bakerst i metadata-linjen (anker = tidsluke-headingen, `#d<dag>-<hhmm>`), og deretter ` · 🌐 [offisiell beskrivelse](<url>)` med URL-en fra programradens 🌐-lenke.

11. **Oppdater konferanse-README.** Åpne `<Konferanse>/<År>/README.md`. Under enten `## Foredrag jeg gikk på` eller `## Foredrag jeg vil se opptak av`, i riktig dag-underseksjon, sett inn (sortert på tid):
    `- **[<HHMM> <Tittel>](talks/<filnavn>)** — <Taler(e)>`
    Fikk foredraget en statuslinje uten eget opptak i steg 8, avslutt raden med ` ⏳` (fjernes av `/video-sjekk` når opptaket lenkes inn).

11a. **Oppdater programraden.** Hvis `program.md` finnes og talken ble matchet der: sett radens `<tr>`-klasse til `attended` eller `wishlist`, legg ✅/👀-badge foran tittelen, og fyll Notater-cellen med `<a class="notes-link" href="talks/<filnavn med .html>">📝 notater</a>` – slik at programmet lenker begge veier. (Én-setnings oppsummering i Notater-cellen kommer fra `/berik-foredrag` senere.)

11b. **Avslutt filen med navigasjon.** For interest-foredrag: avslutt filen med `*[← <Konferanse> <År>](../README.md)*` (tilbakelenke – de har ingen forrige/neste-kjede). For attended: vedlikehold forrige/neste-kjeden som følger. Attended-talks har en avsluttende navigasjonslinje på formen `*[← <forrige>](<fil>) · [<neste> →](<fil>)*`. Finn den nye talkens kronologiske plass blant attended-filene (README-listen er fasit), og:
    - Legg navigasjonslinje nederst i den nye filen (utelat «forrige» hvis først, «neste» hvis sist).
    - Oppdater navigasjonslinjen i nabo-filene (forrige fils «neste»-lenke og neste fils «forrige»-lenke) så kjeden forblir sammenhengende.

12. **Bekreft og loop.** Meld: `Registrert: <filnavn>`. Spør så: `Ett til? (beskriv neste foredrag, eller tomt for å avslutte)`. Ved nytt svar: gå til steg 3 med samme konferanse og dag-kontekst. Ikke commit – la brukeren gjøre det når de er klare.

13. **Oppdater foredrag-badgen.** Når loopen avsluttes: tell talk-filene på tvers av alle konferanser (`<Konferanse>/<År>/talks/*.md`, ignorer `.gitkeep`) og oppdater `foredrag-<antall>`-badgen øverst i rot-`README.md` hvis tallet har endret seg.

## Ikke gjør

- Ikke lag et fyldig sammendrag på egen hånd – dette er en råregistrering. Bruk `/berik-foredrag` senere.
- Ikke commit eller push – bare skriv filer.
- Ikke overskriv en fil som allerede eksisterer. Meld heller: `<filnavn> finnes fra før – rediger direkte eller kjør /berik-foredrag`.
