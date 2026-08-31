# KotlinConf 2026

**München, 21.–22. mai 2026.** JetBrains' årlige Kotlin-konferanse. To dager, seks parallelle spor, ca. 74 foredrag. De fleste videoene ble publisert på [Kotlin sin offisielle YouTube-kanal](https://www.youtube.com/@Kotlin) i juli–august 2026 og er også lenket fra [kotlinconf.com/talks/](https://kotlinconf.com/talks/) – sju sesjoner mangler fortsatt individuelle opptak (markert i talk-filene); jeg lenker dem inn etter hvert.

Én fil per foredrag under [`talks/`](talks/). Klikk deg inn på titlene under.

---

## Anbefalt: Topp 5 fra ønskelisten

Hvis du bare skal se noen få opptak, er dette mine anbefalinger fra foredragene jeg selv gikk glipp av — valgt fordi de spinner videre på tråder jeg gikk mye på (AI-agenter, Ktor/backend, språkdesign):

1. **[Full-Stack Kotlin AI: Powering Compose Multiplatform apps with Koog & MCP](talks/day2-1400-full-stack-kotlin-ai-koog-mcp.md)** — John O'Reilly. Praktisk demo av Koog + Kotlin MCP SDK i en Compose Multiplatform-app, med hopp mellom sky-LLM og on-device. Direkte oppfølging til Briliantovs Koog-foredrag.
2. **[How I Learned to Stop Worrying and Love Value Semantics (in Kotlin)](talks/day2-1115-value-semantics.md)** — Marat Akhin. Dybden bak multi-field value classes (eksperimentelt i 2.5) med benchmarks. Passer bra ved siden av *Local Lifetimes* og *Context parameters*.
3. **[How Kotlin Powers Functional Design: MCP Edition](talks/day2-1515-functional-design-mcp.md)** — David Denton (http4k). Skarp kritikk av offisielle MCP SDK-er + en spec-kompatibel MCP-server på ~50 linjer med http4k. Bra motstemme til hovedstrømmen.
4. **[Automate upgrading to Kotlin 2 with OpenRewrite](talks/day2-1015-openrewrite-kotlin-2-upgrade.md)** — Rooz SF, Jonathan Schneider. Umiddelbart nyttig for oppgraderingsjobber: deterministiske recipes over Lossless Semantic Trees.
5. **[The Backend Immune System](talks/day2-1430-backend-immune-system.md)** — Meike Felicia Hammer. Rike feiltyper + Ktor observability + små deterministiske lokale «immunagenter» innenfor request-grensen. Fint komplement til Vergauwens Ktor-foredrag.

---

## Foredrag jeg gikk på

### Dag 1 — 21. mai 2026 ([offisielt program](https://kotlinconf.com/schedule/?day=2026-05-21))

- **[0900 Opening Keynote](talks/day1-0900-opening-keynote.md)** — JetBrains, Google, Anthropic
- **[1015 Bootiful Kotlin](talks/day1-1015-bootiful-kotlin.md)** — Josh Long
- **[1115 Opinionated Ktor Services](talks/day1-1115-opinionated-ktor-services.md)** — Simon Vergauwen
- **[1300 How google.com/search builds on Kotlin coroutines](talks/day1-1300-google-search-coroutines.md)** — Sam Berlin, Alessio Della Motta
- **[1400 Local Lifetimes for Kotlin](talks/day1-1400-local-lifetimes.md)** — Ross Tate
- **[1515 Why Most AI Agents Never Scale? Building Enterprise-Ready AI with Koog](talks/day1-1515-why-ai-agents-never-scale-koog.md)** — Vadim Briliantov
- **[1615 Talking to terminals (and how they talk back)](talks/day1-1615-talking-to-terminals.md)** — Jake Wharton
- **[1715 Robocoders: The [K]agematch](talks/day1-1715-robocoders-kagematch.md)** — Viktor Gamov, Baruch Sadogursky

### Dag 2 — 22. mai 2026 ([offisielt program](https://kotlinconf.com/schedule/?day=2026-05-22))

