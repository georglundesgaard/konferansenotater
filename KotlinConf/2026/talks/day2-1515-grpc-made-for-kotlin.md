# gRPC, Made for Kotlin

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 15:15 · Alexander Sysoev*

Alexander Sysoev viste i denne lyntalen hvordan kotlinx-rpc endelig gjør gRPC til et fullt idiomatisk Kotlin-verktøy, i stedet for at man må lene seg på autogenererte Java-stubber med callbacks og manuell trådhåndtering. Tjenester defineres som vanlige Kotlin-interfaces der de fire gRPC-mønstrene faller rett inn i språket: unary blir en ren `suspend fun`, server-streaming returnerer `Flow<T>`, klient-streaming tar `Flow<T>` som parameter, og bidirectional kombinerer begge – alt bundet sammen av strukturert samtidighet slik at kansellering av en coroutine også river ned den underliggende RPC-en. Demoen viste en Kotlin-klient og en Kotlin-server som snakker sammen over samme grensesnitt, med Flow-baserte streams som håndteres på begge sider uten boilerplate. Under panseret er kotlinx-rpc sin gRPC-modul bygget som en Kotlin Multiplatform-implementasjon med egen protobuf-serialisering, og første dev-utgivelse (0.11.0-grpc) støtter JVM, Android og native mål. Statusen er fortsatt eksperimentell preview, men biblioteket følger Kotlin-utviklingen tett og er klart for Kotlin 2.4, slik at team kan begynne å prøve det ut i backend-prosjekter allerede nå.

**Notater fra konferansen:**
- Fin lyntale om hvordan bruke det nye Kotlin-biblioteket for gRPC

**Tags:** `Lyntale` · `gRPC` · `kotlinx-rpc` · `Backend` · `Coroutines` · `Flow`

**📹** [gRPC, Made for Kotlin – Alexander Sysoev](https://www.youtube.com/watch?v=RqbTeZXgkdQ)
