# TestBalloon: Kotlin testing is easier (and more fun) than you think

*Dag 2, 22. mai 2026 · kl 15:15 · Oliver Okrongli, Bernd Prünster*

Oliver Okrongli og Bernd Prünster presenterte TestBalloon, et Kotlin-first testrammeverk bygget rundt en liten, konsis API-flate og en utvidbar DSL i ren Kotlin – uten den vanlige annotasjonsmagien. De viste hvordan hierarkiske testtrær med vilkårlig nesting, uttrykksfulle testnavn og dekoratørkjeder gir god struktur, mens fixtures og parameteriserte/datadrevne tester (med tilhørende addons) dekker oppsett, opprydding og gjentagelser på en idiomatisk måte.

En sentral demonstrasjon var førsteklasses støtte for alle Kotlin-mål: ved å kjøre via Wasm/WASI oppnår TestBalloon nestede, samtidige og parallelle tester også på plattformer som mangler native støtte for dette, med coroutine-kontekst som arves nedover treet.

Foredragsholderne viste også hvordan rammeverket gir dyp Gradle-integrasjon og fungerer sømløst sammen med eksisterende assertion-biblioteker, inkludert Kotlin Power-Assert. Til slutt gikk de gjennom JUnit 4- og JUnit 6-interop og en gradvis migreringsvei, slik at eksisterende JVM-prosjekter kan ta i bruk TestBalloon uten å måtte skrive om hele testsuiten på én gang.

**Tags:** `Testing` · `TestBalloon` · `KMP` · `Wasm` · `DSL` · `JUnit`

**📹** [TestBalloon: Kotlin testing is easier (and more fun) than you think – Oliver Okrongli, Bernd Prünster](https://www.youtube.com/watch?v=80ASd_Kt2tw)
