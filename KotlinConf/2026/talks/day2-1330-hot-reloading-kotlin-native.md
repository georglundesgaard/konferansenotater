# Hot-Reloading Kotlin/Native

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 13:30 · Gabriele Pappalardo*

Gabriele Pappalardo (JetBrains) fortalte om den eksperimentelle reisen med å få Compose Hot-Reload til å fungere på iOS-simulator uten en JVM, noe som lenge har blitt ansett som umulig på Apples Darwin-plattformer. I stedet for å bygge en egen Kotlin-virtuell maskin utnyttet teamet LLVM ORC v2 for å laste og linke ny kode dynamisk i den kjørende native-prosessen. Han gikk under panseret på nødvendige kompilator-endringer, spesielt split compilation, som skiller ut kompilerte enheter slik at de kan byttes ut individuelt uten å bygge hele appen på nytt. En ny hot-reload runtime-modul håndterer selve utskiftningen, og han viste hvordan tilstand bevares på tvers av endringer i klasseoppsett, funksjonsoppdateringer og re-linking av symboler. Foredraget ga et konkret innblikk i lavnivå-runtime-manipulasjon på Kotlin/Native og pekte fram mot en langt raskere utviklingsopplevelse for KMP-apper på iOS.

**Tags:** `Kotlin/Native` · `iOS` · `Compose` · `Hot reload` · `LLVM` · `Compiler`

**📹** [Hot-Reloading Kotlin/Native – Gabriele Pappalardo](https://www.youtube.com/watch?v=hXDw2cOxnpo)