- **[0900 We were meant to be](talks/day2-0900-we-were-meant-to-be.md)** *(Day 2 Keynote)* — Lena Reinhard
- **[1015 Dissecting Kotlin: 2026](talks/day2-1015-dissecting-kotlin-2026.md)** — Huyen Tue Dao
- **[1115 Idiomatic Kotlin applications with Spring Boot 4](talks/day2-1115-idiomatic-kotlin-spring-boot-4.md)** — Sébastien Deleuze
- **[1300 Eval-Driven Development](talks/day2-1300-eval-driven-development.md)** — Urs Peter
- **[1400 Context parameters and API design](talks/day2-1400-context-parameters-api-design.md)** — Alejandro Serrano Mena
- **[1515 gRPC, Made for Kotlin](talks/day2-1515-grpc-made-for-kotlin.md)** — Alexander Sysoev
- **[1545 KotlinLLM: Leveraging AI for Runtime Logic Delegation](talks/day2-1545-kotlinllm-runtime-delegation.md)** — Stanislav Sandler
- **[1615 Spec-Driven Development with AI Agents](talks/day2-1615-spec-driven-development.md)** — Anton Arhipov

---

## Foredrag jeg vil se opptak av

Foredrag jeg gikk glipp av (parallelle spor / kollisjoner), sortert etter tid.

### Dag 1 — 21. mai 2026

- **[1015 A tale of the Gradle DSLs](talks/day1-1015-gradle-dsls-tale.md)** — Paul Merlin
- **[1015 Tiny Models, Big Impact: On-Device AI for Real Apps](talks/day1-1015-tiny-models-on-device-ai.md)** — Hammad Akram
- **[1045 Run, Kotlin, Run!](talks/day1-1045-run-kotlin-run.md)** — Marc Reichelt
- **[1115 Kotlin/Wasm: Finally, the missing piece for a full stack Kotlin webapp!](talks/day1-1115-kotlin-wasm-full-stack.md)** — Dan Kim
- **[1300 Real-World Data Science With Kotlin Notebook](talks/day1-1300-real-world-data-science-notebook.md)** — Adele Carpenter
- **[1330 SwiftPM support for Kotlin Multiplatform](talks/day1-1330-swiftpm-support-kmp.md)** — Timofey Solonin
- **[1400 Codex for Kotlin Engineers](talks/day1-1400-codex-for-kotlin.md)** — Benedict Kerres
- **[1430 Building AI-Powered Web Apps in Kotlin/Wasm](talks/day1-1430-ai-powered-web-apps-wasm.md)** — Zalim Bashorov
- **[1515 Compose beyond UI: Display and Print!](talks/day1-1515-compose-beyond-ui.md)** — Salomon Brys
- **[1515 Expedited Shipping: Accelerating iOS Development with KMP at Amazon](talks/day1-1515-expedited-shipping-kmp-amazon.md)** — Jessalyn Wang
- **[1515 The State of Amper](talks/day1-1515-state-of-amper.md)** — Joffrey Bion
- **[1615 Increasing quality of AI generated Kotlin code](talks/day1-1615-ai-generated-code-quality.md)** — Sergei Rybalkin (Meta)
- **[1615 Swift Export: Where We Stand](talks/day1-1615-swift-export-status.md)** — Pamela Hill-Galloway
- **[1645 Can Kotlin Swift Interop Ever Be Perfect?](talks/day1-1645-kotlin-swift-interop-perfect.md)** — Gleb Lukianets
- **[1715 The Lord of Collection Functions](talks/day1-1715-lord-of-collection-functions.md)** — Ben Kadel

### Dag 2 — 22. mai 2026

