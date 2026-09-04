# Bootiful Kotlin

*Dag 1, 21. mai 2026 · kl 10:15 · Josh Long · 📋 [i programmet](../program.md#d1-1015) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1126816/)*

Josh Long leverte en klassisk live-kodet gjennomgang der han bygde en Spring Boot 4-applikasjon i Kotlin fra bunnen av og viste hvor tett rammeverket og språket har vokst sammen. Underveis demonstrerte han hvordan Kotlins konsise syntaks, dataklasser og extension-funksjoner spiller sammen med Spring sine DSL-er – inkludert den nye BeanRegistrar-DSL-en – og virtuelle tråder på moderne JVM for å skjære bort seremoniell kode i en typisk backend. Han trakk også fram JSpecify-samarbeidet mellom Spring, JetBrains, Google og flere, som gjør at nullbarhets-annotasjoner i Spring Framework 7 kommer over som ekte nullable-typer i Kotlin.

En stor del av økten dreide seg om Spring AI-økosystemet i 2026: han integrerte en LLM-drevet ChatClient mot Google Gemma kjørt lokalt i Ollama, og ga modellen domenekunnskap via Anthropic-inspirerte skills – markdown-filer pakket som jar-artefakter på Maven Central, som lastes dynamisk bare når spørsmålet er relevant. Mye tid gikk også til passordløs sikkerhet, med engangstoken-innlogging og passkeys/WebAuthn via Spring Security 7 sin nye customizer-mekanisme, pluss observability der LLM-token-forbruket dukker opp i Grafana. Hovedbudskapet var at Kotlin- og Spring-utviklere allerede sitter på en produktiv, idiomatisk plattform for å levere AI-drevne tjenester i produksjon uten å bytte stack. Som alltid et energisk show fra Josh Long – i praksis samme oppskrift som i fjor, men med AI som krydder.

**Tags:** `Spring Boot` · `Live coding` · `AI` · `Backend`

**📹** [Bootiful Kotlin – Josh Long](https://www.youtube.com/watch?v=_UJs3fkPAr8)

*[← 0900 Opening Keynote](day1-0900-opening-keynote.md) · [1115 Opinionated Ktor Services →](day1-1115-opinionated-ktor-services.md)*
