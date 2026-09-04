# JavaZone 2026: AI overalt – og motvektene som traff best

*4. september 2026*

> **TL;DR:** To dager på Nova Spektrum: AI i annethvert foredrag, men motvektene traff best – Gormans forsvar for det negative rommet og Heggelund Hansens påminnelse om at vi gjør ting vanskeligere enn de trenger å være. Pluss topp 5 fra ønskelisten og fire ønsker til neste års program. *Innlegget er laget med KI, skrevet fra mine egne notater og vurderinger.*

<!-- Når verktøykjede-innlegget publiseres i blogg/: legg denne linjen tilbake i TL;DR-blokken over (med «>»-prefiks og en tom «>»-linje mellom):
**Les også:** [Jeg dro på JavaZone uten laptop](lessons-learned-javazone-2026.md) – om verktøykjeden som førte notatene.
-->

Med etter hvert ganske mange JavaZone-konferanser bak meg er den fortsatt på mange måter årets høydepunkt: spennende og variert program på sju parallelle spor, topp mat gjennom hele dagen fra matbodene, og hyggelig å treffe igjen kjentfolk og kolleger fra JPro. AweZone på onsdagen leverte også, med et forrykende, timelangt Matoma-show fra klokka 21.

Faglig var det umulig å ikke legge merke til mønsteret: AI gikk igjen i en stor andel av foredragene. Jeg fulgte den tråden med vilje – men det som traff best, var like ofte motvektene.

## AI-tråden

Dagen min på torsdag startet og sluttet i hver sin ende av den: Einar Ingebrigtsens **«Event Sourcing: The Only Sane Way to Run Agentic Systems»** argumenterte for at logger og CRUD-databaser viser *hva* som skjedde, men aldri *hvorfor* – og at man ikke kan stole på et agentisk system uten å vite intensjonen, kausaliteten og hvem som autoriserte endringen. Genuint interessant – og ærlig om hvorfor event sourcing likevel knapt finnes i produksjon.

Grepet hans med å formalisere agenter som teammedlemmer med egen identitet i eventstrømmen er den mest konkrete oppskriften på agent-etterrettelighet jeg har sett – og det slo meg at [Henrik Knibergs SmidigDig-keynote om Abundly](../SmidigDig/2026/talks/0910-crossfunctional-team-humans-agents.md) fra i mai er den andre halvdelen av samme tanke: der er agentene allerede teammedlemmer med navn, egne ansvarsområder og retrospektiver på seg selv, mens menneskene beholder siste godkjenning. På en måte to svar på samme spørsmål – hva skal til for å stole på agenter som handler i systemene våre? Kniberg svarer med organisering, Ingebrigtsen med arkitektur.

I den andre enden av dagen: Ricki Sickengers **«Retro Meets AI»**, underholdende om å bygge retrospill med Claude på tvers av førti år med teknologi. Mellom de to: en ønskeliste som este ut, for AI-foredragene sto i kø – mer om den under.

## Motvektene

Christin Gormans **«The positive value of negative space»** ble foredraget jeg tok med meg hjem. Kode er en forpliktelse, ikke en eiendel, og det vi bevisst *ikke* lager, har egenverdi – med eggdeleren som lakmustest (egget skiller selv) og «Christins lov»: uansett hvor godt du skriver koden, vil nestemann ville skrive den om. At hun landet kritikken midt i AI-bølgen – mer kode enn noensinne, «looks good to me» på digre PR-er – gjorde den bare mer treffsikker. Underholdende levert, som alltid.

Robin Heggelund Hansens **«We're making this a lot harder than it needs to be»** spilte på samme streng: MTP – Minimal Technical Product – tapt enkelhet, HTMX for mindre JavaScript og et nøkternt pro/kontra om microservices. De to foredragene sammen var konferansens egentlige røde tråd for min del: kunsten å la være.

## Innimellom

