# How google.com/search builds on Kotlin coroutines for highly scalable, streaming, concurrent servers

*Dag 1, 21. mai 2026 · kl 13:00 · Sam Berlin, Alessio Della Motta · 📋 [i programmet](../program.md#d1-1300) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1085790/)*

Sam Berlin og Alessio Della Motta fra Google Search Infra viser hvordan google.com/search har bygget en tjener-stack på Kotlin coroutines for å drive lavlatens, streaming og massivt samtidige søkeforespørsler i produksjon – hvert eneste Google-søk rutes i dag gjennom en Kotlin-tjener på JVM, valgt for minnesikkerhet i skala og direkte gjenbruk av eksisterende Java-kode. Kjernen i foredraget er Qflow – et internt grafbasert DSL som lar utviklere deklarere asynkrone dataavhengigheter på toppen av vanlig Kotlin-forretningslogikk, slik at planleggeren automatisk kan kjøre uavhengige noder parallelt og streame delresultater videre så snart de er klare. Qflow innfører «varme» strømmer – en hybrid av cold og hot flows som først kjører ved behov, men memoiserer resultatet slik at gjentatt lesing ikke utløser nye RPC-kall – og støtter hot-reload av både Q-filer og JVM-kode, slik at teamet skipper ny kode i produksjon hver time uten å restarte tjenerne.

For å håndtere kompleksiteten instrumenterer teamet coroutine-runtimen med per-node latensmåling og kritisk-vei-analyse, slik at ingeniørene kan se nøyaktig hvilke suspend-punkter som holder svartiden nede i sluttbrukerens tail latency. Samtidig viet de mye tid til fallgruvene i rå structured concurrency – kansellering som fanges ved et uhell og scopes som «forgiftes» – og anbefaler å la Qflow eie scopene fremfor å bygge dem manuelt, selv med massiv fan-out per forespørsel.

Erfaringen fra Google-skala er at «asynkron som standard» bare fungerer når språket, DSL-et og observabiliteten er designet sammen – ellers drukner utviklerne i callback-tenkning eller usynlige flaskehalser. Teamet har til og med bannlyst enkelte Flow-APIer via linter og erstattet dem med tryggere varianter (toList heter awaitCollectToList), fordi tusenvis av utviklere uten Kotlin-bakgrunn skal kunne bidra ukentlig. Lærdommen for backend-utviklere er å behandle coroutines som en plattform man bygger verktøy rundt, ikke bare en språkfunksjon: invester i grafmodell, tracing og strukturert livssyklus før skalaen kommer. Sett live: interessant å se hvordan Google bruker Kotlin-coroutines – foredraget var stappfullt, med lite plass til tilhørerne.

**Tags:** `Coroutines` · `Google` · `Qflow` · `Structured concurrency` · `Skala` · `Casestudie` · `Observability`

**📹** [How google.com/search builds on Kotlin coroutines... – Sam Berlin, Alessio Della Motta](https://www.youtube.com/watch?v=6D1yV5o4CWo)

*[← 1115 Opinionated Ktor Services](day1-1115-opinionated-ktor-services.md) · [1400 Local Lifetimes for Kotlin →](day1-1400-local-lifetimes.md)*
