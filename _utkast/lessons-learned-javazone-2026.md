# Jeg dro på JavaZone uten laptop

*Utkast – komplett med epilog; siste gjennomlesning før publisering.*

> **TL;DR:** Jeg dro på JavaZone 2026 uten laptop og lot en agentisk verktøykjede føre notatene, styrt fra telefonen. Instruksjonene ble testet som kode før konferansen – og de viktigste lærdommene kom fra testene som gikk galt med vilje: Oppdraget er ikke bekreftelse, og et sammendrag uten proveniens er en antagelse som ser ut som kunnskap. *Innlegget er laget med KI, skrevet fra mine egne notater og økter.*
>
> **Les også:** [JavaZone 2026: AI overalt – og motvektene som traff best](../blogg/javazone-2026-oppsummering.md) – oppsummeringen av selve konferansen.
<!-- Ved flytting til blogg/: endre lenken over til javazone-2026-oppsummering.md (sibling), og fjern denne kommentaren. -->



Konferansesekken inneholdt ingen PC. Alt – planlegging, registrering, commits – ble styrt fra telefonen, mot en agentisk verktøykjede på maskinen hjemme. Registrering av et foredrag tok omtrent ett minutt av en pause; resten av tiden var jeg på konferanse.

Dette innlegget handler om hvordan det gikk – og om det som gjorde det mulig: Instruksjonene ble ikke bare skrevet, de ble *testet* som kode. Jeg lot verktøykjeden føre notatene mine, og lærte mest av testene som gikk galt med vilje.

## Oppsettet