- **[1015 Advanced Kotlin Native Integration](talks/day2-1015-advanced-kotlin-native-integration.md)** — Tadeas Kriz (Touchlab)
- **[1015 Automate upgrading to Kotlin 2 with OpenRewrite](talks/day2-1015-openrewrite-kotlin-2-upgrade.md)** — Rooz SF, Jonathan Schneider
- **[1015 10 Gradle Best Practices Every Kotlin Developer Should Know](talks/day2-1015-gradle-best-practices.md)** — Stefan Wolf
- **[1045 A First Look at the Kotlin Ecosystem Plugin for Declarative Gradle](talks/day2-1045-kotlin-ecosystem-plugin-declarative-gradle.md)** — Marcin Mycek
- **[1115 How I Learned to Stop Worrying and Love Value Semantics](talks/day2-1115-value-semantics.md)** — Marat Akhin
- **[1115 Redefining Machine Learning with Kotlin](talks/day2-1115-redefining-ml-skainet.md)** — Michal Harakal
- **[1115 Reflection is Evil](talks/day2-1115-reflection-is-evil.md)** — Jeffrey van Gogh
- **[1330 Hot-Reloading Kotlin/Native](talks/day2-1330-hot-reloading-kotlin-native.md)** — Gabriele Pappalardo
- **[1400 Flow with Exposed: Life Finds a Way](talks/day2-1400-flow-with-exposed.md)** — Chantal Loncle
- **[1400 Full-Stack Kotlin AI: Powering Compose Multiplatform apps with Koog & MCP](talks/day2-1400-full-stack-kotlin-ai-koog-mcp.md)** — John O'Reilly
- **[1400 What Nobody Told Us About Shipping Kotlin to iOS](talks/day2-1400-shipping-kotlin-to-ios.md)** — Suhyeon (Leah) Kim
- **[1430 The Backend Immune System](talks/day2-1430-backend-immune-system.md)** — Meike Felicia Hammer
- **[1515 How Kotlin Powers Functional Design: MCP Edition](talks/day2-1515-functional-design-mcp.md)** — David Denton
- **[1515 TestBalloon: Kotlin testing is easier (and more fun) than you think](talks/day2-1515-testballoon.md)** — Oliver Okrongli, Bernd Prünster
- **[1615 Koin + Kotlin Compiler = ♥️](talks/day2-1615-koin-kotlin-compiler.md)** — Arnaud Giuliani
- **[1645 Powering Up Your Assertions](talks/day2-1645-powering-up-assertions.md)** — Brian Norman
- **[1715 Golden Kodee Awards](talks/day2-1715-golden-kodee-awards.md)**

---

## Livestream / hovedsal

- **Dag 1:** [Keynote + hovedsal](https://www.youtube.com/watch?v=MmwBJbzWbV0)
- **Dag 2:** [Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I) — inneholder Lena Reinhards keynote og Golden Kodee Awards

---

## Kilder

- [KotlinConf 2026 – offisiell side](https://kotlinconf.com/)
- [KotlinConf 2026 – oversikt over alle foredrag med video-innebygging](https://kotlinconf.com/talks/)
- [Kotlin sin offisielle YouTube-kanal](https://www.youtube.com/@Kotlin) – hovedkilde for videoene
- [KotlinConf'26 Keynote Highlights](https://blog.jetbrains.com/kotlin/2026/05/kotlinconf26-keynote-highlights/)
- [KotlinConf'26 Speakers: In Conversation with Josh Long](https://blog.jetbrains.com/kotlin/2026/03/kotlinconf-26-speakers-in-conversation-with-josh-long/)
- [KotlinConf'26 Speakers: In Conversation With Lena Reinhard](https://blog.jetbrains.com/kotlin/2026/04/kotlinconf-26-speakers-in-conversation-with-lena-reinhard/)
- [Koog på GitHub](https://github.com/JetBrains/koog)
- [Next level Kotlin support in Spring Boot 4](https://spring.io/blog/2025/12/18/next-level-kotlin-support-in-spring-boot-4/)
- [KotlinConf 2026: Talks to Help You Navigate the Schedule](https://blog.jetbrains.com/kotlin/2026/03/kotlinconf-2026-talks-schedule/)
- [Eval-driven development: Build and evaluate reliable AI agents](https://developers.redhat.com/articles/2026/03/23/eval-driven-development-build-evaluate-ai-agents)
- [Context parameters – Kotlin Documentation](https://kotlinlang.org/docs/context-parameters.html)
- [Update on Context Parameters](https://blog.jetbrains.com/kotlin/2025/04/update-on-context-parameters/)
- [Introducing Tracy: The AI Observability Library for Kotlin](https://blog.jetbrains.com/kotlin/2026/03/introducing-tracy-the-ai-observability-library-for-kotlin/)
- [Golden Kodee Community Awards](https://kotlinconf.com/awards/)
- [Kotlin DSLs in 2026: Patterns That Stood the Test of Time](https://jonnyzzz.com/blog/2026/01/19/kotlin-dsl-2026/)
- [Kotlin DSL Is Now the Default for New Gradle Builds](https://blog.gradle.org/kotlin-dsl-is-now-the-default-for-new-gradle-builds)
- [SKaiNET – Multiplatform On Device Deep Learning](https://skainet.sk/)
- [Adding Swift packages as dependencies to KMP modules | Kotlin docs](https://kotlinlang.org/docs/multiplatform/multiplatform-spm-import.html)
- [Interoperability with Swift using Swift export | Kotlin Documentation](https://kotlinlang.org/docs/native-swift-export.html)
- [KEEP-485: Local Lifetimes](https://github.com/Kotlin/KEEP/blob/main/proposals/lifetimes.md)
