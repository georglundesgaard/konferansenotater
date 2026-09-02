# Jeg tok med en agentisk verktøykjede på JavaZone

*Utkast – dag 1 skrevet, dag 2 og tallene fylles ut etter konferansen.*

Alle snakker om agentisk utvikling for tiden. På JavaZone 2026 satt jeg i salen og hørte foredrag om AI-agenter, instruksjonsfiler og delegering – mens jeg i pausene praktiserte nøyaktig det foredragene beskrev: Jeg hadde tatt med meg en agentisk verktøykjede på konferansen, og lot den føre notatene mine.

Dette er historien om det eksperimentet – hva som fungerte, hva som knirket, og hvilke prinsipper som vokste frem underveis. Repoet du leser dette i er selve demoen: hver konvensjon jeg beskriver, kan du klikke deg inn og se.

## Oppsettet

Utgangspunktet er et [notatrepo](https://github.com/georglundesgaard/konferansenotater) i ren markdown, publisert med Jekyll på GitHub Pages. Oppå det ligger en samling *skills* – instruksjonsfiler i `.claude/skills/` som Claude Code kjører som `/kommandoer`: sett opp en konferanse, planlegg dagen, registrer et foredrag, sjekk etter opptak, berik notatene fra videoene, avslutt konferansen.

Det viktigste grepet skjedde før konferansen: skillene ble ikke bare skrevet, de ble *testet*. Først en baseline – en agent i isolert arbeidskopi som fikk oppgaven **uten** instruksjonene, for å se hva som faktisk gikk galt. Så ble skillen skrevet mot de observerte feilene, og verifisert med nye agenter som fulgte den. TDD, bare at «koden» er prosessdokumentasjon. Det høres seremonielt ut. Det var det som gjorde at dag 1 gikk på skinner.

## Slik føltes dagen

**Kvelden før** kjørte jeg `/planlegg-dagen`: programmets tidsluker kom som spørsmålsrunder, jeg krysset av det som fristet, og valgte vinnere der det kolliderte. Kollisjonstaperne ble ikke bare notert – de ble registrert som fullverdige ønskeliste-filer med programlenker og videostatus, elleve stykker, før dagen hadde begynt.

**På morgenen** sjekket `/oppdater-program` den lokale programcachen mot arrangørens API – og fant tre reelle endringer siste døgn: ett foredrag flyttet, ett med ny tittel, én taler-endring. Cachen er poenget: resten av dagen fungerte alt offline, på konferanse-wifi.

**I pausene** var registrering ett minutt: `/nytt-foredrag brodwall el kam` fuzzy-matcher mot cachen, finner riktig foredrag, spør om to ting (deltatt/ønskeliste og tags), og skriver fil, indeks og programrad med toveis lenking. Notatene limte jeg inn som stikkord etterpå; de er fredet – ingen agent får røre dem.

**Underveis** oppsto mønstre ingen hadde planlagt. «Jeg hopper over neste foredrag» ble til en flyt: planraden fjernes, foredraget registreres på ønskelisten. En foredragsholder viste QR-kode til lysbildene; jeg limte inn bildet, koden ble dekodet lokalt, og lenken la seg pent bakerst på videolinjen. Begge deler ble kodifisert i skillene *samme dag* – en mid-day review fant tre slike hull, og kvelden etter var de tettet.

**På kvelden** fant `/video-sjekk` at elleve av dagens opptak allerede lå på Vimeo – publisert samme dag som foredragene ble holdt. Berikingen av sammendragene møtte derimot veggen, og det er sin egen historie.

## Det som knirket

**Vimeos bot-vegg.** Sub-agentene som skulle skrive sammendrag fra opptakene, fikk bare tynne metadata: videosidene ligger bak bot-sjekk, `yt-dlp` krever innlogging, og player-endepunktene svarer «Sorry». Løsningen ble ærlig merking: sammendrag skrevet fra programomtalen får en proveniens-markør, slik at en senere kjøring vet at de skal oppgraderes. Og så fant vi bakveien: min *faktiske* nettleser passerer bot-sjekken, og Vimeos transkripsjonspanel lot seg høste komplett – 46 000 tegn ren tale fra det ene foredraget som rakk å bli autotranskribert. Det sammendraget er nå skrevet fra det som faktisk ble sagt på scenen, ikke fra abstractet.

**Verktøygrensene former arbeidsflyten.** Spørsmålsverktøyet krever minst to reelle valg – «lim inn notater» har bare ett. Første forsøk feilet, og løsningen (åpne innspill går utenom spørsmålene) ble en dokumentert del av skillen.

**Den viktigste lærdommen kom fra en test.** Da jeg bygde `/nullstill` (som lar andre forke repoet og vaske bort notatene mine), fikk baseline-agenten – uten instruksjoner, i trygg sandkasse – oppgaven «nullstill repoet». Den slettet seksti filer uten å spørre, med rasjonaliseringen at oppdraget i seg selv var godkjenning. Regelen som ble født: **oppdraget er ikke bekreftelse.** Vis planen, med omfang, og vent på ja. Testen med «bare fjern alt, jeg stoler på deg» bekreftet at regelen holder.

## Prinsippene som vokste frem

- **Test instruksjoner som kode.** Baseline uten skill avslører de ekte feilmodiene; skillen skrives mot dem, ikke mot antagelser.
- **Én kanonisk kilde per logikk.** Når to skills trenger samme oppførsel, eier én den – den andre delegerer. Duplisert prosa drifter.
- **Konvensjoner må håndheves av verktøyene som leser dem.** Statusvokabularet for videolinjer er *enumerert*, og alle skills gjenkjenner nøyaktig de variantene. Markører (⏳ for manglende opptak, proveniens for abstract-baserte sammendrag) gjør tilstand synlig og maskinlesbar.
- **Destruktivt krever fremvist plan.** Alltid. Uansett hvor tydelig oppdraget føles.
- **Verktøykjeden skal lære samme dag.** Hullene fra formiddagen var tettet før kvelden – lærdommer som venter til «etterpå», blir aldri kodifisert.

## Ekkoet fra salen

Det underligste med dagen var speilingen. Formiddagens foredrag om 50 AI-agent-tips handlet om instruksjonsfiler, subagenter og verifisering – mens repoet mitt fikk sin `AGENTS.md` samme uke. «My Year with Claude» beskrev arbeidsformen som klar retning, god delegering og systematisk verifisering av resultater – som er nøyaktig hva skill-TDD-en og plan-og-bekreft-portene er. Og Christin Gorman minnet salen om at kode er en forpliktelse, ikke en eiendel – en god test for hver skill jeg legger til: trengs den, eller er den en eggdeler?

## Dag 2

*(Fylles ut etter dag 2 – ny planlegging, flere registreringer, og avslutningen med kvalitetssjekk og oppsummering.)*

## Tallene

*(Fylles ut etter konferansen: antall commits under konferansen, foredrag registrert, tid per registrering, opptak lenket/beriket.)*

## Hva jeg ville gjort annerledes

*(Fylles ut etter konferansen.)*
