# Kotlin/Wasm: Finally, the missing piece for a full stack Kotlin webapp!

*[← KotlinConf 2026](../README.md) · Dag 1, 21. mai 2026 · kl 11:15 · Dan Kim*

Dan Kim viser i praksis hvordan Kotlin/Wasm endelig lar deg bygge en komplett full-stack webapp i ett og samme språk, ved å demonstrere en todo-applikasjon på rundt 486 linjer der frontend, API, database og delte modeller alle er skrevet i Kotlin. Stacken består av Compose Multiplatform for UI-et (kompilert til Wasm og rendret direkte til canvas via Skia, uten omveien om DOM), Ktor som coroutine-native HTTP-server der hver handler er en suspend-funksjon, Exposed som JetBrains sitt SQL-bibliotek uten annotasjoner eller kodegenerering, og Coroutines som en gjennomgående asynkron modell på tvers av lagene.

Wasm er den «manglende brikken» fordi det gir Kotlin en førsteklasses frontend-runtime i nettleserens sandkasse med tilnærmet native ytelse og pikselperfekt UI, slik at man slipper Kotlin/JS-friksjonen mot JavaScript-økosystemet og kan dele typer og domenemodell direkte mellom klient og server. Utvikleropplevelsen i dag er overraskende ren – lite boilerplate, eksplisitt kode og en produktiv indre løkke – men Kim er tydelig på at Kotlin/Wasm fortsatt er i beta, så bundle-størrelse, nettleserstøtte og modenhet er ting man må gå inn i med åpne øyne.

**Tags:** `Kotlin/Wasm` · `Full-stack` · `Compose` · `Ktor` · `Exposed`

**📹** [Kotlin/Wasm: Finally, the missing piece – Dan Kim](https://www.youtube.com/watch?v=JThr4fn9OOw)
