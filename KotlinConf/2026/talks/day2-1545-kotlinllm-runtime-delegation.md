# KotlinLLM: Leveraging AI for Runtime Logic Delegation in Kotlin

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 15:45 · Stanislav Sandler*

I denne lyntalen viste Stanislav Sandler frem KotlinLLM, et forskningsprototyp fra JetBrains som lar deg delegere forretningslogikk til en LLM ved runtime bak en typet Kotlin-fasade – via såkalte Smart macros som `asLlm<F, T>()` der du beskriver hva du vil ha, og AI-en fyller inn kroppen med generert Kotlin-kode mot dine data classes og enums. Poenget er at delegeringen er eksplisitt i koden, at resultatet persisteres som vanlig Kotlin-kildekode og at det blir portabelt: når koden først er generert kjører den uten LLM-kall, uten ekstra latens eller kostnad. Runtime delegation kobles inn i den bredere Kotlin AI-stakken, og Tracy – JetBrains sitt nye AI-observabilitetsbibliotek bygget på OpenTelemetry – sørger for at genereringen kan spores, måles og debugges på lik linje med vanlige tjenestekall, mens caching av genererte macroer og fallback til tidligere versjoner behandles som førsteklasses bekymringer. Mønsteret gir mest mening der input er semistrukturert eller reglene endrer seg raskt (parsing, adaptere, klassifisering, mock-implementasjoner av grensesnitt) – ikke som erstatning for imperativ kode der determinisme og ytelse teller mest. Hovedbudskapet: du kan hente inn AI som en språknær byggekloss i Kotlin uten å ofre type-safety, observabilitet eller reproduserbarhet.

**Notater fra konferansen:**
- God lyntale om LLM for Kotlin

**Tags:** `Lyntale` · `KotlinLLM` · `Tracy` · `Runtime delegation` · `LLM`

**📹** [KotlinLLM: Leveraging AI for Runtime Logic Delegation | Stanislav Sandler](https://www.youtube.com/watch?v=tmPZajBUsKg)
