# Eval-Driven Development: The Fine Line Between Agentic Success and Failure

*Dag 2, 22. mai 2026 · kl 13:00 · Urs Peter · 📋 [i programmet](../program.md#d2-1300) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1086726/)*

Urs Peter argumenterer for at Eval-Driven Development (EDD) er den ingeniørdisiplinen som skiller fungerende AI-agenter fra prototyper som havarerer i produksjon, og han flytter dermed evaluering fra en ad hoc-aktivitet til et førsteklasses utviklingsartefakt på linje med tester og CI. Han organiserer arbeidet i sin egen «evalpyramide»: billige deterministiske sjekker i bunn (skjema, JSON, verktøykall), ground truth-sjekker, LLM-as-judge for tone og kvalitet, og mennesket på toppen som vurderer produksjonstraces og kalibrerer dommerne.

På metrikksiden kombinerer han deterministiske mål (latency, kostnad, verktøysuksess, JSON-validitet) med LLM-as-judge-scorer for korrekthet, relevans og tone, og han viser hvordan man oppdager stille degradering i produksjon ved å sample trafikk, kjøre kontinuerlig scoring og varsle om drift i disse metrikkene fremfor bare på harde feil. Peter demonstrerer også hvordan man bruker en LLM til å generere syntetiske testtilfeller og edge cases fra en liten seed, slik at evalueringsdatasettet vokser i takt med agenten. Han viser også multi-turn-evaluering med en brukersimulator som gir personaen humør og mål og lar en dommer vurdere hele samtalen – i demoen avslørte den at agenten foreslo overlappende konferansesesjoner.

Konkret demonstreres alt i en Spring AI-demoapp («talk to KotlinConf») med eval-rammeverket Dokimos – et nytt open source EDD-rammeverk for JVM med integrasjoner for Spring AI, LangChain4j og Koog, som Peter selv har bidratt til med Kotlin-støtte – der evalsuiter kjører som vanlige JUnit-tester i CI, mens produksjonstracing skjer via Langfuse. I produksjon lukkes sløyfen med tommel-ned-tilbakemeldinger og en LLM-basert «feedback-triager» som klassifiserer klager, hvorpå dårlige traces konverteres TDD-aktig til feilende evals i det «gyldne datasettet». Hovedbudskapet er at en agent uten evaluering ikke er ferdig – du eier metrikkene og regresjonsvernet like mye som koden, ellers seiler kvaliteten ukontrollert med hver modell- og promptendring.

**Tags:** `AI-agenter` · `Evaluering` · `Koog` · `Metode` · `Testing`

**📹** [Eval-Driven Development – Urs Peter](https://www.youtube.com/watch?v=L2bZzPXfmyE)

*[← 1115 Idiomatic Kotlin, Spring Boot 4](day2-1115-idiomatic-kotlin-spring-boot-4.md) · [1400 Context parameters and API design →](day2-1400-context-parameters-api-design.md)*
