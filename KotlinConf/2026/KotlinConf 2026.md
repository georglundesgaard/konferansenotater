# KotlinConf 2026

> **Om videoene:** Videoene fra alle sesjonene ble publisert i juli–august 2026 på JetBrains sin offisielle [Kotlin-YouTube-kanal](https://www.youtube.com/@Kotlin), og er også lenket fra hver enkelt talk på [kotlinconf.com/talks/](https://kotlinconf.com/talks/). Hvert foredrag under har direktelenke i **📹**-linjen. Noen få sesjoner (som Robocoders, dag 2-keynoten og Spec-Driven Development) har foreløpig bare Day 2-livestreamen tilgjengelig – jeg oppdaterer disse så snart individuelle videoer dukker opp.

---

## May 21

**📹 Live-stream / opptak fra hovedsal:** [KotlinConf'26 – Day 1 Keynote og hovedsal](https://www.youtube.com/watch?v=MmwBJbzWbV0).

### 0900 Opening Keynote — JetBrains, Google, Anthropic

Åpningskeynoten samlet ti talere fra JetBrains, Google og Anthropic for å tegne opp Kotlins retning på tvers av språk, verktøy, AI og multiplattform, med Kotlin 2.4 som rød tråd der context parameters, explicit backing fields og multi-field value classes ble stabilisert, samtidig som standardbiblioteket nå får en 18-måneders sikkerhetsstøttepolicy. Sentralt sto lanseringen av Kotlin Toolchain, et samlet CLI-inngangspunkt bygget rundt Amper som dekker prosjektopprettelse, bygg, testing, formatering og agentintegrasjon, sammen med en ny Kotlin Language Server i alpha, offisiell VS Code-utvidelse, ktfmt-standardisering og førsteklasses Bazel-støtte. På backend-siden ble Exposed 1.0 med vektortyper for AI-søk, kotlinx-rpc med gRPC og Ktor–Koog-integrasjon annonsert, mens Koog 1.0 gikk stabil som Kotlins agentrammeverk med typesikre workflow-DSL-er og en Mercedes-Benz-casestudie for kjøretøysvedlikehold. AI-fortellingen ble utvidet med det åpne Agent Client Protocol, Junie med egen Android-støtte og CLI, JetBrains Air som orkestrerer flere parallelle agenter i worktrees eller containere, og et tett Anthropic-partnerskap der Claude nå kjører nativt i IntelliJ og Android Studio og oppnår 86,4 % løsningsrate på Kotlin SWE-Bench. Google fremhevet at 92 % av profesjonelle Android-utviklere bruker Kotlin, og at R8-optimaliseringer gir opptil 50 % Compose-ytelsesgevinst, mens KMP-fortellingen løftet Swift Export til alpha, SPM-import, ny standard prosjektstruktur og at KMP-pluginet nå fungerer på alle operativsystemer. Compose Multiplatform ble erklært stabilt for mobil og desktop med Web i beta, Navigation 3 som stabilt bibliotek og nye iOS-interop-APIer mot Liquid Glass, og samlet peker keynoten mot et Kotlin som skal være det naturlige valget for agentdrevet, plattformuavhengig utvikling.

**Tags:** `Keynote` · `Kotlin 2.4` · `AI-agenter` · `KMP` · `Compose` · `Tooling` · `Koog` · `ACP` · `Kotlin Toolchain`

**📹** [Keynote | KotlinConf '26](https://www.youtube.com/watch?v=MmwBJbzWbV0)

---

### 1015 Bootiful Kotlin — Josh Long

Josh Long leverte en klassisk live-kodet gjennomgang der han bygde en Spring Boot 4-applikasjon i Kotlin fra bunnen av og viste hvor tett rammeverket og språket har vokst sammen. Underveis demonstrerte han hvordan Kotlins konsise syntaks, data-klasser, extension-funksjoner og coroutines spiller sammen med Spring sine DSL-er, virtuelle tråder på moderne JVM og deklarative HTTP-klienter for å skjære bort seremoniell kode i en typisk backend. En stor del av økten dreide seg om Spring AI-økosystemet i 2026: han integrerte en LLM-drevet ChatClient, la på verktøybruk og RAG mot en vektordatabase, og eksponerte tjenester som et MCP-endepunkt slik at agenter kunne kalle dem. Han bandt det hele sammen ved å bygge en autonom agent som orkestrerte forretningslogikk gjennom Spring-bønner, og understreket at Spring AI gjør det trivielt å knytte modeller til eksisterende infrastruktur som sikkerhet, observability og transaksjoner. Hovedbudskapet var at Kotlin- og Spring-utviklere allerede sitter på en produktiv, idiomatisk plattform for å levere AI-agenter i produksjon uten å bytte stack.

**Notater fra konferansen:**
- Energisk foredrag med en svært energisk foredragsholder
- Tilsvarende foredrag som i fjor, denne gangen med AI som krydder

**Tags:** `Spring Boot` · `Live coding` · `AI-agenter` · `MCP` · `Backend`

**📹** [Bootiful Kotlin | Josh Long](https://www.youtube.com/watch?v=_UJs3fkPAr8)

---

### 1115 Opinionated Ktor Services — Simon Vergauwen

Simon Vergauwen tar utgangspunkt i at Ktor bevisst er et lite meningssterkt rammeverk – kjernen er coroutines, et plugin-system og modulfunksjoner – og bruker økten til å legge sine egne meninger oppå denne fleksible grunnmuren. Han argumenterer for å strukturere en Ktor-tjeneste rundt små, utskiftbare `Application`-moduler som er extension-funksjoner, kombinert med eksplisitt dependency injection (den nye Ktor 3.2 DI-pluginen, eller Koin/Kodein), slik at man kan bytte ut infrastruktur og lastes moduler forskjellig i test og produksjon. For feilhåndtering anbefaler han typede feil via Arrow sin Raise-DSL i stedet for kastede exceptions, slik at forretningsfeil blir en del av signaturen og kan mappes eksplisitt til HTTP-statuskoder i rute-laget. Han viser en domenesentrert lagdeling der ruter er tynne, tjenester og repositories holder logikken, og persistens gjøres med SqlDelight og KotlinX Serialization; strukturert samtidighet fra coroutines brukes samtidig til å håndtere ressurslivssyklus og graceful shutdown. Testing baseres på TestContainers og at man kan mocke enkeltavhengigheter uten å røre resten av grafen. Hovedbudskapet er at en Ktor-utvikler bør velge sitt eget «meningssett» tidlig – modulær DI, typede feil og en tydelig domenekjerne – slik at tjenesten forblir enkel å teste, refaktorere og skalere når den vokser.

**Notater fra konferansen:**
- Greit foredrag, men ikke spesielt interessant

**Tags:** `Ktor` · `Backend` · `Arkitektur` · `Arrow` · `Feilhåndtering` · `DDD`

**📹** [Opinionated Ktor Services | Simon Vergauwen](https://www.youtube.com/watch?v=JOZFZ__3M7Q)

---

### 1300 How google.com/search builds on Kotlin coroutines for highly scalable, streaming, concurrent servers — Sam Berlin, Alessio Della Motta

Sam Berlin og Alessio Della Motta fra Google Search Infra viser hvordan google.com/search har bygget en tjener-stack på Kotlin coroutines for å drive lavlatens, streaming og massivt samtidige søkeforespørsler i produksjon. Kjernen i foredraget er Qflow – et internt grafbasert DSL som lar utviklere deklarere asynkrone dataavhengigheter på toppen av vanlig Kotlin-forretningslogikk, slik at planleggeren automatisk kan kjøre uavhengige noder parallelt og streame delresultater videre så snart de er klare. For å håndtere kompleksiteten instrumenterer teamet coroutine-runtimen med per-node latensmåling og kritisk-vei-analyse, slik at ingeniørene kan se nøyaktig hvilke suspend-punkter som holder svartiden nede i sluttbrukerens tail latency. De lener seg tungt på structured concurrency for å garantere at kansellering, feilhåndtering og ressursopprydding forplanter seg korrekt gjennom hele grafen, selv når tusenvis av samtidige coroutines fan-outes per forespørsel. Erfaringen fra Google-skala er at «asynkron som standard» bare fungerer når språket, DSL-et og observabiliteten er designet sammen – ellers drukner utviklerne i callback-tenkning eller usynlige flaskehalser. Lærdommen for backend-utviklere er å behandle coroutines som en plattform man bygger verktøy rundt, ikke bare et språkfeature: invester i grafmodell, tracing og strukturert livssyklus før skalaen kommer.

**Notater fra konferansen:**
- Interessant å se hvordan Google bruker Kotlin-coroutines
- Fullt foredrag – lite plass til tilhørere

**Tags:** `Coroutines` · `Google` · `Qflow` · `Structured concurrency` · `Skala` · `Casestudie` · `Observability`

**📹** [How google.com/search builds on Kotlin coroutines... | Sam Berlin, Alessio Della Motta](https://www.youtube.com/watch?v=6D1yV5o4CWo)

---

### 1400 Local Lifetimes for Kotlin — Ross Tate

Ross Tate presenterte et forslag om «local lifetimes» i Kotlin — et typesystem-tillegg der et nytt `local`-nøkkelord på parametere (og `local class`-deklarasjoner) begrenser hvor lenge en referanse får leve, supplert av en subskript-notasjon som `Iterator<B>_{this&transform}` som binder returtypens levetid til inn-parameterne. Målet er å forhindre at ressurser og tilbakekall lekker ut av kallets leksikalske ramme, slik at man trygt kan bygge effektlignende mønstre som `Raise<E>`, non-local return i `fold`, samt lekkasjefrie byggere som `buildMap` og `lazy`. Forslaget ligger tettere på scope-funksjoner (`let`, `apply`, `run` blir typesikre uten å endre bruksmønsteret) og gir grunnlag for «leksikalsk suspend» ved siden av dagens coroutines, mens det utfyller context parameters som en ortogonal mekanisme. Ross viste eksempler som `MappingIterator`-implementasjon, lokalisering av standardbiblioteket og et casestudium med pods4k-biblioteket der bare rundt tjue annoteringer trengtes – og forklarte at kompilatoren kan behandle levetider som en form for generisk parameter og utlede dem på samme måte som typeargumenter. Han la vekt på at forslaget er bakoverkompatibelt: eksisterende kode fortsetter å virke, `Any` kan gjøres `local` uten å bryte arv, og biblioteker kan gradvis annotere signaturer uten å tvinge klienter til endringer. Arbeidet er publisert som design notes i KEEP #485 og er fremdeles forskning under utvikling, delt tidlig for å samle tilbakemeldinger før et formelt KEEP-forslag.

**Notater fra konferansen:**
- Interessant og nyttig ny Kotlin-feature

**Tags:** `Språkdesign` · `Type system` · `Forslag` · `Escape analysis` · `Effects` · `Compiler`

**📹** [Local Lifetimes for Kotlin | Ross Tate](https://www.youtube.com/watch?v=6ALhoqxYrV0)

---

### 1515 Why Most AI Agents Never Scale? Building Enterprise-Ready AI with Koog — Vadim Briliantov

Vadim Briliantov peker på hvorfor de fleste AI-agenter aldri når produksjon: de mangler feiltoleranse når LLM-kall svikter, de mister tilstand under lange kjøringer, kontekstvinduet eksploderer i løpende samtaler, arbeidsflytene er løst typet og «prompt-limt», og de er dårlig koblet til eksisterende enterprise-stack og observability. Koog svarer på dette med innebygde retries, agent-persistens som gjenoppretter hele tilstandsmaskinen (ikke bare chat-historikken), automatisk historikk-komprimering for lange kontekster, og en typet workflow-DSL som gjør agentlogikken forutsigbar. Rammeverket har førsteklasses observability gjennom OpenTelemetry – nå også på tvers av Kotlin Multiplatform – med kobling til verktøy som Langfuse, samt integrasjoner mot Spring Boot/Spring AI og en frakoblet HTTP-transport som spiller pent med Ktor og annen JVM-infrastruktur. Under KotlinConf 2026 annonserte Briliantov Koog 1.0 som stabil utgivelse med ett års API-stabilitetsgaranti, redesignet Java-interop, Anthropic prompt caching og en Mercedes-Benz-case rundt agenter for kjøretøyvedlikehold. Hovedbudskapet for Kotlin-utviklere er at man ikke lenger trenger å bygge egne løsninger for feilhåndtering, persistens og sporing – idiomatisk Kotlin pluss Koog gir de byggeklossene enterprise-agenter faktisk trenger for å skalere.

**Notater fra konferansen:**
- Erfaringsforedrag om AI

**Tags:** `Koog` · `AI-agenter` · `Enterprise` · `Observability` · `LLM`

**📹** [Why Most AI Agents Never Scale? | Vadim Briliantov](https://www.youtube.com/watch?v=9XL0r5lJNDs)

---

### 1615 Talking to terminals (and how they talk back) — Jake Wharton

Jake Wharton tar oss med på et dypdykk i hvordan CLI-programmer faktisk snakker med moderne terminaler, langt utover det å skrive ut tekst i en farge. Han rammer inn terminal-I/O gjennom ANSI-escape-sekvenser, kontrollkoder, terminfo-databasen og innkommende input som må parses byte for byte, og viser hvor stor forskjell det er mellom Windows-konsollen og Unix-pty-er. Kjernen i foredraget er hans egen Mosaic, en Compose-basert TUI-stack for Kotlin, sammen med det underliggende mosaic-terminal-laget som nå kjører en egendreven parser slik at KMP-apper får lik oppførsel både på JVM og Kotlin/Native. Wharton går gjennom praktiske fallgruver: hvordan man leser museklikk og utvidede tastetrykk via Kitty-keyboardprotokollen, hvordan man reagerer momentant på resize-, fokus- og temaendringer, og hvorfor terminfo ofte lyver om hva terminalen faktisk støtter. Underveis viser han levende demoer med bilder rendret rett i terminalen, jevn frame sync, og små interaktive apper bygd rundt `runMosaic` og Compose-state-håndtering. Hovedlærdommen for Kotlin-utviklere som lager CLI- eller TUI-verktøy er å ikke skrive sitt eget escape-lag fra bunnen, men heller bygge på Mosaic og den delte Multiplatform-terminalabstraksjonen slik at OS-forskjellene og de kroniske edge-casene håndteres én gang for alle.

**Notater fra konferansen:**
- Morsomt teknisk foredrag

**Tags:** `TUI` · `CLI` · `Mosaic` · `Compose` · `KMP` · `Dypdykk`

**📹** [Talking to terminals (and how they talk back) | Jake Wharton](https://www.youtube.com/watch?v=QYlzKV0Oe1A)

---

### 1715 Robocoders: The [K]agematch — Viktor Gamov, Baruch Sadogursky

En underholdende avslutning på dag én der ulike AI-kodeagenter ble satt opp mot hverandre i en «cage match» (med K for Kotlin). Agentene fikk samme Kotlin-oppgaver og publikum kunne se i sanntid hvordan ulike modeller, prompts og verktøykjeder takler reelle programmeringsutfordringer – like mye en demonstrasjon av status for AI-kodeassistenter som av hvor langt agentene ennå har igjen.

**Notater fra konferansen:**
- Godt potensial, men foredraget var avhengig av god nettverksytelse – noe som ødela det
- Kunne vært morsomt hvis nettverket hadde fungert som det skulle

**Tags:** `AI` · `AI-agenter` · `Live demo` · `Underholdning`

**📹** Individuell video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

---

## May 22

**📹 Live-stream / opptak fra hovedsal:** [KotlinConf'26 – Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I) – inneholder hovedsal-foredragene fra dag 2.

### 0900 We were meant to be — Lena Reinhard *(Day 2 Keynote)*

Lederutvikler og tidligere VP of Engineering Lena Reinhard holdt dag 2-keynoten med et menneskelig blikk på tech-bransjen i 2026. Hun adresserte usikkerheten mange føler i AI-tidsalderen – produktivitetsdebatten, hvordan karriereveier endrer seg, og spørsmålet om disse karrierene i det hele tatt vil eksistere som før. Et reflekterende foredrag om teknologi, mennesker, krise og fremtiden, formet gjennom en åpen «work log» i månedene før konferansen.

**Notater fra konferansen:**
- Inspirerende foredrag

**Tags:** `Keynote` · `Karriere` · `Mennesker` · `AI-debatt`

**📹** Inngår i [Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I) – individuell video forventet senere.

---

### 1015 Dissecting Kotlin: 2026 — Huyen Tue Dao

Ti år etter Kotlin 1.0 tar Huyen Tue Dao publikum gjennom et knippe ferske stabile og forhåndsvisning-funksjoner – med hovedvekt på context parameters som stabiliseres i Kotlin 2.4, sammen med tilhørende KEEP-forslag og andre nyheter fra språkets siste utviklingsrunder. Hennes signaturmetode er å bruke både design og implementasjon som linse: hun leser KEEP-diskusjonene for å forstå hvorfor komiteen valgte som de gjorde, og dissekerer deretter den genererte bytekoden for å vise hva funksjonen faktisk koster og betyr på JVM. Underveis peker hun på konkrete overraskelser – som hvordan context parameters måtte erstatte context receivers etter praktiske problemer, og hvilke fallgruver som oppstår når kildekoden ser elegant ut mens kompilatoren gjør noe helt annet bak kulissene. Hun leser dette som et signal om at Kotlin nå prioriterer ekspressiv, kontekstsensitiv kode og mer disiplinert språkdesign framfor rene syntaktiske godbiter. Hovedbudskapet er at Kotlin-utviklere blir bedre av å lese både KEEPs og bytekode: å forstå hvordan en funksjon ble designet og hvordan den lander i praksis, gjør deg til en tydeligere forfatter av din egen Kotlin.

**Tags:** `Kotlin 2.4` · `Context parameters` · `KEEP` · `Språkdesign` · `Dypdykk`

**📹** [Dissecting Kotlin: 2026 | Huyen Tue Dao](https://www.youtube.com/watch?v=PB2YYHpEhkQ)

---

### 1115 Idiomatic Kotlin applications with Spring Boot 4 — Sébastien Deleuze

Sébastien Deleuze viser hvordan Spring Boot 4 gjør backend-utvikling i Kotlin mer idiomatisk enn noen gang, med korte demoer på tvers av bygg, null-safety, serialisering, observability, persistens og AI. JSpecify-annotasjoner er nå rullet ut i hele Spring-porteføljen og oversettes automatisk til Kotlin-nullability takket være K2-kompilatoren, slik at plattformtyper og uventede NPE-er i praksis forsvinner og Spring-API-ene føles native i Kotlin. Den offisielle Kotlin-tutorialen for Spring Boot er migrert fra JPA til Spring Data JDBC fordi det gir mer idiomatisk kode med uforanderlige `data class`-entiteter og en lettere stack som spiller bedre sammen med språket. For skalerbare API-er anbefaler Deleuze coroutines med automatisk kontekstpropagering for tracing og observability, samt virtual threads som lar deg få høy samtidighet uten å ta på seg den reaktive kompleksiteten. Spring Boot 4 leverer også en dedikert `spring-boot-starter-kotlinx-serialization-json`, forutsigbar sameksistens mellom Jackson og kotlinx.serialization, og Kotlin 2.2 som ny baseline. Hovedbudskapet er at Kotlin+Spring-stacken nå er så godt integrert at man kan velge mellom suspenderende funksjoner og virtuelle tråder etter behov, og få null-safety på kjøpet uten ekstra arbeid.

**Notater fra konferansen:**
- Interessant å se hvordan Spring-vedlikeholderne implementerer støtte for Kotlin, og hvordan dette gjør idiomatiske Kotlin-applikasjoner enkle å lage

**Tags:** `Spring Boot` · `Backend` · `Null-safety` · `Coroutines` · `Virtual threads` · `JSpecify`

**📹** [Idiomatic Kotlin applications with Spring Boot 4 | Sébastien Deleuze](https://www.youtube.com/watch?v=TxmBk_VhuqY)

---

### 1300 Eval-Driven Development: The Fine Line Between Agentic Success and Failure — Urs Peter

Urs Peter argumenterer for at Eval-Driven Development (EDD) er den ingeniørdisiplinen som skiller fungerende AI-agenter fra prototyper som havarerer i produksjon, og han flytter dermed evaluering fra en ad hoc-aktivitet til et førsteklasses utviklingsartefakt på linje med tester og CI. Han organiserer testing av agenter i tydelige lag: enhetstester for enkeltverktøy og promptfunksjoner, integrasjonstester for verktøykjeder og LLM-kall, ende-til-ende-tester som kjører hele agentflyten mot realistiske scenarier, og regresjonstester som fanger opp at nye modellversjoner eller promptendringer bryter tidligere adferd. På metrikksiden kombinerer han deterministiske mål (latency, kostnad, verktøysuksess, JSON-validitet) med LLM-as-judge-scorer for korrekthet, relevans og tone, og han viser hvordan man oppdager stille degradering i produksjon ved å sample trafikk, kjøre kontinuerlig scoring og alarmere på drift i disse metrikkene fremfor bare på harde feil. Peter demonstrerer også hvordan man bruker en LLM til å generere syntetiske testtilfeller og edge cases fra en liten seed, slik at evalueringsdatasettet vokser i takt med agenten. Konkret vises alt integrert i Koog gjennom JetBrains sitt rammeverk: agent- og verktøydefinisjoner får evaluatorer koblet på, kjøringer instrumenteres via Koogs observability-lag, og evalueringssuiter kjøres i CI som del av byggepipelinen. Hovedbudskapet er at en agent uten evaluering ikke er ferdig – du eier metrikkene og regresjonsvernet like mye som koden, ellers seiler kvaliteten ukontrollert med hver modell- og promptendring.

**Notater fra konferansen:**
- Intro til EDD for å bygge gode AI-agenter og sikre at de blir riktige

**Tags:** `AI-agenter` · `Evaluering` · `Koog` · `Metode` · `Testing`

**📹** [Eval-Driven Development | Urs Peter](https://www.youtube.com/watch?v=L2bZzPXfmyE)

---

### 1400 Context parameters and API design — Alejandro Serrano Mena

Context parameters ble stabilisert i Kotlin 2.4 og skrives foran signaturen som `context(users: UserService) fun User.getFriends()`, slik at verdien tres implisitt gjennom kallkjeden uten manuelt gjennomstikk på hvert nivå. Serrano Mena bruker en teater-metafor – «spotlight-prinsippene» – for å skille hovedroller (mottakere, `this`) fra biroller (context parameters): en mottaker kan fylle et kontekstargument implisitt, men aldri motsatt, og Kotlin begrenser bevisst antall «hovedroller» på scenen for å unngå at det implisitte scopet blir uoversiktlig, slik det tidligere context receivers-forslaget led under. Context parameters egner seg best i to mønstre: usynlige kontekster som `Logger` eller Arrows `Raise` (der bindestreknavn `_` kan brukes), og «leaf-only»-tjenester som `UserService` eller sjekker-kontekster i selve Kotlin-kompilatoren – altså typesikker, «fattigmanns» dependency injection, transaksjons-, logg- og autorisasjonsscoper. Byggere og DSL-er som `buildList` eller `kotlinx.html` skal derimot forbli mottakere, for objektet som bygges er hovedrollen i scenen, og bruk av `DslMarker` og nøsting bryter ellers sammen. Anti-mønsteret Serrano advarer mot er «bridge function hell» – å duplisere hele API-et både som medlemmer/extensions på writer-typen og som kontekstuelle funksjoner – og å konvertere alt fra mottakere til context parameters bare fordi språket nå tillater det; når rekkefølgen på mottakere skaper trøbbel i rekursive kall, bør man heller lage små «dance»-hjelpere som gjør `with { ... }`-vendingen for kalleren. Hovedbudskapet til API-designere er derfor konseptuelt, ikke syntaktisk: velg mottaker når verdien fortjener rampelyset, og context parameter når den bare skal skygges bak kulissene.

**Notater fra konferansen:**
- Godt foredrag om en nyttig ny feature i Kotlin (stabil i 2.4)

**Tags:** `Kotlin 2.4` · `Context parameters` · `API-design` · `DSL` · `Språkdesign`

**📹** [Context parameters and API design | Alejandro Serrano Mena](https://www.youtube.com/watch?v=O1nTwf0QPj4)

---

### 1515 gRPC, Made for Kotlin — Alexander Sysoev

Alexander Sysoev viste i denne lyntalen hvordan kotlinx-rpc endelig gjør gRPC til et fullt idiomatisk Kotlin-verktøy, i stedet for at man må lene seg på autogenererte Java-stubber med callbacks og manuell trådhåndtering. Tjenester defineres som vanlige Kotlin-interfaces der de fire gRPC-mønstrene faller rett inn i språket: unary blir en ren `suspend fun`, server-streaming returnerer `Flow<T>`, klient-streaming tar `Flow<T>` som parameter, og bidirectional kombinerer begge – alt bundet sammen av strukturert samtidighet slik at kansellering av en coroutine også river ned den underliggende RPC-en. Demoen viste en Kotlin-klient og en Kotlin-server som snakker sammen over samme grensesnitt, med Flow-baserte streams som håndteres på begge sider uten boilerplate. Under panseret er kotlinx-rpc sin gRPC-modul bygget som en Kotlin Multiplatform-implementasjon med egen protobuf-serialisering, og første dev-utgivelse (0.11.0-grpc) støtter JVM, Android og native mål. Statusen er fortsatt eksperimentell preview, men biblioteket følger Kotlin-utviklingen tett og er klart for Kotlin 2.4, slik at team kan begynne å prøve det ut i backend-prosjekter allerede nå.

**Notater fra konferansen:**
- Fin lyntale om hvordan bruke det nye Kotlin-biblioteket for gRPC

**Tags:** `Lyntale` · `gRPC` · `kotlinx-rpc` · `Backend` · `Coroutines` · `Flow`

**📹** [gRPC, Made for Kotlin | Alexander Sysoev](https://www.youtube.com/watch?v=RqbTeZXgkdQ)

---

### 1545 KotlinLLM: Leveraging AI for Runtime Logic Delegation in Kotlin — Stanislav Sandler

I denne lyntalen viste Stanislav Sandler frem KotlinLLM, et forskningsprototyp fra JetBrains som lar deg delegere forretningslogikk til en LLM ved runtime bak en typet Kotlin-fasade – via såkalte Smart macros som `asLlm<F, T>()` der du beskriver hva du vil ha, og AI-en fyller inn kroppen med generert Kotlin-kode mot dine data classes og enums. Poenget er at delegeringen er eksplisitt i koden, at resultatet persisteres som vanlig Kotlin-kildekode og at det blir portabelt: når koden først er generert kjører den uten LLM-kall, uten ekstra latens eller kostnad. Runtime delegation kobles inn i den bredere Kotlin AI-stakken, og Tracy – JetBrains sitt nye AI-observabilitetsbibliotek bygget på OpenTelemetry – sørger for at genereringen kan spores, måles og debugges på lik linje med vanlige tjenestekall, mens caching av genererte macroer og fallback til tidligere versjoner behandles som førsteklasses bekymringer. Mønsteret gir mest mening der input er semistrukturert eller reglene endrer seg raskt (parsing, adaptere, klassifisering, mock-implementasjoner av grensesnitt) – ikke som erstatning for imperativ kode der determinisme og ytelse teller mest. Hovedbudskapet: du kan hente inn AI som en språknær byggekloss i Kotlin uten å ofre type-safety, observabilitet eller reproduserbarhet.

**Notater fra konferansen:**
- God lyntale om LLM for Kotlin

**Tags:** `Lyntale` · `KotlinLLM` · `Tracy` · `Runtime delegation` · `LLM`

**📹** [KotlinLLM: Leveraging AI for Runtime Logic Delegation | Stanislav Sandler](https://www.youtube.com/watch?v=tmPZajBUsKg)

---

### 1615 Spec-Driven Development with AI Agents: From High-Level Requirements to Working Software — Anton Arhipov

Arhipov presenterte «spec-driven development» som en strukturert måte å jobbe med AI-kodeagenter på. Metoden går ut på å starte med høyt-nivå krav, raffinere dem til en utviklingsplan, og bryte planen ned i en sporbar oppgaveliste – alt som artefakter (`requirements.md`, `plan.md`, `tasks.md`) som agenten jobber fra. Et rammeverk for å gjøre AI-koding forutsigbar og reviewbar i stedet for kaotisk.

**Notater fra konferansen:**
- Intro til SDD, en metode for å bygge kode med kode-agenter

**Tags:** `AI` · `AI-agenter` · `Metode` · `Workflow`

**📹** Individuell video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin). Lysbilder: [Speaker Deck](https://speakerdeck.com/antonarhipov/spec-driven-development-with-ai-agents-from-high-level-requirements-to-working-software-e397ad2e-3484-4bfa-a80b-6c47c593ed11).

---

# Foredrag jeg vil se opptak av

Foredrag jeg gikk glipp av (parallelle spor / kollisjoner) og som jeg vil se når videoene kommer på YouTube. De fleste er nå publisert – individuelle lenker er lagt inn under.

## May 21

### 1015 A tale of the Gradle DSLs — Paul Merlin

Paul Merlin tar oss gjennom historikken til Gradle sine build-språk, fra den dynamiske Groovy-DSL-en som ga stor fleksibilitet men svakt IDE-vern, via den statisk typede Kotlin DSL-en som ble innført for å styrke vedlikeholdbarhet, brukeropplevelse og navigering, og videre mot et rent deklarativt konfigurasjonsspråk inspirert av Kotlin. Han viser hvilke mønstre som har vist seg holdbare på tvers av generasjonene, særlig tanken om et deklarativt kjernespråk med tydelige utvidelsespunkter, og forklarer hvorfor Kotlin DSL nå er standardvalget: den kombinerer lesbarhet og autofullføring med tilstrekkelig kraft til plugin-utvikling. Sentralt i foredraget står skillet mellom software definition og build logic, og hvordan denne oppdelingen tjener både applikasjonsutviklere, build-ingeniører og plugin-forfattere som bruker disse verktøyene daglig. Konkret råder Merlin til å holde build-skriptene tynne og deklarative, flytte imperativ logikk ut i plugins under `buildSrc` eller composite builds, og strukturere prosjektene slik at man allerede i dag drar full nytte av Kotlin DSL samtidig som man er forberedt på overgangen til det kommende deklarative språket.

**Tags:** `Gradle` · `Kotlin DSL` · `Build tools` · `Historikk`

**📹** [A tale of the Gradle DSLs | Paul Merlin](https://www.youtube.com/watch?v=k8T9IOnXPao)

---

### 1015 Tiny Models, Big Impact: On-Device AI for Real Apps — Hammad Akram

Hammad Akram viste hvordan små språkmodeller (SLM-er) kan kjøre direkte på Android-enheter via Llama Stack Kotlin SDK-en, som pakker inn ExecuTorch og lar utviklere bytte mellom lokal og fjern inferens med tilnærmet identisk kode. Han demonstrerte praktiske bruksområder som chat-fullføring, RAG med on-device vektordatabaser og bildeforståelse, uten at brukerdata må forlate telefonen. Foredraget var ærlig om avveiningene ved on-device AI: latens og personvern vinner, men du må designe rundt modellstørrelse på disk, batteribruk under generering og at kvaliteten ligger et hakk under skybaserte flaggskip-modeller. Akram plasserte tilnærmingen som et komplement til JetBrains sin bredere AI-satsning – der Koog og MCP dekker agent-flyter og IDE-integrasjon – mens SLM-er på enhet passer best i personvernkritiske og offline-scenarier. Konklusjonen var at en riktig valgt liten modell allerede kan levere reell nytteverdi i produksjonsapper, så lenge man er bevisst på begrensningene.

**Tags:** `AI` · `LLM` · `On-device` · `Llama Stack` · `Android`

**📹** [Tiny Models, Big Impact | Hammad Akram](https://www.youtube.com/watch?v=Rqj4QCdwBMc)

---

### 1045 Run, Kotlin, Run! — Marc Reichelt

I denne lyntalen tar Marc Reichelt utfordringen med å kjøre den samme lille `isPrime`-funksjonen fra et Kotlin Multiplatform-prosjekt på så mange – og gjerne så eksotiske – måter som mulig i løpet av et kvarter. Han går raskt gjennom det opplagte som JVM og Android, hopper over til Kotlin Playground (der man også kan bytte backend til JS eller Wasm), og bruker deretter Kotlin/Native til å bygge egne binærfiler for macOS, for Linux (kjørt via Docker) og for Windows (`.exe` kjørt via Wine på Mac). Fra utviklerverktøyene demonstrerer han IntelliJ scratch files, `.kts`-skript kjørt både fra IDE-en og fra `kotlin`-kommandolinjen, og til og med `.kts`-filer gjort kjørbare med shebang. Til slutt bruker han samme felles modul til å starte iOS-appen fra Android Studio og til å drive SwiftUI-previews i Xcode. Poenget er ikke ytelsestall eller binærstørrelser, men en energisk feiring av hvor mange kjøremåter Kotlin har fått – hver nye demo markert med et bjelleslag.

**Tags:** `Lyntale` · `JVM` · `Kotlin/Native` · `Kotlin/Wasm` · `KMP`

**📹** [Run, Kotlin, Run! | Marc Reichelt](https://www.youtube.com/watch?v=-w97euRLTBA)

---

### 1115 Kotlin/Wasm: Finally, the missing piece for a full stack Kotlin webapp! — Dan Kim

Dan Kim viser i praksis hvordan Kotlin/Wasm endelig lar deg bygge en komplett full-stack webapp i ett og samme språk, ved å demonstrere en todo-applikasjon på rundt 486 linjer der frontend, API, database og delte modeller alle er skrevet i Kotlin. Stacken består av Compose Multiplatform for UI-et (kompilert til Wasm og rendret direkte til canvas via Skia, uten omveien om DOM), Ktor som coroutine-native HTTP-server der hver handler er en suspend-funksjon, Exposed som JetBrains sitt SQL-bibliotek uten annotasjoner eller kodegenerering, og Coroutines som en gjennomgående asynkron modell på tvers av lagene. Wasm er den «manglende brikken» fordi det gir Kotlin en førsteklasses frontend-runtime i nettleserens sandkasse med tilnærmet native ytelse og piksel-perfekt UI, slik at man slipper Kotlin/JS-friksjonen mot JavaScript-økosystemet og kan dele typer og domenemodell direkte mellom klient og server. Utvikleropplevelsen i dag er overraskende ren – lite boilerplate, eksplisitt kode og en produktiv indre løkke – men Kim er tydelig på at Kotlin/Wasm fortsatt er i beta, så bundle-størrelse, browserstøtte og modenhet er ting man må gå inn i med åpne øyne.

**Tags:** `Kotlin/Wasm` · `Full-stack` · `Compose` · `Ktor` · `Exposed`

**📹** [Kotlin/Wasm: Finally, the missing piece | Dan Kim](https://www.youtube.com/watch?v=JThr4fn9OOw)

---

### 1300 Real-World Data Science With Kotlin Notebook — Adele Carpenter

Adele Carpenter viser hvordan hun analyserer et powerlifting-datasett på over 3,3 millioner rader fra Open Powerlifting direkte i Kotlin Notebook, uten å forlate IntelliJ eller lære Python fra bunnen av. Rådataene ligger i Postgres, og hun bruker DataFrame-bibliotekets `readSqlTable` og `readSqlQuery` til å filtrere på databasesiden før resultatene hentes inn som en dataframe – en pragmatisk løsning når hele datasettet ikke får plass i minnet. Deretter validerer og utforsker hun tallene, og visualiserer trender rundt deltakelsen i 2023 med Kandy, et deklarativt plottbibliotek bygget på lets-plot. Poenget hennes er at Kotlin-utviklere kan drive reell, utforskende dataanalyse i sitt vante økosystem, og at trioen Notebook + DataFrame + Kandy langt på vei matcher Pythons pandas- og matplotlib-stakk for praktiske caser. Python har fortsatt et bredere bibliotekutvalg for spesialisert statistikk og ML, men for SQL-drevet utforskning, datavalidering og visualisering er Kotlin-veien i dag fullt brukbar.

**Tags:** `Data Science` · `Kotlin Notebook` · `DataFrame` · `Kandy` · `Postgres`

**📹** [Real-World Data Science With Kotlin Notebook | Adele Carpenter](https://www.youtube.com/watch?v=1sp05VqRVDA)

---

### 1330 SwiftPM support for Kotlin Multiplatform — Timofey Solonin

Timofey Solonin viste i denne lyntalen hvordan Kotlin Multiplatform nå kan konsumere SwiftPM-avhengigheter direkte fra Gradle via en ny `swiftPMDependencies {}`-blokk, demonstrert med populære pakker som FirebaseFirestore, Sentry og Google Maps SDK. Xcode-integrasjonen fungerer ved at Gradle-taska `integrateLinkagePackage` genererer en syntetisk SwiftPM-pakke som legges inn i `.xcodeproj` og deretter oppdateres automatisk når avhengigheter endres, med en `Package.resolved`-låsfil sjekket inn i repoet. Under panseret oppdager Kotlin Gradle-pluginen Clang-modulene i Swift-pakkene og eksponerer dem for Kotlin/Native under navnerommet `swiftPMImport.<group>.<project>.<Module>`, slik at Objective-C- og Swift-API-er (via genererte Obj-C-headere) kan importeres direkte i `iosMain`. Transitiv maskinkode kobles inn automatisk ved testing og framework-linking, mens publisering av KMP-biblioteker som selv bruker SwiftPM-importer foreløpig ikke er støttet (sporet i KT-84420) – funksjonen er i alfa, og statiske rammeverk anbefales for å unngå duplikatsymboler.

**Tags:** `Lyntale` · `KMP` · `iOS` · `SwiftPM` · `Kotlin/Native` · `Tooling`

**📹** [SwiftPM support for Kotlin Multiplatform | Timofey Solonin](https://www.youtube.com/watch?v=GrO-bTnn_Ng)

---

### 1400 Codex for Kotlin Engineers — Benedict Kerres

Kort sesjon om hvordan OpenAI Codex passer godt sammen med Kotlin sitt strenge typesystem, tydelige domenemodeller og testbare struktur når man genererer, refaktorerer og gjennomgår kode. Kerres demonstrerer hvordan man bruker Codex effektivt i en Kotlin-arbeidsflyt. Praktisk innretning mot AI-assistert utvikling for Kotlin-utviklere.

**Tags:** `AI` · `Codex` · `Workflow` · `AI-assistert utvikling`

**📹** Individuell video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

---

### 1430 Building AI-Powered Web Apps in Kotlin/Wasm — Zalim Bashorov

Bashorov ser på de nye, native AI-API-ene som moderne nettlesere er i ferd med å standardisere, og hvordan man kan bygge fullt klientside-baserte AI-apper uten serverinfrastruktur. Han dekker fordelene (personvern, responsivitet, offline-bruk) og begrensningene ved Web AI, og demonstrerer eksempler som sanntidsoppsummering og oversettelse kjørt rett i nettleseren – alt fra Kotlin/Wasm.

**Tags:** `Kotlin/Wasm` · `AI` · `Web` · `On-device`

**📹** Individuell video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

---

### 1515 Expedited Shipping: Accelerating iOS Development with KMP at Amazon — Jessalyn Wang

Jessalyn Wang forteller hvordan Amazon Delivery bruker Kotlin Multiplatform for å akselerere iOS-utvikling på tvers av en stor organisasjon med mange team. Kjernen er et internt bibliotek kalt «App Platform» som standardiserer state management, dependency injection og dekopling mellom logikklag, slik at forretningslogikk kan deles mens hver plattform beholder sitt eget UI. På iOS-siden går hun i dybden på integrasjonen mot SwiftUI: hvordan Kotlin-eksponerte state holders og observerbar state kobles idiomatisk mot SwiftUI-views, og hvordan navigasjon modelleres i delt kode uten å bryte med SwiftUIs deklarative navigasjonsmønstre. Hun deler også hvilke fallgruver teamet støtte på i Kotlin/Native-interop og hvordan API-ene ble slipt for at iOS-utviklere skulle oppleve det delte laget som et naturlig Swift-bibliotek. Til slutt viser hun hvordan plattformen skalerer i en Amazon-kontekst der mange produktteam bygger på samme grunnmur, med tydelige konvensjoner som reduserer duplisert arbeid og gjør det raskere å levere nye funksjoner på begge plattformer.

**Tags:** `KMP` · `iOS` · `SwiftUI` · `Skala` · `Casestudie` · `Amazon`

**📹** [Expedited Shipping: Accelerating iOS Development with KMP at Amazon | Jessalyn Wang](https://www.youtube.com/watch?v=DKE_aNl-2HU)

---

### 1515 The State of Amper — Joffrey Bion

Joffrey Bion oppsummerer et travelt år for Amper, som ved KotlinConf 2026 ble omdøpt og reposisjonert som selve fundamentet for Kotlin Toolchain – JetBrains sin visjon om én `kotlin`-kommando som dekker prosjektopprettelse, bygging, testing, pakking og publisering. Blant høydepunktene fra det siste året trekker han fram Amper 0.10 med JDK-provisioning, Maven-konverter og støtte for egendefinerte kompilator-plugins, samt november-2025-forhåndsvisningen av utvidbarhet med lokale plugins og forbedret IDE-integrasjon som quick-fixes og konfigurasjonshjelp for tredjeparts Kotlin compiler plugins. Med Kotlin Toolchain 0.11 kom prosjektet i Alpha, og fikk publisering av JVM-biblioteker som møter Maven Central-krav med bare noen få linjer konfigurasjon, samt nye API-er for plugin-utvikling. På veikartet framover står deling og publisering av plugins slik at de kan gjenbrukes på tvers av prosjekter, plugin-templates som konfigurerer forbrukermoduler automatisk, samt fortsatt utbygging av IDE-støtte og bredere multiplatform-dekning på vei mot en stabil 1.0.

**Tags:** `Amper` · `Kotlin Toolchain` · `Build tools` · `JetBrains` · `Tooling`

**📹** [The State of Amper | Joffrey Bion](https://www.youtube.com/watch?v=S19BE4Xvyrs)

---

### 1515 Compose beyond UI : Display and Print! — Salomon Brys

Salomon Brys strukturerte lyntalen rundt to konkrete sideprosjekter som viser at Compose kan brukes langt utover vanlige app-grensesnitt: presentasjonsrammeverket CuP (Compose ur Pres), som lar ham programmere lysbilder med de samme komponentene som han bygger UI med til daglig, og Card-Composer, et Compose Desktop-bibliotek for å designe og trykke brettspillkort. For kortprosjektet erstattet han Material-temaet med et eget CardTheme, redefinerte enhetssystemet slik at 1 dp tilsvarer 1 PostScript-punkt (1/72 tomme) for å tenke direkte i millimeter og tommer, og la til `FormattedText` for tag-basert rik tekst tilpasset trykk. Selve rendringen skjer i en `cardComposerApplication()`-funksjon som gir forhåndsvisning og eksportdialog med PNG per kortgruppe og PDF klar for profesjonell trykking med bleed-marger, mens CuP demonstrerer hvordan den samme Compose-kjøretiden animerer kildekode og progressive fremhevninger i stedet for Keynote-slides. Den bærende innsikten er at Compose i praksis er en tegne-motor bundet til Skia – så snart utvikleren peker den mot en PDF- eller bilde-flate i stedet for et vindu, blir hele det deklarative UI-verktøysettet plutselig et fullverdig verktøy for grafisk design og produksjon.

**Tags:** `Lyntale` · `Compose Multiplatform` · `Kreativt` · `PDF` · `Print`

**📹** [Compose beyond UI: Display and Print! | Salomon Brys](https://www.youtube.com/watch?v=gi3R122UpgM)

---

### 1615 Increasing quality of AI generated Kotlin code — Sergei Rybalkin (Meta)

Sergei Rybalkin fra Meta viste hvorfor bedre AI-generert Kotlin-kode krever mer enn smartere prompter, og delte hvordan teamet hans løfter kodekvalitet i stor skala. Han beskrev typiske utfordringer som at modellene produserer plausibel, men inkonsistent kode, bruker foreldede API-er eller bryter etablerte idiomer og konvensjoner i en enorm kodebase. For å måle forbedringer bygger Meta systematiske evalueringer som kombinerer automatiske signaler – kompilering, tester og statisk analyse – med menneskelige vurderinger av lesbarhet og vedlikeholdbarhet. Rybalkin la vekt på verktøykjeden rundt agentene: kontekstfiler med Kotlin-idiomer, integrasjon mot lintere og statisk analyse, og feedback-løkker som lar agenten rette opp feil før koden når reviewer. Casestudien fra Meta viste at kombinasjonen av kuraterte retningslinjer, målrettet evaluering og tett kobling mot eksisterende utviklerverktøy gir mer forutsigbar og pålitelig kode enn ren promptoptimalisering, og at oppsettet må tilpasses etter hvert som modellene utvikler seg.

**Tags:** `AI` · `Kodekvalitet` · `Meta` · `Skala` · `Evaluering` · `Casestudie`

**📹** [Increasing quality of AI generated Kotlin code | Sergei Rybalkin](https://www.youtube.com/watch?v=rZvEuqUiPnw)

---

### 1615 Swift Export: Where We Stand — Pamela Hill-Galloway

Statusoppdatering på Swift Export-prosjektet fra JetBrains, som skal erstatte den gamle Objective-C-broen og gi mer idiomatisk Swift-tilgang til delt Kotlin-kode. Hill-Galloway viser kodeeksempler på overgangen, hvilke features som støttes i dag, og hvilke kant-tilfeller som fortsatt mangler arbeid. Målet er at du selv skal kunne vurdere om Swift Export er klar for ditt team.

**Tags:** `KMP` · `iOS` · `Swift interop` · `Swift Export`

**📹** Individuell video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

---

### 1645 Can Kotlin Swift Interop Ever Be Perfect? — Gleb Lukianets

Gleb Lukianets tar utgangspunkt i at Kotlin og Swift på overflaten virker svært like, men at typesystemene, minnemodellene og runtime-semantikken skiller lag på måter som gjør «perfekt» interop nesten umulig. Han går gjennom hva den nye Swift Export-pipelinen faktisk klarer å bygge bro over sammenlignet med den gamle Objective-C-headeren: nullbare primitiver mappes nå direkte til Swift optionals uten `KotlinInt`-bokseklasser, `suspend`-funksjoner blir `async`, `Flow` blir `AsyncSequence`, pakker blir nøstede Swift-enumer, og Kotlin `enum class` blir ekte Swift `enum`. Samtidig tvinger de semantiske forskjellene fram harde designvalg: generiske typer type-slettes til sin øvre grense og støtter i praksis bare Kotlin-klasser (ikke Swifts value types), all cross-language arv er blokkert slik at selv `open`-klasser blir `final` på Swift-siden, og extension-funksjoner degraderes til statiske metoder med eksplisitt mottaker istedenfor idiomatiske Swift-extensions. Sealed classes eksponeres som et hierarki, men taper eksaustivitetssjekken i `switch`, og navngivning beholdes verbatim fra Kotlin uten camelCase-normalisering. Konklusjonen er at Swift Export flytter smertepunktene, men fordi Kotlins nominelle, JVM-inspirerte objektmodell og Swifts protokoll- og value-type-orienterte modell trekker i hver sin retning, må teamet velge mellom Kotlin-troskap og Swift-idiomatikk i hver eneste mapping.

**Tags:** `KMP` · `iOS` · `Swift interop` · `Swift Export` · `Språkdesign`

**📹** [Can Kotlin Swift Interop Ever Be Perfect? | Gleb Lukianets](https://www.youtube.com/watch?v=XnPmdTea3VA)

---

### 1715 The Lord of Collection Functions - The Fellowship of Kotlin — Ben Kadel

Ben Kadel tar oss med på en Tolkien-inspirert reise gjennom Kotlins collection-funksjoner, der hver funksjon presenteres som et medlem av følget i kampen mot imperativ kode. Vi følger klassikere som `filter`, `map` og `partition` sammen med kraftigere våpen som `flatMap`, `zip`, `groupBy` og `associateWith`, før turen ender hos mer eksotiske reisefeller som `windowed` og `runningFold`. Poenget er å vise hvordan standardbiblioteket lar deg uttrykke transformasjoner deklarativt på `List`, `Set` og `Map` framfor å skrive løkker og midlertidige variabler. Kadel rammer det hele inn med eksempler av typen Advent of Code, der riktig valg av collection-funksjon gjør løsningen kortere, lesbarere og nærmere problemformuleringen. Foredraget er både et underholdende show og en praktisk oppslagsbok for utviklere som vil skrive mer idiomatisk Kotlin.

**Tags:** `Collections` · `Funksjonell` · `Standardbibliotek` · `Underholdning`

**📹** [The Lord of Collection Functions | Ben Kadel](https://www.youtube.com/watch?v=iRum03U1oZo)

---

## May 22

### 1015 Automate upgrading to Kotlin 2 with OpenRewrite — Rooz SF, Jonathan Schneider

Rooz SF og Jonathan Schneider viste hvordan OpenRewrite nå har fullverdig støtte for Kotlin 2, slik at store kodebaser kan oppgraderes automatisk i stedet for manuelt. Verktøyet bygger opp en Lossless Semantic Tree (LST) – en type- og formatbevarende representasjon av kildekoden – som gjør at oppskriftene (recipes) kan gjøre presise, kompilatornøyaktige endringer uten å ødelegge kommentarer, whitespace eller stil. Sammensatte oppskrifter håndterer hele migreringsløpet: `UpgradeDependencyVersion` og `ChangeDependency` løfter Kotlin- og bibliotekversjoner i både Groovy- og Kotlin-baserte Gradle-skript, mens API-oppskrifter refaktorerer bruddendringer fra 1.9 til 2.x og retter opp stilinkonsistenser underveis. Gevinsten for store monorepoer er konkret: det som tidligere var uker med manuell PR-vasking blir en deterministisk, repeterbar kjøring som kan skaleres på tvers av hundrevis av moduler og kjøres i CI for å holde koden kontinuerlig oppdatert.

**Tags:** `Tooling` · `Refaktorering` · `OpenRewrite` · `Kotlin 2` · `Migrering`

**📹** [Automate upgrading to Kotlin 2 with OpenRewrite | Rooz SF, Jonathan Schneider](https://www.youtube.com/watch?v=XrPqvtWniuk)

---

### 1015 Advanced Kotlin Native Integration — Tadeas Kriz (Touchlab)

Tadeas Kriz fra Touchlab tar for seg en av de mest oversette begrensningene ved Kotlin Multiplatform: et prosjekt kan i praksis bare inneholde ett Kotlin/Native-binærprodukt om gangen. Foredraget viser hva som skjer hvis man likevel bunter inn flere KMP-binærprodukter i samme applikasjon – blant annet symbolkonflikter, oppblåst størrelse og duplisert runtime som er vanskelig å feilsøke. Kriz går gjennom teknikker for å dele opp kompileringen i mindre biter, slik at hvert team kan jobbe uavhengig uten å bryte enkeltbinær-regelen. Han diskuterer også løsninger tilpasset større organisasjoner med komplekse repostrukturer, der en felles «paraply»-modul samler delkoden fra flere team og leverer det endelige binærproduktet ut mot iOS-siden. Passer for team som allerede bruker KMP i produksjon og møter skaleringssmerter når kodebasen og antallet konsumenter vokser.

**Tags:** `KMP` · `Kotlin/Native` · `Build tools` · `Avansert` · `Touchlab`

**📹** [Advanced Kotlin Native Integration | Tadeas Kriz](https://www.youtube.com/watch?v=Qk2aClaCZgY)

---

### 1015 10 Gradle Best Practices Every Kotlin Developer Should Know — Stefan Wolf

Lynforedrag med 10 viktige Gradle-praksiser basert på offisielle anbefalinger fra JetBrains, Google og Gradle-teamene. Wolf dekker prosjektstruktur, trygg avhengighetshåndtering, vedlikeholdbar build-logikk, vanlige konfigurasjonsfeller og CI-optimalisering – pluss en sniktitt på IntelliJ IDEAs sanntids-build-inspeksjoner. Greit oppslagsverk for både Android-, backend- og multiplatform-utviklere.

**Tags:** `Lyntale` · `Gradle` · `Build tools` · `Best practices`

**📹** Individuell video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

---

### 1045 A First Look at the Kotlin Ecosystem Plugin for Declarative Gradle — Marcin Mycek

Marcin Mycek ga en tidlig demo av Kotlin Ecosystem Plugin – en eksperimentell prototyp bygget oppå Declarative Gradle – som skal gi Kotlin- og KMP-builds en helt ny, deklarativ syntaks. I stedet for imperative Kotlin/Groovy-scripts med håndkonfigurerte source sets, targets og hierarkier, pakker pluginen kompliserte konsepter inn i opinionated «Software Types» (som `kotlinJvmApplication` og en KMP-variant) der utvikleren bare beskriver *hva* som skal bygges, ikke *hvordan*. Mycek viste hvordan den deklarative modellen gjør typiske smertepunkter i KMP – target-oppsett, source set-topologi og plugin-rekkefølge – nesten usynlige, samtidig som IDE-støtte, validering og analyse blir vesentlig bedre fordi build-en er en ren datastruktur. Resonnementet bak endringene er å flytte kompleksitet inn i gjenbrukbare økosystem-plugins slik at build-scriptene blir korte, konsistente og trygge å endre, og å legge grunnlaget for verktøy som IDE-er, migrasjons-recipes og build-init kan forstå direkte. Foredraget var eksplisitt en «first look» på en prototyp under aktiv utvikling, men skisserte tydelig retningen JetBrains og Gradle tar for Kotlin-builds fremover.

**Tags:** `Gradle` · `Build tools` · `Declarative` · `KMP` · `Tooling`

**📹** [A First Look at the Kotlin Ecosystem Plugin for Declarative Gradle | Marcin Mycek](https://www.youtube.com/watch?v=25Ngfn9Bhqc)

---

### 1115 How I Learned to Stop Worrying and Love Value Semantics (in Kotlin) — Marat Akhin

Marat Akhin fra JetBrains sitt Kotlin Language Evolution-team argumenterer for hvorfor value-semantikk fortjener en langt mer sentral plass i Kotlin, i motsetning til den referansesemantikken JVM-utviklere er vant til å sjonglere. Han viser hvordan `data class` og `.copy()` allerede gir et snev av value-tankegang, men at nøstede `.copy()`-kall raskt blir tungvinte når domenemodellen vokser. Løsningen som er på vei er multi-field value classes (eksperimentelt fra Kotlin 2.5), som gir ekte in-place, uforanderlig-først-logikk uten allokeringsoverhead. Han knytter dette sammen med uforanderlige samlinger og peker på Compose som et konkret eksempel der immutability-by-default gjør endringsdeteksjon dramatisk mer effektiv. Benchmarks i foredraget viser at value-orientert design ikke er en akademisk luksus, men fullt praktisk på JVM: ytelsen holder tritt med, og ofte slår, tradisjonelle mutable referanser. Konklusjonen er at Kotlin er i ferd med å bli et språk der man trygt kan slutte å bekymre seg for delt mutabel tilstand og heller lene seg på verdier.

**Tags:** `Språkdesign` · `Value classes` · `Immutability` · `Performance` · `Data class`

**📹** [How I Learned to Stop Worrying and Love Value Semantics | Marat Akhin](https://www.youtube.com/watch?v=YeQijxpnI3E)

---

### 1115 Redefining Machine Learning with Kotlin: A Device-First Approach to AI — Michal Harakal

Michal Harakal presenterte SKaiNET, et Kotlin-basert rammeverk som gjør maskinlæring praktisk på enheten uten å måtte gå veien om Python eller skyløsninger. Kjernen er en typesikker DSL (`nn { }` / `dag { }`) der utviklere definerer nevrale nettverk én gang i idiomatisk Kotlin, og modellen fanges enten som en tape eller en DAG-basert beregningsgraf. Fra samme definisjon kan man kjøre eagert under utvikling og deretter kompilere den til ulike backends – StableHLO/MLIR via IREE for native mål, C99 for Arduino, og Minerva for sikre mikrokontrollere. Harakal viste hvordan lettvekts-ConvNets og kompakte LLM-er kan kjøres fullstendig offline på mobil og innebygde enheter, med Kotlin Multiplatform som tillater deling av modellen på tvers av Android, JVM, Kotlin/Native, Wasm og JS. Poenget er at typesikkerhet, ytelse og personvern kan gå hånd i hånd når AI flyttes fra serveren og ned til brukerens egen enhet.

**Tags:** `AI` · `ML` · `KMP` · `On-device` · `SKaiNET` · `Personvern`

**📹** [Redefining Machine Learning with Kotlin | Michal Harakal](https://www.youtube.com/watch?v=uTmCE0SlvSM)

---

### 1115 Reflection is Evil — Jeffrey van Gogh

Jeffrey van Gogh, «språkgeek» hos Google, argumenterte i denne lyntalen for at refleksjon – evnen kjørende JVM- og .NET-kode har til å inspisere og kalle sine egne komponenter – koster ytelse (mindre inlining fra JIT-en), typesikkerhet, sikkerhet (serialisering) og verktøystøtte, og saboterer kodeslankere som Androids R8: Bouncy Castle må for eksempel friholdes med over 240 ProGuard-regler for ikke å krasje ved kjøring. Han rangerte dynamisk klasselasting som «rent ondt», var streng også mot testrammeverk og mocking-bibliotek som bryter seg inn i privat kode, men lot debugging (betingede breakpoints via ekspresjonsevaluatoren) og bakoverkompatible workarounds slippe unna. Som alternativer viste han fram verktøykassen som allerede finnes: KSP og Java-annotation-processors ved compile-time, tekstbaserte kodegeneratorer, bytekode-omskriving og Kotlin compiler plugins som endrer AST-en og får IDE-integrasjon på kjøpet – samt embedded DSL-er, rene biblioteker eller nye språkegenskaper (som Compose) når problemet virkelig fortjener det. Poenget: refleksjon er ikke ond i seg selv, men blir det når den er den eneste hammeren i verktøykassa.

**Tags:** `Lyntale` · `JVM` · `Compiler plugin` · `Compile-time` · `Språkdesign`

**📹** [Reflection is Evil | Jeffrey van Gogh](https://www.youtube.com/watch?v=bxpmPZOWJOQ)

---

### 1330 Hot-Reloading Kotlin/Native — Gabriele Pappalardo

Gabriele Pappalardo (JetBrains) fortalte om den eksperimentelle reisen med å få Compose Hot-Reload til å fungere på iOS-simulator uten en JVM, noe som lenge har blitt ansett som umulig på Apples Darwin-plattformer. I stedet for å bygge en egen Kotlin-virtuell maskin utnyttet teamet LLVM ORC v2 for å laste og linke ny kode dynamisk i den kjørende native-prosessen. Han gikk under panseret på nødvendige kompilator-endringer, spesielt split compilation, som skiller ut kompilerte enheter slik at de kan byttes ut individuelt uten å bygge hele appen på nytt. En ny hot-reload runtime-modul håndterer selve utskiftningen, og han viste hvordan tilstand bevares på tvers av endringer i klasseoppsett, funksjonsoppdateringer og re-linking av symboler. Foredraget ga et konkret innblikk i lavnivå-runtime-manipulasjon på Kotlin/Native og pekte fram mot en langt raskere utviklingsopplevelse for KMP-apper på iOS.

**Tags:** `Kotlin/Native` · `iOS` · `Compose` · `Hot reload` · `LLVM` · `Compiler`

**📹** [Hot-Reloading Kotlin/Native | Gabriele Pappalardo](https://www.youtube.com/watch?v=hXDw2cOxnpo)

---

### 1400 Full-Stack Kotlin AI: Powering Compose Multiplatform apps with Koog & MCP — John O'Reilly

John O'Reilly viser hvordan Koog kan brukes som den intelligente kjernen i en Compose Multiplatform-app, og dermed gi ett felles rammeverk for AI-agenter på tvers av Android, iOS og desktop. Han demonstrerer hvordan «local tools» utvider agenten med plattformspesifikke muligheter, slik at den kan utføre reelle handlinger på hver enkelt enhet i tillegg til å svare i chat. Videre kobles agenten mot en MCP-server bygget med Kotlin MCP SDK, noe som lar den samme Koog-agenten benytte eksterne verktøy og datakilder via Model Context Protocol. O'Reilly viser også hvordan man kan bytte mellom skybaserte LLM-er og lokale, on-device-modeller, avhengig av krav til ytelse, kostnad og personvern. Til sammen tegnes et bilde av en full-stack Kotlin-tilnærming der Koog, MCP og Compose Multiplatform utgjør en samlet pakke for å bygge agentdrevne apper med delt kode.

**Tags:** `Koog` · `MCP` · `Compose Multiplatform` · `Full-stack` · `AI-agenter` · `On-device`

**📹** [Full-Stack Kotlin AI: Powering Compose Multiplatform apps with Koog & MCP | John O'Reilly](https://www.youtube.com/watch?v=0ttH-wnawtA)

---

### 1400 What Nobody Told Us About Shipping Kotlin to iOS — Suhyeon (Leah) Kim

Suhyeon (Leah) Kim delte erfaringer fra en to-måneders sprint der teamet skulle skipe en Kotlin Multiplatform-basert iOS-app under sterk tidspress, og hun brukte tre casestudier for å vise hvor Swift-Kotlin-interop faktisk knirker. Første case handlet om native state observation: i stedet for å tvinge Kotlin StateFlow inn i SwiftUI direkte, brøt de flyten ned til Combine-vennlige signaler slik at iOS-siden fikk føles idiomatisk. Andre case var Firebase uten en offisiell KMP-SDK, der de brukte et delegate-mønster slik at Kotlin-koden definerte protokoller mens Swift stod for selve Firebase-kallene og injiserte implementasjonene tilbake. Tredje case var SPM Umbrella Export for binærisolasjon, som lot dem pakke flere Kotlin-frameworks bak én Swift Package uten symbolkollisjoner eller lekkasje av transitive avhengigheter. Til slutt oppsummerte hun et jukseark over vanlige interop-fallgruver – sealed classes som blir NSObject-hierarkier, suspend-funksjoner som krever completion handlers, default arguments som forsvinner, generics som kollapser til Any, og enum-navn som kolliderer med Swift-nøkkelord – med praktiske omgåelser for hver.

**Tags:** `KMP` · `iOS` · `Compose Multiplatform` · `Swift interop` · `Casestudie` · `Firebase`

**📹** [What Nobody Told Us About Shipping Kotlin to iOS | Suhyeon Kim](https://www.youtube.com/watch?v=nziQi2Mg1OY)

---

### 1400 Flow with Exposed: Life Finds a Way — Chantal Loncle

Chantal Loncle bruker en zero-player automaton-simulering som gjennomgående demo for å vise hvordan Exposed takler høy throughput og asynkrone database-operasjoner uten å knele. Simuleringen genererer store mengder tilstandsendringer per tick, og Loncle demonstrerer hvordan man kombinerer Kotlin Flow over Exposed DSL-spørringer for å strømme kontinuerlige state-updates ut til klienten via Coroutines. Underveis viser hun konkrete mønstre for å håndtere backpressure og batch-skriving når Exposed presses på grensen av hva biblioteket kan levere. Etter at simuleringen har generert data, tar hun resultatene inn i Kotlin Notebook og analyserer og visualiserer atferden med DataFrame og Kandy, slik at man ser hvordan automatens «liv» utvikler seg over tid. Til slutt introduserer hun den nye Exposed Gradle-pluginen som forenkler skjema-migrasjoner ved å generere migrasjonsscript direkte fra tabelldefinisjonene i koden.

**Tags:** `Exposed` · `Database` · `Flow` · `Coroutines` · `DataFrame` · `Kandy`

**📹** [Flow with Exposed: Life Finds a Way | Chantal Loncle](https://www.youtube.com/watch?v=Uoe7ClRkbGI)

---

### 1430 The Backend Immune System - Rich Errors, Ktor Observability and Safe Local Remediation — Meike Felicia Hammer

Meike Felicia Hammer presenterte et Kotlin-native motstandsmønster hun kaller «The Backend Immune System», bygd på tre samvirkende lag: rike, typede feil som bærer presis diagnostisk kontekst, Ktor-basert observability som gjør symptomene synlige i sanntid, og lokale deterministiske «agenter» som utfører små, idempotente og strengt avgrensede mikro-utbedringer innenfor selve request-grensen. Hun var eksplisitt på at disse agentene ikke er LLM-drevne – det er ren Kotlin-logikk med forutsigbar oppførsel, klare invarianter og korte tidsvinduer, slik at oppførselen kan testes og revideres på vanlig måte. Demoen kjørte samme tjeneste i to moduser: i «legacy mode» ble en forbigående feil sluppet gjennom som en 500-respons, mens «immune mode» fanget den samme feilen, klassifiserte den via de rike feiltypene og gjennomførte en avgrenset lokal utbedring før svaret forlot serveren. Poenget er at motstandsdyktighet bør bygges inn nær årsaken framfor å overlates til retries lenger ute i kjeden eller til uforutsigbare AI-mekanismer, slik at kjente feilmodi håndteres automatisk uten menneskelig inngripen.

**Tags:** `Backend` · `Ktor` · `Resilience` · `Observability` · `Feilhåndtering` · `Rich errors`

**📹** [The Backend Immune System | Meike Felicia Hammer](https://www.youtube.com/watch?v=oPKxwwppnuA)

---

### 1515 How Kotlin Powers Functional Design: MCP Edition — David Denton

David Denton fra http4k viste hvordan Kotlin og funksjonell design gir en langt enklere vei til MCP-servere enn de offisielle SDK-ene, som han kritiserer for tung bruk av refleksjon, tett kobling mellom protokoll og transport (spesielt stdio som sammenfletter klient- og server-runtime) og feil som først dukker opp i kjøretid. I stedet bygger http4k videre på sine eksisterende funksjonelle prinsipper: klar separasjon mellom protokoll og transport, kapabiliteter modellert som rene funksjoner (for eksempel `typealias ToolHandler = (ToolRequest) -> ToolResponse`), og full in-memory-testing uten porter eller nettverk. Ved å gjenbruke http4k sine byggeklosser for OAuth, Lenses og JSON-RPC får man kompileringstidssikkerhet på tvers av verktøy, ressurser og prompts, og MCP blir bare enda et sett med HTTP-håndterere. Denton demonstrerte dette med en spec-kompatibel MCP-server på cirka 50 linjer Kotlin, samt en Wiretap-plugin som gir HTTP-trafikk, OpenTelemetry-spor og sekvensdiagrammer i JUnit-rapporter. Poenget er at Kotlins extension functions og type aliases lar biblioteket eksponere en idiomatisk, funksjonell API der MCP-domenet uttrykkes direkte som funksjonstyper istedenfor annoterte klasser og magisk oppstart.

**Tags:** `MCP` · `http4k` · `Funksjonell` · `Backend` · `API-design` · `Extension functions`

**📹** [How Kotlin Powers Functional Design: MCP Edition | David Denton](https://www.youtube.com/watch?v=Xmkl7Y3lwUk)

---

### 1515 TestBalloon: Kotlin testing is easier (and more fun) than you think — Oliver Okrongli, Bernd Prünster

Oliver Okrongli og Bernd Prünster presenterte TestBalloon, et Kotlin-first testrammeverk bygget rundt en liten, konsis API-flate og en utvidbar DSL i ren Kotlin – uten den vanlige annotasjonsmagien. De viste hvordan hierarkiske testtrær med vilkårlig nesting, uttrykksfulle testnavn og dekoratørkjeder gir god struktur, mens fixtures og parameteriserte/datadrevne tester (med tilhørende addons) dekker oppsett, opprydding og gjentagelser på en idiomatisk måte. En sentral demonstrasjon var full støtte for alle Kotlin-mål i første klasse: gjennom å eksekvere via Wasm/WASI oppnår TestBalloon nestede, samtidige og parallelle tester også på plattformer som mangler native støtte for dette, med korutinekontekst som arves nedover treet. Foredragsholderne viste også hvordan rammeverket gir dyp Gradle-integrasjon og fungerer sømløst sammen med eksisterende assertion-biblioteker, inkludert Kotlin Power-Assert. Til slutt gikk de gjennom JUnit 4- og JUnit 6-interop og en gradvis migreringsvei, slik at eksisterende JVM-prosjekter kan ta i bruk TestBalloon uten å måtte skrive om hele testsuiten på én gang.

**Tags:** `Testing` · `TestBalloon` · `KMP` · `Wasm` · `DSL` · `JUnit`

**📹** [TestBalloon: Kotlin testing is easier (and more fun) than you think | Oliver Okrongli, Bernd Prünster](https://www.youtube.com/watch?v=80ASd_Kt2tw)

---

### 1615 Koin + Kotlin Compiler = ♥️ — Arnaud Giuliani

Arnaud Giuliani presenterte den største endringen i Koin på åtte år: en tett integrasjon med Kotlin-kompilatoren som flytter mesteparten av arbeidet fra kjøretid til kompileringstid. Med en ny kompilator-plugin blir DSL-oppsettet automatisert, slik at utviklerne slipper å skrive og vedlikeholde like mye modul-boilerplate for hånd. Pluginen bygger også forhåndsberegnede avhengighetsindekser, noe som gir merkbart raskere oppstart og redusert overhead i grafoppslag. Samtidig får man ekte kompileringstidssikkerhet – manglende eller sirkulære bindinger avdekkes før appen kjører – uten at det velkjente og lettleste API-et endres. Resultatet er at Koin beholder sin pragmatiske ergonomi, men flytter seg fra ren runtime-DI til en løsning som konkurrerer med kompilator-genererte rammeverk på ytelse og sikkerhet.

**Tags:** `Koin` · `DI` · `Compiler plugin` · `Compile-time` · `Performance`

**📹** [Koin + Kotlin Compiler = ♥️ | Arnaud Giuliani](https://www.youtube.com/watch?v=eBu9i2MYWWM)

---

### 1645 Powering Up Your Assertions — Brian Norman

Brian Norman viser hvordan Power-Assert i Kotlin 2.4 tar et solid steg framover, med direkte respons på tilbakemeldingene fra brukerne. Gradle-konfigurasjonen blir vesentlig enklere å sette opp, feildiagrammene blir mer lesbare og lettere å tolke når en assertion feiler, og integrasjonen med tredjeparts assertion-biblioteker fungerer langt bedre enn før. For biblioteksforfattere introduseres førstepartsstøtte, slik at rammeverk som Kotest og lignende kan levere den samme diagrammerte feilrapporteringen ut av boksen uten ekstra oppsett hos sluttbrukeren. Til slutt gir Norman en smakebit på hva teamet jobber med videre etter 2.4, slik at Power-Assert kan bli en enda mer selvfølgelig del av Kotlin-testing.

**Tags:** `Testing` · `Power-Assert` · `Kotlin 2.4` · `Compiler plugin` · `Diagnostics`

**📹** [Powering Up Your Assertions | Brian Norman](https://www.youtube.com/watch?v=KhT1jYMpkRU)

---

### 1715 Golden Kodee Awards

Avslutningsseremonien på KotlinConf 2026 delte ut de aller første Golden Kodee Community Awards, som hyller fremragende bidragsytere i Kotlin-økosystemet. Prisene ble delt ut i fem kategorier: Creativity til Nicole Terc, Online Presence til Jaewoong Eum, In-Person Presence til Yinlong Liu, Education til Matheus Leandro Ferreira, og Positive Societal Impact til Eeva-Jonna Panula. Vinnerne ble kåret gjennom en kombinasjon av offentlig avstemning og juryvurdering, og markerte en verdig avslutning på konferansen.

**Tags:** `Awards` · `Community` · `Avslutning`

**📹** [Golden Kodee Awards | KotlinConf'26](https://www.youtube.com/watch?v=p88y4pjb8Cg) · Inngår også i [Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I).

---

# Kilder

- [KotlinConf 2026 – offisiell side](https://kotlinconf.com/)
- [KotlinConf 2026 – oversikt over alle foredrag med video-innebygging](https://kotlinconf.com/talks/)
- [Kotlin sin offisielle YouTube-kanal](https://www.youtube.com/@Kotlin) – hovedkilde for videoene
- [KotlinConf'26 Keynote Highlights](https://blog.jetbrains.com/kotlin/2026/05/kotlinconf26-keynote-highlights/)
- [KotlinConf'26 Speakers: In Conversation with Josh Long](https://blog.jetbrains.com/kotlin/2026/03/kotlinconf-26-speakers-in-conversation-with-josh-long/)
- [KotlinConf'26 Speakers: In Conversation With Lena Reinhard](https://blog.jetbrains.com/kotlin/2026/04/kotlinconf-26-speakers-in-conversation-with-lena-reinhard/)
- [Koog på GitHub](https://github.com/JetBrains/koog)
- [Next level Kotlin support in Spring Boot 4](https://spring.io/blog/2025/12/18/next-level-kotlin-support-in-spring-boot-4/)
- [KotlinConf 2026: Talks to Help You Navigate the Schedule](https://blog.jetbrains.com/kotlin/2026/03/kotlinconf-2026-talks-schedule/)
- [Eval-driven development: Build and evaluate reliable AI agents](https://developers.redhat.com/articles/2026/03/23/eval-driven-development-build-evaluate-ai-agents)
- [Context parameters – Kotlin Documentation](https://kotlinlang.org/docs/context-parameters.html)
- [Update on Context Parameters](https://blog.jetbrains.com/kotlin/2025/04/update-on-context-parameters/)
- [Introducing Tracy: The AI Observability Library for Kotlin](https://blog.jetbrains.com/kotlin/2026/03/introducing-tracy-the-ai-observability-library-for-kotlin/)
- [Golden Kodee Community Awards](https://kotlinconf.com/awards/)
- [Kotlin DSLs in 2026: Patterns That Stood the Test of Time](https://jonnyzzz.com/blog/2026/01/19/kotlin-dsl-2026/)
- [Kotlin DSL Is Now the Default for New Gradle Builds](https://blog.gradle.org/kotlin-dsl-is-now-the-default-for-new-gradle-builds)
- [SKaiNET – Multiplatform On Device Deep Learning](https://skainet.sk/)
- [Adding Swift packages as dependencies to KMP modules | Kotlin docs](https://kotlinlang.org/docs/multiplatform/multiplatform-spm-import.html)
- [Interoperability with Swift using Swift export | Kotlin Documentation](https://kotlinlang.org/docs/native-swift-export.html)
- [KEEP-485: Local Lifetimes](https://github.com/Kotlin/KEEP/blob/main/proposals/lifetimes.md)
