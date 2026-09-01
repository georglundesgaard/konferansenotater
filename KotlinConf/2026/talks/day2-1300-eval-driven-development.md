# Eval-Driven Development: The Fine Line Between Agentic Success and Failure

*Dag 2, 22. mai 2026 · kl 13:00 · Urs Peter*

Urs Peter argumenterer for at Eval-Driven Development (EDD) er den ingeniørdisiplinen som skiller fungerende AI-agenter fra prototyper som havarerer i produksjon, og han flytter dermed evaluering fra en ad hoc-aktivitet til et førsteklasses utviklingsartefakt på linje med tester og CI. Han organiserer testing av agenter i tydelige lag: enhetstester for enkeltverktøy og promptfunksjoner, integrasjonstester for verktøykjeder og LLM-kall, ende-til-ende-tester som kjører hele agentflyten mot realistiske scenarier, og regresjonstester som fanger opp at nye modellversjoner eller promptendringer bryter tidligere adferd.

På metrikksiden kombinerer han deterministiske mål (latency, kostnad, verktøysuksess, JSON-validitet) med LLM-as-judge-scorer for korrekthet, relevans og tone, og han viser hvordan man oppdager stille degradering i produksjon ved å sample trafikk, kjøre kontinuerlig scoring og alarmere på drift i disse metrikkene fremfor bare på harde feil. Peter demonstrerer også hvordan man bruker en LLM til å generere syntetiske testtilfeller og edge cases fra en liten seed, slik at evalueringsdatasettet vokser i takt med agenten.

Konkret vises alt integrert i Koog gjennom JetBrains sitt rammeverk: agent- og verktøydefinisjoner får evaluatorer koblet på, kjøringer instrumenteres via Koogs observability-lag, og evalueringssuiter kjøres i CI som del av byggepipelinen. Hovedbudskapet er at en agent uten evaluering ikke er ferdig – du eier metrikkene og regresjonsvernet like mye som koden, ellers seiler kvaliteten ukontrollert med hver modell- og promptendring.

**Notater fra konferansen:**
- Intro til EDD for å bygge gode AI-agenter og sikre at de blir riktige

**Tags:** `AI-agenter` · `Evaluering` · `Koog` · `Metode` · `Testing`

**📹** [Eval-Driven Development – Urs Peter](https://www.youtube.com/watch?v=L2bZzPXfmyE)
