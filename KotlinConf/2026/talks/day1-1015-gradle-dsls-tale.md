# A tale of the Gradle DSLs

*Dag 1, 21. mai 2026 · kl 10:15 · Paul Merlin · 📋 [i programmet](../program.md#d1-1015) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1085720/)*

Paul Merlin tar oss gjennom historikken til Gradle sine build-språk, fra den dynamiske Groovy-DSL-en som ga stor fleksibilitet, men svakt IDE-vern, via den statisk typede Kotlin DSL-en som ble innført for å styrke vedlikeholdbarhet, brukeropplevelse og navigering, og videre mot et rent deklarativt konfigurasjonsspråk inspirert av Kotlin. Han viser hvilke mønstre som har vist seg holdbare på tvers av generasjonene, særlig tanken om et deklarativt kjernespråk med tydelige utvidelsespunkter, og forklarer hvorfor Kotlin DSL nå er standardvalget: den kombinerer lesbarhet og autofullføring med tilstrekkelig kraft til plugin-utvikling.

Sentralt i foredraget står skillet mellom software definition og build logic, og hvordan denne oppdelingen tjener både applikasjonsutviklere, build-ingeniører og plugin-forfattere som bruker disse verktøyene daglig. Konkret råder Merlin til å holde build-skriptene tynne og deklarative, flytte imperativ logikk ut i plugins under `buildSrc` eller composite builds, og strukturere prosjektene slik at man allerede i dag drar full nytte av Kotlin DSL samtidig som man er forberedt på overgangen til det kommende deklarative språket.

**Tags:** `Gradle` · `Kotlin DSL` · `Build tools` · `Historikk`

**📹** [A tale of the Gradle DSLs – Paul Merlin](https://www.youtube.com/watch?v=k8T9IOnXPao)

*[← KotlinConf 2026](../README.md)*
