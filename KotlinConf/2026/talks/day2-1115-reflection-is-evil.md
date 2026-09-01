# Reflection is Evil

*Dag 2, 22. mai 2026 · kl 11:15 · Jeffrey van Gogh · 📋 [i programmet](../program.md#d2-1115) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1061540/)*

Jeffrey van Gogh, «språkgeek» hos Google, argumenterte i denne lyntalen for at refleksjon – evnen kjørende JVM- og .NET-kode har til å inspisere og kalle sine egne komponenter – koster ytelse (mindre inlining fra JIT-en), typesikkerhet, sikkerhet (serialisering) og verktøystøtte, og saboterer kodeslankere som Androids R8: Bouncy Castle må for eksempel friholdes med over 240 ProGuard-regler for ikke å krasje ved kjøring.

Han rangerte dynamisk klasselasting som «rent ondt», var streng også mot testrammeverk og mocking-bibliotek som bryter seg inn i privat kode, men lot debugging (betingede breakpoints via uttrykksevaluatoren) og bakoverkompatible workarounds slippe unna.

Som alternativer viste han fram verktøykassen som allerede finnes: KSP og Java-annotation-processors ved compile-time, tekstbaserte kodegeneratorer, bytekode-omskriving og Kotlin compiler plugins som endrer AST-en og får IDE-integrasjon på kjøpet – samt embedded DSL-er, rene biblioteker eller nye språkegenskaper (som Compose) når problemet virkelig fortjener det. Poenget: refleksjon er ikke ond i seg selv, men blir det når den er den eneste hammeren i verktøykassa.

**Tags:** `Lyntale` · `JVM` · `Compiler plugin` · `Compile-time` · `Språkdesign`

**📹** [Reflection is Evil – Jeffrey van Gogh](https://www.youtube.com/watch?v=bxpmPZOWJOQ)