Mellom ytterpunktene fikk jeg med meg mye som verken var AI-tråd eller motvekt. **Cay Horstmann** ga en ren Java-prat om dataorientert programmering og pattern matching – sealed interfaces, records og exhaustiveness-sjekk, og et klart råd om når DOP passer og når OOP fortsatt vinner. Interessant, smalere enn først antatt. **Hafsa Elkam og Johannes Brodwall** fortalte politiets moderniseringshistorie som en dialog mellom «smidig byråkrat» og «teknologitrollmann»: nytt og gammelt system mot samme data, organisk adopsjon uten opplæring – «brukerne elsker uferdige systemer» – og prinsippet om å bygge den nye vingen før man tar av den gamle. Rundt 96 prosent av oppdragene går nå i de nye operative løsningene.

Onsdagskvelden hørte historiene til. **Anders Norås** fortalte om Ted Nelson og Xanadu – hyperteksten som kunne gitt oss en rikere web med toveislenker, transklusjon og kreditering, men der det eneste Nelson krediteres for, er tilbake-knappen. Og med en tankevekkende hale: Xanadus siteringsmekanismer kunne løst dagens etiske floker rundt generativ KI. Rett etterpå rundet **Eivind Vea** av dagen med røverhistorier fra 80- og 90-tallets hackerkultur – phreaking, wardialing, demoscene og verdens første DDoS med pizza som angrepsvektor. Fantastisk underholdende, og med mye gjenkjennbart for min egen del. Torsdagens pusterom var **Heis.fm LIVE**, en podcast-innspilling fra scenen med Erik Bakstad og Ivar Conradi Østhus som gjester – akkurat den typen avbrekk et konferanseprogram trenger.

## Hvis du bare skal se noen få opptak

Ønskelisten min endte på 34 foredrag. De fem jeg anbefaler først, valgt fordi de spinner videre på trådene over:

1. **Let's create a tiny LLM library together** (Johannes Bechberger) – LLM-klient, tool calling og en liten kodeagent live, uten 100 MB rammeverk.
2. **50 tips på 60 min – bli bedre med AI-agenter** (Kjetil Jørgensen-Dahl) – konsentrert agent-praksis fra Telenor.
3. **Trust, But Verify: Skill-Driven Development** (Totto) – «bygg systemer rundt frykten din»: tester og kunnskapsgrafer som gjør at agentene ikke kan jukse.
4. **My Year with Claude: Building Midimeria** (Øyvind Løkling) – ett år med autonome agenter på hobbyprosjekt, med ærlig regnskap over kognitiv gjeld.
5. **Hvordan logger kan felle en Nav-direktør** (Trond Arve Wasskog og Audun Fauchald Strand) – historien bak direktøravgangen og opprydningen i Nav.

Alle notatene, med lenker til opptak etter hvert som de publiseres, ligger på [JavaZone 2026-siden](../JavaZone/2026/README.md) i [konferansenotat-repoet](https://github.com/georglundesgaard/konferansenotater).

## Hva jeg vil se på neste konferanse

2026-programmet var fullt av «slik kommer vi i gang med agenter». Neste år vil jeg ha fasiten: erfaringsforedragene fra team som har kjørt agentisk utvikling i produksjon i et år, med tall, feilskjær og det ærlige regnskapet – à la Løklings «My Year with Claude», men fra vanlige produktteam. Og jeg tror det viktige sporet blir etterrettelighet snarere enn demo: Ingebrigtsens event sourcing-tråd og Tottos «trust, but verify» peker mot verifisering, evals og revisjonsspor for agenter – hvordan vi *vet* at de gjør rett, ikke bare at demoen gikk bra.

Så håper jeg på flere historier fra offentlig sektor. Politiets modernisering og Nav-fortellingen var blant konferansens beste – samfunnskritiske systemer har en fallhøyde og dilemmaer ingen SaaS-demo kan matche. Og til slutt: vern om det som *ikke* handler om AI. Norås om Ted Nelson og Vea om phreaking hadde null prosent AI og hundre prosent verdi. Et program som puster, trenger de smale, rare og historiske foredragene – det negative rommet, om du vil.
