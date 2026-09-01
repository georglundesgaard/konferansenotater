# What Nobody Told Us About Shipping Kotlin to iOS

*Dag 2, 22. mai 2026 · kl 14:00 · Suhyeon (Leah) Kim · 📋 [i programmet](../program.md#d2-1400) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1086104/)*

Suhyeon (Leah) Kim delte erfaringer fra en tomåneders sprint der teamet skulle levere en Kotlin Multiplatform-basert iOS-app under sterk tidspress, og hun brukte tre casestudier for å vise hvor Swift-Kotlin-interop faktisk knirker.

Første case handlet om native state observation: i stedet for å tvinge Kotlin StateFlow inn i SwiftUI direkte, brøt de flyten ned til Combine-vennlige signaler slik at iOS-siden føltes idiomatisk. Andre case var Firebase uten en offisiell KMP-SDK, der de brukte et delegate-mønster slik at Kotlin-koden definerte protokoller mens Swift stod for selve Firebase-kallene og injiserte implementasjonene tilbake. Tredje case var SPM Umbrella Export for binærisolasjon, som lot dem pakke flere Kotlin-frameworks bak én Swift Package uten symbolkollisjoner eller lekkasje av transitive avhengigheter.

Til slutt oppsummerte hun et jukseark over vanlige interop-fallgruver – sealed classes som blir NSObject-hierarkier, suspend-funksjoner som krever completion handlers, default arguments som forsvinner, generics som kollapser til Any, og enum-navn som kolliderer med Swift-nøkkelord – med praktiske omgåelser for hver.

**Tags:** `KMP` · `iOS` · `Compose Multiplatform` · `Swift interop` · `Casestudie` · `Firebase`

**📹** [What Nobody Told Us About Shipping Kotlin to iOS – Suhyeon Kim](https://www.youtube.com/watch?v=nziQi2Mg1OY)
