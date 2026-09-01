# How Kotlin Powers Functional Design: MCP Edition

*Dag 2, 22. mai 2026 · kl 15:15 · David Denton · 📋 [i programmet](../program.md#d2-1515) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1078053/)*

David Denton fra http4k viste hvordan Kotlin og funksjonell design gir en langt enklere vei til MCP-servere enn de offisielle SDK-ene, som han kritiserer for tung bruk av refleksjon, tett kobling mellom protokoll og transport (spesielt stdio som sammenfletter klient- og server-runtime) og feil som først dukker opp ved kjøretid.

I stedet bygger http4k videre på sine eksisterende funksjonelle prinsipper: klar separasjon mellom protokoll og transport, kapabiliteter modellert som rene funksjoner (for eksempel `typealias ToolHandler = (ToolRequest) -> ToolResponse`), og full in-memory-testing uten porter eller nettverk. Ved å gjenbruke http4k sine byggeklosser for OAuth, Lenses og JSON-RPC får man kompileringstidssikkerhet på tvers av verktøy, ressurser og prompts, og MCP blir bare enda et sett med HTTP-håndterere.

Denton demonstrerte dette med en spec-kompatibel MCP-server på cirka 50 linjer Kotlin, samt en Wiretap-plugin som gir HTTP-trafikk, OpenTelemetry-spor og sekvensdiagrammer i JUnit-rapporter. Poenget er at Kotlins extension functions og type aliases lar biblioteket eksponere et idiomatisk, funksjonelt API der MCP-domenet uttrykkes direkte som funksjonstyper istedenfor annoterte klasser og magisk oppstart.

**Tags:** `MCP` · `http4k` · `Funksjonell` · `Backend` · `API-design` · `Extension functions`

**📹** [How Kotlin Powers Functional Design: MCP Edition – David Denton](https://www.youtube.com/watch?v=Xmkl7Y3lwUk)

*[← KotlinConf 2026](../README.md)*
