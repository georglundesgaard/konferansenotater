# Kontinuerlige leveranser med parprogrammering, læring og AI

*27. mai 2026 · kl 14:35 · Asgaut Mjølne Söderbom (SpareBank1) · 📋 [i programmet](../program.md)*

Söderbom fortalte hvordan team PM Konto i SpareBank 1 – som forvalter kontodomenet med rundt 1,2 millioner brukere og over 100 millioner API-kall daglig – prodsetter flere ganger i timen ved å jobbe sammen på absolutt alt: parprogrammering og mobbing med bytte hvert sjuende minutt, testdrevet utvikling, små inkrementer bak feature toggles og fire minutters vei til prod. Teamet har systematisk kuttet waste – ingen pull requests eller Jira siden 2022, ingen standups, egne testere eller ende-til-ende-testing – og klarer seg med ett 30-minutters ukesmøte som kombinerer retro og planlegging.

I januar bestemte teamet seg for å prøve «Claude first» frem mot konferansen, og delte fem erfaringer. Claude ga økt autonomi (skripting, frontend, dashboards og Grafana-analyse ved produksjonsfeil uten å måtte spørre andre team) og er svært god på analyse på tvers av apper og på kjedelige hjelpeoppgaver som nynorsk-oversettelse. Men ren kodegenerering svekket den kritiske tenkningen – en «apply, apply, apply»-kultur førte blant annet til at et umaskert token slapp ut i produksjon, noe som ikke ville skjedd med teamets vanlige arbeidsmåte. Teamets vellykkede korttidshospitering, der gjester fra andre team får kode i produksjon før lunsj første dag, fungerte også dårligere med Claude i førersetet på grunn av ventetid og svakere domenelæring.

Konklusjonen etter retro er at teamet nå igjen skriver kode og tester manuelt i domenelaget, der forretningslogikken skal ligge og være forvaltbar, mens Claude tar rammeverksdetaljer og kjedelige oppgaver – en «superkonsulent i hjørnet» som ikke husker noe, men kan spørres om alt. Hovedbudskapet er at fart ikke er målet i seg selv: kode i forvaltbar tilstand, rask feedback på alle nivåer og det å jobbe sammen er like relevant som før, også med AI.

**Notater fra konferansen:**
- Erfaringsforedrag fra Team PM Konto

**Tags:** `Casestudie` · `Parprogrammering` · `Continuous delivery` · `Læring` · `SpareBank1` · `AI` · `Testing`

**📹** [Kontinuerlige leveranser med parprogrammering, læring og AI – Asgaut Mjølne Söderbom](https://vimeo.com/1196401476)

*[← 1335 All aboard the AI train!](1335-ai-train-hvor-skal-vi.md)*
