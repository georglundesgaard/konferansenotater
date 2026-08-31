# A First Look at the Kotlin Ecosystem Plugin for Declarative Gradle

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 10:45 · Marcin Mycek*

Marcin Mycek ga en tidlig demo av Kotlin Ecosystem Plugin – en eksperimentell prototyp bygget oppå Declarative Gradle – som skal gi Kotlin- og KMP-builds en helt ny, deklarativ syntaks. I stedet for imperative Kotlin/Groovy-scripts med håndkonfigurerte source sets, targets og hierarkier, pakker pluginen kompliserte konsepter inn i opinionated «Software Types» (som `kotlinJvmApplication` og en KMP-variant) der utvikleren bare beskriver *hva* som skal bygges, ikke *hvordan*. Mycek viste hvordan den deklarative modellen gjør typiske smertepunkter i KMP – target-oppsett, source set-topologi og plugin-rekkefølge – nesten usynlige, samtidig som IDE-støtte, validering og analyse blir vesentlig bedre fordi build-en er en ren datastruktur. Resonnementet bak endringene er å flytte kompleksitet inn i gjenbrukbare økosystem-plugins slik at build-scriptene blir korte, konsistente og trygge å endre, og å legge grunnlaget for verktøy som IDE-er, migrasjons-recipes og build-init kan forstå direkte. Foredraget var eksplisitt en «first look» på en prototyp under aktiv utvikling, men skisserte tydelig retningen JetBrains og Gradle tar for Kotlin-builds fremover.

**Tags:** `Gradle` · `Build tools` · `Declarative` · `KMP` · `Tooling`

**📹** [A First Look at the Kotlin Ecosystem Plugin for Declarative Gradle | Marcin Mycek](https://www.youtube.com/watch?v=25Ngfn9Bhqc)
