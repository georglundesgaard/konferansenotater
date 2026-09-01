# Automate upgrading to Kotlin 2 with OpenRewrite

*Dag 2, 22. mai 2026 · kl 10:15 · Rooz SF, Jonathan Schneider*

Rooz SF og Jonathan Schneider viste hvordan OpenRewrite nå har fullverdig støtte for Kotlin 2, slik at store kodebaser kan oppgraderes automatisk i stedet for manuelt. Verktøyet bygger opp en Lossless Semantic Tree (LST) – en type- og formatbevarende representasjon av kildekoden – som gjør at oppskriftene (recipes) kan gjøre presise, kompilatornøyaktige endringer uten å ødelegge kommentarer, whitespace eller stil.

Sammensatte oppskrifter håndterer hele migreringsløpet: `UpgradeDependencyVersion` og `ChangeDependency` løfter Kotlin- og bibliotekversjoner i både Groovy- og Kotlin-baserte Gradle-skript, mens API-oppskrifter refaktorerer bruddendringer fra 1.9 til 2.x og retter opp stilinkonsistenser underveis. Gevinsten for store monorepoer er konkret: det som tidligere var uker med manuell PR-vasking blir en deterministisk, repeterbar kjøring som kan skaleres på tvers av hundrevis av moduler og kjøres i CI for å holde koden kontinuerlig oppdatert.

**Tags:** `Tooling` · `Refaktorering` · `OpenRewrite` · `Kotlin 2` · `Migrering`

**📹** [Automate upgrading to Kotlin 2 with OpenRewrite – Rooz SF, Jonathan Schneider](https://www.youtube.com/watch?v=XrPqvtWniuk)
