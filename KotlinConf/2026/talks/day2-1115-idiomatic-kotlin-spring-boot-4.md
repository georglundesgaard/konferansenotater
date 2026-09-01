# Idiomatic Kotlin applications with Spring Boot 4

*Dag 2, 22. mai 2026 · kl 11:15 · Sébastien Deleuze*

Sébastien Deleuze viser hvordan Spring Boot 4 gjør backend-utvikling i Kotlin mer idiomatisk enn noen gang, med korte demoer på tvers av bygg, null-safety, serialisering, observability, persistens og AI. JSpecify-annotasjoner er nå rullet ut i hele Spring-porteføljen og oversettes automatisk til Kotlin-nullability takket være K2-kompilatoren, slik at plattformtyper og uventede NPE-er i praksis forsvinner og Spring-API-ene føles native i Kotlin.

Den offisielle Kotlin-tutorialen for Spring Boot er migrert fra JPA til Spring Data JDBC fordi det gir mer idiomatisk kode med uforanderlige `data class`-entiteter og en lettere stack som spiller bedre sammen med språket. For skalerbare API-er anbefaler Deleuze coroutines med automatisk kontekstpropagering for tracing og observability, samt virtual threads som lar deg få høy samtidighet uten å ta på seg den reaktive kompleksiteten.

Spring Boot 4 leverer også en dedikert `spring-boot-starter-kotlinx-serialization-json`, forutsigbar sameksistens mellom Jackson og kotlinx.serialization, og Kotlin 2.2 som ny baseline. Hovedbudskapet er at Kotlin+Spring-stacken nå er så godt integrert at man kan velge mellom suspenderende funksjoner og virtuelle tråder etter behov, og få null-safety på kjøpet uten ekstra arbeid.

**Notater fra konferansen:**
- Interessant å se hvordan Spring-vedlikeholderne implementerer støtte for Kotlin, og hvordan dette gjør idiomatiske Kotlin-applikasjoner enkle å lage

**Tags:** `Spring Boot` · `Backend` · `Null-safety` · `Coroutines` · `Virtual threads` · `JSpecify`

**📹** [Idiomatic Kotlin applications with Spring Boot 4 – Sébastien Deleuze](https://www.youtube.com/watch?v=TxmBk_VhuqY)
