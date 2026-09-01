# Redefining Machine Learning with Kotlin: A Device-First Approach to AI

*Dag 2, 22. mai 2026 · kl 11:15 · Michal Harakal · 📋 [i programmet](../program.md#d2-1115) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1082547/)*

Michal Harakal presenterte SKaiNET, et Kotlin-basert rammeverk som gjør maskinlæring praktisk på enheten uten å måtte gå veien om Python eller skyløsninger. Kjernen er en typesikker DSL (`nn { }` / `dag { }`) der utviklere definerer nevrale nettverk én gang i idiomatisk Kotlin, og modellen fanges enten som en tape eller en DAG-basert beregningsgraf.

Fra samme definisjon kan man kjøre eagert under utvikling og deretter kompilere den til ulike backends – StableHLO/MLIR via IREE for native mål, C99 for Arduino, og Minerva for sikre mikrokontrollere. Harakal viste hvordan lettvekts-ConvNets og kompakte LLM-er kan kjøres fullstendig offline på mobil og innebygde enheter, med Kotlin Multiplatform som tillater deling av modellen på tvers av Android, JVM, Kotlin/Native, Wasm og JS.

Poenget er at typesikkerhet, ytelse og personvern kan gå hånd i hånd når AI flyttes fra serveren og ned til brukerens egen enhet.

**Tags:** `AI` · `ML` · `KMP` · `On-device` · `SKaiNET` · `Personvern`

**📹** [Redefining Machine Learning with Kotlin – Michal Harakal](https://www.youtube.com/watch?v=uTmCE0SlvSM)

*[← KotlinConf 2026](../README.md)*
