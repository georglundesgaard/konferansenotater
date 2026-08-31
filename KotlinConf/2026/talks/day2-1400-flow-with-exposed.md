# Flow with Exposed: Life Finds a Way

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 14:00 · Chantal Loncle*

Chantal Loncle bruker en zero-player automaton-simulering som gjennomgående demo for å vise hvordan Exposed takler høy throughput og asynkrone database-operasjoner uten å knele. Simuleringen genererer store mengder tilstandsendringer per tick, og Loncle demonstrerer hvordan man kombinerer Kotlin Flow over Exposed DSL-spørringer for å strømme kontinuerlige state-updates ut til klienten via Coroutines. Underveis viser hun konkrete mønstre for å håndtere backpressure og batch-skriving når Exposed presses på grensen av hva biblioteket kan levere. Etter at simuleringen har generert data, tar hun resultatene inn i Kotlin Notebook og analyserer og visualiserer atferden med DataFrame og Kandy, slik at man ser hvordan automatens «liv» utvikler seg over tid. Til slutt introduserer hun den nye Exposed Gradle-pluginen som forenkler skjema-migrasjoner ved å generere migrasjonsscript direkte fra tabelldefinisjonene i koden.

**Tags:** `Exposed` · `Database` · `Flow` · `Coroutines` · `DataFrame` · `Kandy`

**📹** [Flow with Exposed: Life Finds a Way – Chantal Loncle](https://www.youtube.com/watch?v=Uoe7ClRkbGI)