Utgangspunktet er et [notatrepo](https://github.com/georglundesgaard/konferansenotater) i ren Markdown, publisert med Jekyll på GitHub Pages. Oppå det ligger en samling *skills* – instruksjonsfiler som Claude Code (Anthropics kodeagent i terminalen) kjører som `/kommandoer`: sett opp en konferanse, planlegg dagen, registrer et foredrag, sjekk etter opptak, berik notatene fra videoene, avslutt konferansen.

Det viktigste grepet skjedde før konferansen: Skillene ble ikke bare skrevet, de ble *testet*. Først en baseline – en agent i isolert arbeidskopi som fikk oppgaven **uten** instruksjonene, for å se hva som faktisk gikk galt. Så ble skillene skrevet mot de observerte feilene og verifisert med nye agenter som fulgte dem. TDD, bare at «koden» er prosessdokumentasjon. Det høres seremonielt ut. Det var det som gjorde at konferansedagen gikk på skinner. (Konvensjonene kan du klikke deg inn i repoet og se; selve testene levde i øktene.)

Ett eksempel på hva slike tester fanger – kjørt i en pause midt under konferansen: `/nullstill` er en bitteliten feature, lagt til kun for at andre skal kunne gjenbruke repoet. Baseline-testen av den lærte meg likevel mer enn mange av de store: En agent fikk oppgaven «nullstill repoet» uten instruksjoner, i en trygg, isolert arbeidskopi – og slettet seksti filer uten å spørre, med bortforklaringen at oppdraget i seg selv var godkjenning. Regelen som ble født, står nå ordrett i verktøykjeden: **Oppdraget er ikke bekreftelse.** Vis planen, med omfang, og vent på ja.

## Slik føltes dagen

**Kvelden før** kjørte jeg `/planlegg-dagen`: Programmets tidsluker kom som spørsmålsrunder, jeg krysset av det som fristet, og valgte vinnere der det kolliderte. De elleve kollisjonstaperne ble ikke bare notert – de ble registrert som fullverdige ønskelistefiler med programlenker og videostatus, og et ekstra søk gjennom resten av programmet la til seks til. Sytten ønskeliste-foredrag før dagen hadde begynt. Planen ble committet, men bevisst ikke pushet før dagen var i gang – en publisert dagsplan forteller offentlig hvor du kommer til å være, så den regelen ligger også i verktøykjeden.

**På morgenen** sjekket `/oppdater-program` den lokale programcachen mot arrangørens API – og fant tre reelle endringer siste døgn: ett foredrag flyttet, ett med ny tittel, én talerendring. Cachen er poenget: Resten av dagen fungerte alt offline, på konferanse-wifi.

**I pausene** tok registreringen ett minutt: `/nytt-foredrag brodwall el kam` fuzzy-matcher mot cachen, finner riktig foredrag, spør om to ting (deltatt/ønskeliste og tags) og skriver fil, indeks og programrad med toveis lenking. Notatene limte jeg inn som stikkord etterpå; de er fredet – ingen agent får røre dem.

**Underveis** oppsto mønstre ingen hadde planlagt. «Jeg hopper over neste foredrag» ble til en flyt: Planraden fjernes, foredraget registreres på ønskelisten. En foredragsholder viste en QR-kode til lysbildene; jeg limte inn bildet, koden ble dekodet lokalt, og lenken la seg pent bakerst på videolinjen. En gjennomgang midt på dagen fant tre slike hull i skillene – blant annet at notater ikke passer inn i spørsmålsverktøyets format, som krever minst to reelle valg – og alle tre var kodifisert og tettet før klokka 16, før ettermiddagsforedragene begynte. Lærdommer som venter til «etterpå», blir aldri kodifisert.

**På kvelden** fant `/video-sjekk` at elleve av dagens opptak allerede lå på Vimeo – publisert samme dag som foredragene ble holdt. Berikingen av sammendragene møtte derimot veggen, og det er en historie for seg.

**Og resten av kvelden** hørte konferansen til, ikke verktøykjeden: en runde quiz og sosialt på messegulvet med gamle og nåværende kolleger, før Matoma entret scenen klokka 21 og leverte en times forrykende show. Notatene tar seg av seg selv – det er jo hele poenget.

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

Dag 2 var testen på om dag 1 var flaks. Det var den ikke – men den føltes annerledes: kjedeligere, i ordets beste betydning. Planleggingen om morgenen tok minutter, registreringene i pausene var rutine, og hopp-flyten som ble improvisert i går, var nå dokumentert oppførsel. Verktøykjeden hadde sluttet å være eksperimentet og begynt å være notatboken.

Ironien fikk også en oppfølger: Dagens program hadde et foredrag som bokstavelig talt handlet om metoden min – «Trust, But Verify: Skill-Driven Development for the Sceptical Java Developer». Jeg hoppet over det også. Det ligger på ønskelisten, pent registrert av skillene det handler om.

Infrastrukturen fikk også sin test. Fjernstyringen fra telefonen fungerte utmerket hele dag 1 – men dag 2 bød på utfall flere ganger og merkbare forsinkelser. Mistanken var at hjemme-PC-en hadde gått i dvale, og strømloggen bekreftet det om kvelden med tall som ikke lot seg misforstå: 56 dvale-hendelser i arbeidstiden dag 2, mot null dag 1. Maskinen døset mellom hver økt, og hver kommando fra konferansegulvet måtte først vekke den. Lærdommen er banal og viktig: Den svakeste lenken i en agentisk verktøykjede er ikke agenten – det er strømsparingsinnstillingene på maskinen den bor på.

Kvelden ga en lærdom om tålmodighet. JavaZone publiserte 20 nye opptak samme dag – fem av dem foredrag jeg selv satt i – men Vimeos autotranskripsjoner var ikke generert ennå; selv gårsdagens videoer manglet. Planen om en full transkripsjonsrunde ble justert på fakta: Alle 30 abstract-baserte sammendrag bærer proveniensmarkøren og oppgraderes i én samlet runde når transkripsjonene finnes. Verktøykjeden vet forskjellen på det den vet og det den antar – det er kanskje det viktigste enkelttrekket ved hele designet.

## Tallene

To konferansedager ga **26 commits** – fra morgenplanen 2. september kl. 09:13 til avslutningscommiten 3. september kl. 20:20 – alle styrt fra telefonen. Resultatet: **43 foredragsfiler** for JavaZone alene (9 jeg deltok på, 34 på ønskelisten), **45 egne notatlinjer** skrevet i pausene, **31 opptak lenket** – de fleste samme dag som foredraget ble holdt – og 31 sammendrag på plass i første versjon. Fem planlagte foredrag ble hoppet over underveis; alle fem ble automatisk konvertert til ønskeliste-oppføringer i stedet for å forsvinne.

Verktøykjeden selv vokste også: Dagen før konferansen fantes ni skills; nå er det ti, pluss `AGENTS.md`, lisens og seks skill-forbedringer kodifisert *mens* konferansen pågikk. Foredragstelleren i repoet gikk fra 59 til 102 på tre dager. Og den kanskje viktigste målingen har ingen enhet: Registrering av et foredrag tok omtrent ett minutt av en pause – resten av tiden var jeg på konferanse.

## Hva jeg ville gjort annerledes

- **Skrudd av dvalemodus på hjemme-PC-en før avreise.** Fjernstyringen fra telefonen var sømløs dag 1 og hakkete dag 2 – strømloggen viste i etterkant 56 dvale-hendelser i arbeidstiden. Én `caffeinate`-kommando hadde spart alle utfallene.
- **Ventet noen dager med videojakten.** Opptakene kom imponerende raskt, men transkripsjonene tar sin tid – og beriking uten dem gir sammendrag som uansett skal oppgraderes. Neste gang: `/video-sjekk` som ukentlig rutine fra noen dager etter konferansen, og berikingsrundene når kildene faktisk er klare. Markørsystemet gjør heldigvis gjentatte runder billige – ferdig berikede foredrag hoppes over automatisk.

Og ett punkt jeg *ikke* ville gjort annerledes: hoppene. Fem planlagte foredrag røk til fordel for messegulvet – å gå rundt, snakke med folk og ta inn inntrykk er en vel så viktig del av konferansen som salene. Planen viser hva jeg ville sett om foredrag var alt; ønskelisten fanger dem når de ikke er det. Det er ikke et avvik fra systemet – det er systemet.

## Epilog: da transkripsjonene kom

Tålmodigheten fra dag 2 betalte seg. En snau uke etter konferansen hadde Vimeo generert autotranskripsjoner, og den utsatte berikingsrunden kjørte i én økt: 30 JavaZone-sammendrag skrevet på nytt fra det som faktisk ble sagt på scenen, hentet via bakveien gjennom min egen nettleser – som nå er dokumentert steg for steg i skillen. Proveniensmarkørene gjorde runden triviell: Verktøykjeden visste nøyaktig hvilke sammendrag som var antagelser og hvilke som var kunnskap.

Så kom den ubehagelige testen. Samme flyt ble kjørt mot KotlinConf-notatene fra mai – sammendrag skrevet *før* markørsystemet fantes, uten proveniens. Verifiseringen mot transkripsjonene avslørte at flere av dem inneholdt selvsikre detaljer som aldri forekom i foredragene: et observabilitetsbibliotek som ikke nevnes i opptaket, en feilhåndterings-DSL taleren eksplisitt *ikke* brukte, verktøy og protokoller lånt fra helt andre sammenhenger. Ingen vond vilje – bare en språkmodell som fylte hull med plausibilitet. Lærdommen er prinsippet fra dag 2 i skarpere form: **Et sammendrag uten proveniens er en antagelse som ser ut som kunnskap.** Nå bærer alt enten transkripsjonsbelegg eller markør.

Notatregelen fikk også sin oppgradering. «Ingen agent rører notatene» står fortsatt – men notatene blir nå *verifisert* mot opptaket, flettet inn i sammendragene og arkivert ordrett i en upublisert mappe, med korreksjoner som kursiverte merknader under punktet i stedet for endringer i det. Tjuefire foredrag på tvers av tre konferanser har vært gjennom den kverna nå, og verifiseringen ga til og med en hyggelig overraskelse: Et notatpunkt som ikke fantes i transkripsjonen, viste seg – etter et kjapt intervju med meg – å stå på et lysbilde 42 minutter inn i foredraget. Notatet var riktig. Det var bare aldri sagt høyt.

## Hva jeg vil prøve neste gang

- **Diktere i stedet for å taste.** Claude-appen har dikteringsfunksjon, og pausene er korte: I stedet for å knote inn stikkord på telefonen vil jeg prøve å *snakke* inn inntrykkene rett etter foredraget – tilbakemeldinger, høydepunkter, det jeg ville sagt til en kollega – og la agenten strukturere det til notatpunkter.
- **Intervjuform på registreringen.** Diktering kombinert med at skillen stiller et par korte oppfølgingsspørsmål – hva traff, hva var du uenig i, hvem bør se dette? – kan gi rikere notater enn dagens stikkordsinnliming, uten å ta mer av pausen.
- **Bedre navn på skillen.** `/nytt-foredrag` beskriver filen som opprettes, ikke det jeg faktisk gjør. `/registrer-foredrag` – eller `/registrer-deltagelse` – sier det bedre. Navn bør beskrive handlingen, ikke artefakten.
