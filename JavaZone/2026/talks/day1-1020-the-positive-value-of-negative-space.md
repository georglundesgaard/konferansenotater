# The positive value of negative space

*Dag 1, 2. september 2026 · kl 10:20 · Christin Gorman · 📋 [i programmet](../program.md#d1-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/d8028049-c093-44e3-b929-a848351b7834)*

Christin Gorman (nå i eget familiefirma, Piece of Cake) bygger foredraget rundt at negativt rom – det vi bevisst *ikke* lager – har like stor verdi som det vi lager. Hun går løs på bransjens «hopium»: store drømmeprosjekter (NHS, amerikanske og norske helseplattformer) som føles perfekte nettopp fordi de ikke finnes ennå, og lanserer «Christins lov» – uansett hvor godt du skriver koden, vil nestemann ville skrive den om. Motgiften er å jorde drømmene: drøm stort, men bygg smått, og spør først om det i det hele tatt trengs programvare – Excel og post-it-lapper som virker, er en løsning, ikke et problem, for «code is a liability, not an asset».

Verktøykritikken konkretiseres med kjøkkenmetaforer (eggdeleren du ikke trenger – egget skiller selv) og left-pad-kollapsen, før hun viser frem sitt eget motstykke: pieceofcake.no bygget i ren HTML/CSS/JS, deployet med `git push` til en norsk VPS med post-receive-hook og NGINX – «90-tallsteknologi på moderne maskinvare» og den raskeste pipelinen hun har hatt. Spring får gjennomgå i en live-demo av hvor lite rammeverket egentlig gjør: DI-interfaces med én implementasjon, mapper-objekter som burde vært pure functions, og mock-tester som bare verifiserer sine egne mocks. Alternativet er en main-funksjon som instansierer det lille som trenger tilstand, programmatiske ruter med Javalin eller Helidon Níma, og lynraske tester uten kontekst-oppspinning – illustrert med anekdoten om «current date»-mikrotjenesten som distribuerte dagens dato over Kafka.

Mot slutten løfter hun blikket: med AI produseres det mer kode enn noensinne, og med hjernens prediktive natur (fra boken «The Experience Machine») ser vi bare det vi forventer i digre PR-er – «looks good to me». Hun er ikke anti-teknologi, men anti-søppel: bransjen trenger folk som tør å si nei, tettere regulering av aktørene som tjener på volumet, og et ideal om at fravær av ting er vakkert – som nattehimmelen vi ikke lenger ser på grunn av lysforurensning. Underholdende levert – som alltid med Gorman.

**Tags:** `Produktivitet` · `Minimalisme` · `Kritisk blikk` · `AI` · `Tooling` · `Bærekraft`

**📹** [The positive value of negative space – Christin Gorman](https://vimeo.com/1223305711)

*[1300 Java Patterns →](day1-1300-java-patterns-why-how-and-when-not.md)*
