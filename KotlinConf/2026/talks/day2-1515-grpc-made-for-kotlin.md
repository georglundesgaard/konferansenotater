# gRPC, Made for Kotlin

*Dag 2, 22. mai 2026 · kl 15:15 · Alexander Sysoev · 📋 [i programmet](../program.md#d2-1515) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1240308/)*

Alexander Sysoev viste i denne lyntalen hvordan kotlinx-rpc endelig gjør gRPC til et fullt idiomatisk Kotlin-verktøy, i stedet for at man må lene seg på autogenererte Java-stubber med callbacks og manuell trådhåndtering. Tjenester defineres som vanlige Kotlin-interfaces der de fire gRPC-mønstrene faller rett inn i språket: unary blir en ren `suspend fun`, server-streaming returnerer `Flow<T>`, klient-streaming tar `Flow<T>` som parameter, og bidirectional kombinerer begge – alt bundet sammen av strukturert samtidighet slik at kansellering av en coroutine også river ned den underliggende RPC-en.

Demoen var en chat-app i Compose Multiplatform der Android- og iOS-klienter snakket med samme server over samme grensesnitt – en server som også kan plugges rett inn i en Ktor-applikasjon på egen port i samme prosess.

Under panseret er kotlinx-rpc sin gRPC-modul en Kotlin Multiplatform-implementasjon med egen protobuf-serialisering, der all kodegenerering skjer i en kompilator-plugin på FIR/IR-nivå – de omfangsrike klassene gRPC Java ellers genererer er helt skjult, og IDE-en slipper å indeksere dem. Selve gRPC-maskineriet delegeres til plattformbibliotekene: gRPC Java på JVM og gRPC C på Kotlin/Native. Protobuf-genereringen er nær 100 % spesifikasjonskompatibel, mens gRPC-funksjonspariteten ennå ikke er komplett – autentisering og interceptors er på plass, tracing og deadlines mangler. Statusen er fortsatt eksperimentell dev-preview, og planen er å gjøre gRPC til hovedfokus for kotlinx-rpc og flytte previewen inn i hovedgrenen, via alpha mot en 1.0-utgivelse. En fin lyntale som viste hvor enkelt det nye biblioteket gjør gRPC-bruk i Kotlin.

**Tags:** `Lyntale` · `gRPC` · `kotlinx-rpc` · `Backend` · `Coroutines` · `Flow`

**📹** [gRPC, Made for Kotlin – Alexander Sysoev](https://www.youtube.com/watch?v=RqbTeZXgkdQ)

*[← 1400 Context parameters and API design](day2-1400-context-parameters-api-design.md) · [1545 KotlinLLM →](day2-1545-kotlinllm-runtime-delegation.md)*
