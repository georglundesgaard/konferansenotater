# KotlinLLM: Leveraging AI for Runtime Logic Delegation in Kotlin

*Dag 2, 22. mai 2026 · kl 15:45 · Stanislav Sandler · 📋 [i programmet](../program.md#d2-1515) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1085233/)*

I denne lyntalen viste Stanislav Sandler frem KotlinLLM, en forskningsprototyp fra JetBrains som lar deg delegere forretningslogikk til en LLM ved runtime bak en typet Kotlin-fasade – via en «smart parser» – inline-funksjonen `asLlm` – der du beskriver hva du vil ha, og AI-en fyller inn logikken som generert Kotlin-kode mot dine data classes og enums. Poenget er at delegeringen er eksplisitt i koden, at resultatet persisteres som vanlig Kotlin-kildekode og at det blir portabelt: når koden først er generert, kjører den uten LLM-kall, uten ekstra latens eller kostnad. Sandler var tydelig på at dette er en mulighetsstudie, ikke et formelt språkforslag.

Parseren «evolverer» ved behov: første gang er `asLlm` bare en stub, og møter den input den ikke håndterer, returneres null – noe som utløser generering av ny logikk ved runtime, mens en ParseResult-wrapper skiller evolusjons-null fra en reell parseverdi. Demoen «Easy Issue Radar» klassifiserte GitHub-issues som nybegynnervennlige ut fra label-navn, med egen runtime-generert parselogikk per repo – uten restart. Typene fungerer som spesifikasjon: en beskrivende data class eller nullable returtype kan erstatte hint-parameteren og fortelle LLM-en hva som skal skje ved feil. Prototypen kjører foreløpig bare på JVM, siden den bygger på JVM hot reload, og sikkerheten håndteres med heuristikker eller LLM-som-dommer som verifiserer at generert funksjon er pur og ikke endrer app-tilstand.

Mønsteret gir mest mening der input er semistrukturert eller reglene endrer seg raskt (parsing, adaptere, klassifisering) – ikke som erstatning for imperativ kode der determinisme og ytelse teller mest. Hovedbudskapet: du kan hente inn AI som en språknær byggekloss i Kotlin uten å ofre type-safety. En god lyntale om LLM for Kotlin – et lekent innblikk i et fortsatt underutforsket område.

**Tags:** `Lyntale` · `KotlinLLM` · `Runtime delegation` · `LLM`

**📹** [KotlinLLM: Leveraging AI for Runtime Logic Delegation – Stanislav Sandler](https://www.youtube.com/watch?v=tmPZajBUsKg)

*[← 1515 gRPC, Made for Kotlin](day2-1515-grpc-made-for-kotlin.md) · [1615 Spec-Driven Development →](day2-1615-spec-driven-development.md)*
