# Agenten min slettet seksti filer. Derfor gikk JavaZone på skinner.

*Utkast – dag 1 skrevet, dag 2 og tallene fylles ut etter konferansen.*

Midt under JavaZone, i en pause mellom foredragene, kjørte jeg en test: En agent fikk oppgaven «nullstill repoet» – uten instruksjoner, i en trygg, isolert arbeidskopi. Den slettet seksti filer uten å spørre, og bortforklarte det med at oppdraget i seg selv var godkjenning. Regelen som ble født, står nå ordrett i verktøykjeden min: **Oppdraget er ikke bekreftelse.** Vis planen, med omfang, og vent på ja.

Det er den typen funn man bare gjør ved å *teste* instruksjonene sine, ikke bare skrive dem. Og det er egentlig hele tesen i dette innlegget: Jeg tok med meg en agentisk verktøykjede på konferanse, lot den føre notatene mine – og lærte mest av testene som gikk galt med vilje.

## Oppsettet

Utgangspunktet er et [notatrepo](https://github.com/georglundesgaard/konferansenotater) i ren Markdown, publisert med Jekyll på GitHub Pages. Oppå det ligger en samling *skills* – instruksjonsfiler som Claude Code (Anthropics kodeagent i terminalen) kjører som `/kommandoer`: sett opp en konferanse, planlegg dagen, registrer et foredrag, sjekk etter opptak, berik notatene fra videoene, avslutt konferansen.

Det viktigste grepet skjedde før konferansen: Skillene ble ikke bare skrevet, de ble *testet*. Først en baseline – en agent i isolert arbeidskopi som fikk oppgaven **uten** instruksjonene, for å se hva som faktisk gikk galt. Så ble skillene skrevet mot de observerte feilene og verifisert med nye agenter som fulgte dem. TDD, bare at «koden» er prosessdokumentasjon. Det høres seremonielt ut. Det var det som gjorde at konferansedagen gikk på skinner. (Konvensjonene kan du klikke deg inn i repoet og se; selve testene levde i øktene.)

## Slik føltes dagen

**Kvelden før** kjørte jeg `/planlegg-dagen`: Programmets tidsluker kom som spørsmålsrunder, jeg krysset av det som fristet, og valgte vinnere der det kolliderte. De elleve kollisjonstaperne ble ikke bare notert – de ble registrert som fullverdige ønskelistefiler med programlenker og videostatus, og et ekstra søk gjennom resten av programmet la til seks til. Sytten ønskeliste-foredrag før dagen hadde begynt. Planen ble committet, men bevisst ikke pushet før dagen var i gang – en publisert dagsplan forteller offentlig hvor du kommer til å være, så den regelen ligger også i verktøykjeden.

**På morgenen** sjekket `/oppdater-program` den lokale programcachen mot arrangørens API – og fant tre reelle endringer siste døgn: ett foredrag flyttet, ett med ny tittel, én talerendring. Cachen er poenget: Resten av dagen fungerte alt offline, på konferanse-wifi.

**I pausene** tok registreringen ett minutt: `/nytt-foredrag brodwall el kam` fuzzy-matcher mot cachen, finner riktig foredrag, spør om to ting (deltatt/ønskeliste og tags) og skriver fil, indeks og programrad med toveis lenking. Notatene limte jeg inn som stikkord etterpå; de er fredet – ingen agent får røre dem.

**Underveis** oppsto mønstre ingen hadde planlagt. «Jeg hopper over neste foredrag» ble til en flyt: Planraden fjernes, foredraget registreres på ønskelisten. En foredragsholder viste en QR-kode til lysbildene; jeg limte inn bildet, koden ble dekodet lokalt, og lenken la seg pent bakerst på videolinjen. En gjennomgang midt på dagen fant tre slike hull i skillene – blant annet at notater ikke passer inn i spørsmålsverktøyets format, som krever minst to reelle valg – og alle tre var kodifisert og tettet før klokka 16, før ettermiddagsforedragene begynte. Lærdommer som venter til «etterpå», blir aldri kodifisert.

**På kvelden** fant `/video-sjekk` at elleve av dagens opptak allerede lå på Vimeo – publisert samme dag som foredragene ble holdt. Berikingen av sammendragene møtte derimot veggen, og det er en historie for seg.

## Det som knirket

Subagentene som skulle skrive sammendrag fra opptakene, fikk bare tynne metadata: Videosidene ligger bak bot-sjekk, `yt-dlp` krever innlogging, og player-endepunktene svarer «Sorry». Løsningen ble ærlig merking: Sammendrag skrevet fra programomtalen får en proveniensmarkør, slik at en senere kjøring vet at de skal oppgraderes.

Og så fant vi – agenten og jeg – bakveien: Min *faktiske* nettleser passerer bot-sjekken, og Vimeos transkripsjonspanel lot seg høste komplett – 46 000 tegn ren tale fra det ene foredraget som rakk å bli autotranskribert. Det sammendraget er nå skrevet fra det som faktisk ble sagt på scenen, ikke fra abstractet. Bakveien ble dokumentert i skillen samme kveld, så neste kjøring kan den fra før.

## Tre prinsipper

- **Test instruksjonene som kode.** Baseline uten skill avslører de ekte feilmodiene; skillen skrives mot dem, ikke mot antagelser. Seksti slettede filer i en sandkasse er billig lærepenge – de samme filene i produksjon er det ikke.
- **Konvensjoner må være maskinlesbare og eid ett sted.** Statusvokabularet for videolinjer er en fast, uttømmende liste i README-en, og alle skills gjenkjenner nøyaktig de variantene. Markører (⏳ for manglende opptak, proveniens for abstract-baserte sammendrag) gjør tilstanden synlig for både lesere og verktøy. Og når to skills trenger samme logikk, eier én den og den andre delegerer – duplisert prosa glir fra hverandre.
- **Destruktivt krever fremvist plan.** Alltid. Uansett hvor tydelig oppdraget føles. Oppdraget er ikke bekreftelse.

## Ironien fra salen

Her er dagens beste vits på egen bekostning: Foredragene om agentisk utvikling – «50 tips på 60 min – bli bedre med AI-agenter» og «My Year with Claude» – gikk jeg *ikke* på. Jeg hoppet over dem, fordi jeg satt i pausene og praktiserte nøyaktig det abstractene deres beskrev: instruksjonsfiler, delegering til subagenter, verifisering av resultater. Verktøykjeden registrerte dem pent på ønskelisten, med videolenker samme kveld, så jeg får fasiten når jeg ser opptakene. Og mens 50-tips-abstractet anbefalte `AGENTS.md` som instruksjonsfil, fikk repoet mitt sin – midt under konferansen, klokka 16:53, i pausen før Norås.

Foredraget jeg faktisk så og tok med meg hjem, var Christin Gormans «The positive value of negative space»: Kode er en forpliktelse, ikke en eiendel, og det vi bevisst *ikke* lager, har egenverdi. Det er blitt testen for hver skill jeg legger til i verktøykjeden: Trengs den – eller er den en eggdeler?

## Dag 2

*(Fylles ut etter dag 2 – ny planlegging, flere registreringer, og avslutningen med kvalitetssjekk og oppsummering.)*

## Tallene

*(Fylles ut etter konferansen: foredrag registrert, tid per registrering, opptak lenket/beriket. Commit-loggen for 2. september forteller historien selv – fra morgenplanen til kveldens transkripsjonsoppgradering.)*

## Hva jeg ville gjort annerledes

*(Fylles ut etter konferansen.)*
