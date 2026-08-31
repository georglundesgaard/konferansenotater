# Advanced Kotlin Native Integration

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 10:15 · Tadeas Kriz (Touchlab)*

Tadeas Kriz fra Touchlab tar for seg en av de mest oversette begrensningene ved Kotlin Multiplatform: et prosjekt kan i praksis bare inneholde ett Kotlin/Native-binærprodukt om gangen. Foredraget viser hva som skjer hvis man likevel bunter inn flere KMP-binærprodukter i samme applikasjon – blant annet symbolkonflikter, oppblåst størrelse og duplisert runtime som er vanskelig å feilsøke.

Kriz går gjennom teknikker for å dele opp kompileringen i mindre biter, slik at hvert team kan jobbe uavhengig uten å bryte enkeltbinær-regelen. Han diskuterer også løsninger tilpasset større organisasjoner med komplekse repostrukturer, der en felles «paraply»-modul samler den delte koden fra flere team og leverer det endelige binærproduktet ut mot iOS-siden.

Passer for team som allerede bruker KMP i produksjon og møter skaleringssmerter når kodebasen og antallet konsumenter vokser.

**Tags:** `KMP` · `Kotlin/Native` · `Build tools` · `Avansert` · `Touchlab`

**📹** [Advanced Kotlin Native Integration – Tadeas Kriz](https://www.youtube.com/watch?v=Qk2aClaCZgY)
