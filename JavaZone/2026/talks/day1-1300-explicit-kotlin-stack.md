# No More Magic: Mastering the Explicit Kotlin Stack with Ktor, Exposed and Koin

*Dag 1, 2. september 2026 · kl 13:00 · Geoffrey Rekier · 📋 [i programmet](../program.md#d1-1300) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/4443a9a9-e4c6-4954-ab59-cc0d528d47f9)*

Rekier argumenterte for en eksplisitt Kotlin-stack – Ktor, Koin og Exposed – som alternativ til Spring Boots «magi». Han illustrerte problemet med en produksjonshistorie der en @Transactional-annotasjon aldri rullet tilbake fordi kallet skjedde internt i samme klasse og dermed aldri gikk gjennom Spring-proxyen: konvensjon-over-konfigurasjon gir rask start, men også bønnekonflikter, proxytunge stack traces og feil man ikke selv har skrevet koden til å forstå. Med den eksplisitte tilnærmingen må alt skrives i koden, og gevinsten er kode som kan leses topp-til-bunn, Ctrl-klikk-navigasjon overalt, kompileringstidsfeil i stedet for stille runtime-feil, og langt raskere oppstart uten refleksjon og klasseskanning.

Han gikk gjennom de tre delene: Ktor som asynkront webrammeverk på coroutines med pluggbar arkitektur og Kotlin-DSL for ruter, Koin for avhengighetsinjeksjon med rene Kotlin-funksjoner i moduler (med et ærlig forbehold om at `get`-inferens kan bli uoversiktlig med mange beans), og Exposed som typet SQL-DSL der kompilatoren fanger opp at spørringer bruker et omdøpt kolonnenavn – i motsetning til Spring Data JPA som feiler stille. I live-demoen bygde han fra start.ktor.io en app med JSON-plugin, ruter, Koin-modul og Exposed-basert brukerlagring, med oppstartstid på rundt et halvt sekund.

Konklusjonen var balansert: stacken passer for team som kan Kotlin godt og trenger rask oppstart, full kontroll og effektiv concurrency, men kostnaden er mer boilerplate, et langt mindre økosystem enn Spring og flere beslutninger man selv må eie – mange prosjekter med tunge integrasjonsbehov er fortsatt best tjent med Spring Boot. I spørsmålsrunden plasserte han Quarkus «midt mellom» Spring og Ktor på magi-skalaen.

**Tags:** `Ktor` · `Exposed` · `Koin` · `Backend` · `Arkitektur` · `Live coding`

**📹** [No More Magic – Geoffrey Rekier](https://vimeo.com/1223398145)

*[← JavaZone 2026](../README.md)*
