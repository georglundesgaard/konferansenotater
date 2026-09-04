# Why Most AI Agents Never Scale? Building Enterprise-Ready AI with Koog

*Dag 1, 21. mai 2026 · kl 15:15 · Vadim Briliantov · 📋 [i programmet](../program.md#d1-1515) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1086353/)*

Vadim Briliantov peker på hvorfor de fleste AI-agenter aldri når produksjon: de mangler feiltoleranse når LLM-kall svikter, de mister tilstand under lange kjøringer, kontekstvinduet eksploderer i løpende samtaler, arbeidsflytene er løst typet og «prompt-limt», og de er dårlig koblet til eksisterende enterprise-stack og observability. Kostnadsproblemet underbygde han med JetBrains' egne tall – én enkelt kjøring av en kodeagent gjennom SWE-bench koster 500–700 dollar – og en personlig anekdote om en visum-agent som krasjet på kontekstgrensen.

Koog svarer på dette med innebygde retries, agent-persistens som gjenoppretter hele tilstandsmaskinen (ikke bare chat-historikken), automatisk historikk-komprimering for lange kontekster – med strategier som chunking og «fact retrieval», som ifølge Briliantov er unik for Koog og ga 5–8 % forbedring på deres benchmark – og en typet workflow-DSL som gjør agentlogikken forutsigbar. Hver subtask i grafen kan kjøre sin egen modell (i demoen GPT-5 for brukersamtale, Claude Sonnet for verktøykall og en resonneringsmodell for verifisering), mens Koog automatisk re-forklarer tidligere verktøykall for neste modell. Rammeverket har førsteklasses observability gjennom OpenTelemetry med kobling til verktøy som Langfuse, Weights &amp; Biases og Datadog, samt integrasjoner mot Spring Boot/Spring AI. Poengene ble demonstrert ved å bygge en bankassistent live – fra fire linjers naiv agent til typet graf-workflow med chat-minne i Postgres via Spring AI.

Under KotlinConf 2026 annonserte Briliantov Koog 1.0 som stabil utgivelse – nøyaktig ett år etter at Koog ble presentert på KotlinConf 2025, etter et år med persistens, observability, Koog for Java (lansert på JavaOne), Spring-integrasjoner og lokal on-device-modellstøtte for Android – og viste til Mercedes-Benz som produksjonsbruker. Hovedbudskapet for Kotlin-utviklere er at man ikke lenger trenger å bygge egne løsninger for feilhåndtering, persistens og sporing – idiomatisk Kotlin pluss Koog gir de byggeklossene enterprise-agenter faktisk trenger for å skalere.

**Tags:** `Koog` · `AI-agenter` · `Enterprise` · `Observability` · `LLM`

**📹** [Why Most AI Agents Never Scale? – Vadim Briliantov](https://www.youtube.com/watch?v=9XL0r5lJNDs)

*[← 1400 Local Lifetimes for Kotlin](day1-1400-local-lifetimes.md) · [1615 Talking to terminals →](day1-1615-talking-to-terminals.md)*
