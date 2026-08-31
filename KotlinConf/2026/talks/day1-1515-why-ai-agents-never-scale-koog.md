# Why Most AI Agents Never Scale? Building Enterprise-Ready AI with Koog

*[← KotlinConf 2026](../README.md) · Dag 1, 21. mai 2026 · kl 15:15 · Vadim Briliantov*

Vadim Briliantov peker på hvorfor de fleste AI-agenter aldri når produksjon: de mangler feiltoleranse når LLM-kall svikter, de mister tilstand under lange kjøringer, kontekstvinduet eksploderer i løpende samtaler, arbeidsflytene er løst typet og «prompt-limt», og de er dårlig koblet til eksisterende enterprise-stack og observability. Koog svarer på dette med innebygde retries, agent-persistens som gjenoppretter hele tilstandsmaskinen (ikke bare chat-historikken), automatisk historikk-komprimering for lange kontekster, og en typet workflow-DSL som gjør agentlogikken forutsigbar. Rammeverket har førsteklasses observability gjennom OpenTelemetry – nå også på tvers av Kotlin Multiplatform – med kobling til verktøy som Langfuse, samt integrasjoner mot Spring Boot/Spring AI og en frakoblet HTTP-transport som spiller pent med Ktor og annen JVM-infrastruktur. Under KotlinConf 2026 annonserte Briliantov Koog 1.0 som stabil utgivelse med ett års API-stabilitetsgaranti, redesignet Java-interop, Anthropic prompt caching og en Mercedes-Benz-case rundt agenter for kjøretøyvedlikehold. Hovedbudskapet for Kotlin-utviklere er at man ikke lenger trenger å bygge egne løsninger for feilhåndtering, persistens og sporing – idiomatisk Kotlin pluss Koog gir de byggeklossene enterprise-agenter faktisk trenger for å skalere.

**Notater fra konferansen:**
- Erfaringsforedrag om AI

**Tags:** `Koog` · `AI-agenter` · `Enterprise` · `Observability` · `LLM`

**📹** [Why Most AI Agents Never Scale? – Vadim Briliantov](https://www.youtube.com/watch?v=9XL0r5lJNDs)
