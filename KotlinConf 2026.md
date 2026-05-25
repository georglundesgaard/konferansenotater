# KotlinConf 2026

> **Om videoene:** Konferansen ble ferdig 22. mai 2026. Enkeltvideoer publiseres fortløpende på [Kotlin sin offisielle YouTube-kanal](https://www.youtube.com/@Kotlin) i løpet av de neste 1–2 månedene. Foreløpig (per 25. mai 2026) ligger åpnings-keynoten og Day 2-livestreamen ute; jeg legger inn lenker til individuelle videoer under hvert foredrag når de dukker opp.

## May 21

**📹 Live-stream / opptak fra hovedsal:** Day 1 / Keynote-rommet ble streamet; opptak forventes på Kotlin-kanalen.

* **0900 Opening Keynote**
  Åpningskeynoten i München presenterte de store linjene for Kotlin-økosystemet det neste året. Sjefsspråkdesigner Michail Zarečenskij ga en forhåndstitt på Kotlin 2.4.0 med fokus på tryggere og mer ergonomisk kode, og introduserte en ny 18-måneders sikkerhetspolicy for standardbiblioteket. Mye av tiden gikk til AI-drevet utvikling: JetBrains er medledere for den åpne standarden Agent Client Protocol (ACP), Junie-agenten har fått dedikert Android-støtte, og Vadim Briliantov annonserte den stabile 1.0-utgivelsen av Koog. Det overordnede budskapet var at Kotlin har vokst fra et språk til et komplett økosystem for backend, mobil, web, AI og multiplattform.
  📹 [Keynote | KotlinConf '26](https://www.youtube.com/watch?v=MmwBJbzWbV0)

* **1015 Bootiful Kotlin** – *Josh Long*
  Spring-veteranen Josh Long viste hvordan Kotlin og Spring Boot spiller sammen for å gi en renere og mer produktiv utvikleropplevelse. Foredraget gikk dypere inn i hvordan Spring- og Kotlin-teamene har jobbet for å gjøre Spring Boot til en førsteklasses opplevelse for Kotlin-utviklere som vil i produksjon raskere og tryggere – med levende koding i typisk Josh Long-stil.
  📹 2026-utgaven ikke publisert ennå. Forrige utgave for kontekst: [Bootiful Kotlin by Josh Long](https://www.youtube.com/watch?v=etwrkcqIMnk)

* **1115 Opinionated Ktor Services**
  Ktor er bevisst lite opinionert, men de fleste team ender opp med å finne opp de samme strukturene på nytt. Foredraget viste et sett med meninger om hvordan man bygger Ktor-tjenester som forblir modulære, testbare og enkle å utvide – med en pragmatisk arkitektur som dekker modulinndeling, DDD-inspirert domeneisolasjon og Gradle multi-module oppsett som standardrigg for nye prosjekter.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1300 How google.com/search builds on Kotlin coroutines for highly scalable, streaming, concurrent servers**
  En Senior Staff Software Engineer fra Google Search Infra fortalte hvordan Google Søk bruker server-side Kotlin og coroutines for å oppnå asynkrone, streamende kodebaner med lav latens i ekstrem skala. Sentralt sto Qflow – et data-graph-grensesnittspråk som kobler asynkrone definisjoner med Kotlin-forretningslogikk – samt instrumentering av coroutines for latency-sporing og kritisk-vei-analyse.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1400 Local Lifetimes for Kotlin** – *Ross Tate*
  Ross Tate presenterte et designforslag for å gi Kotlin håndhevbar lokalitet: lettvekts-objekter med begrenset levetid som garantert ikke unnslipper sitt tiltenkte scope. Utover lekkasje- og bug-forebygging åpner mekanismen for avanserte kontrollmønstre, effekt-lignende oppførsel og sterk bakoverkompatibilitet – og er designet for å passe rent inn i dagens Kotlin-økosystem.
  📹 Video ikke publisert ennå. Relatert tidligere foredrag: [Revamping and Extending Kotlin's Type System | Ross Tate](https://www.youtube.com/watch?v=3uNpmhHwkuQ)

* **1515 Why Most AI Agents Never Scale? Building Enterprise-Ready AI with Koog** – *Vadim Briliantov*
  Teknisk leder og forfatter av Koog viste hvorfor de fleste AI-agenter aldri kommer seg ut av prototypestadiet, og hvordan Koog løser problemene med idiomatisk Kotlin. Foredraget dekket feiltoleranse med innebygde retries og agent-persistens, intelligent historikkomprimering for å kontrollere token-kostnader, sterkt typede arbeidsflyter, observabilitet via OpenTelemetry og Langfuse, og enterprise-integrasjoner med Spring Boot og Ktor. Samtidig ble Koog 1.0 annonsert som stabil utgivelse.
  📹 Relatert (eldre foredrag av samme taler, til opptaket dukker opp): [Building AI Agents in Kotlin with Koog | Vadim Briliantov](https://www.youtube.com/watch?v=O8WQCrdza8E) · [Fault tolerant AI Agents on the JVM with Koog framework](https://www.youtube.com/watch?v=2l1GBp80CbY)

* **1615 Talking to terminals (and how they talk back)** – *Jake Wharton*
  Jake Wharton tok publikum med under panseret på terminalen – fra ANSI escape-sekvenser og kontrollkoder til moderne TUI-rammeverk i Kotlin. Foredraget viste hvordan man skriver Kotlin-kode som faktisk samhandler med terminalen toveis: tegner UI, leser input og oppfører seg riktig på tvers av plattformer, terminaler og rare edge-cases.
  📹 Video ikke publisert ennå – sjekk Jake Wharton sin [presentations-side](https://jakewharton.com/presentations/) eller Kotlin-kanalen.

* **1715 Robocoders: The [K]agematch**
  En underholdende avslutning på dag én der ulike AI-kodeagenter ble satt opp mot hverandre i en «cage match» (med K for Kotlin). Agentene fikk samme Kotlin-oppgaver og publikum kunne se i sanntid hvordan ulike modeller, prompts og verktøykjeder takler reelle programmeringsutfordringer – like mye en demonstrasjon av status for AI-kodeassistenter som av hvor langt agentene ennå har igjen.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

## May 22

**📹 Live-stream / opptak fra hovedsal:** [KotlinConf'26 – Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I) – inneholder hovedsal-foredragene fra dag 2.

* **0900 We were meant to be** – *Lena Reinhard* (Day 2 Keynote)
  Lederutvikler og tidligere VP of Engineering Lena Reinhard holdt dag 2-keynoten med et menneskelig blikk på tech-bransjen i 2026. Hun adresserte usikkerheten mange føler i AI-tidsalderen – produktivitetsdebatten, hvordan karriereveier endrer seg, og spørsmålet om disse karrierene i det hele tatt vil eksistere som før. Et reflekterende foredrag om teknologi, mennesker, krise og fremtiden, formet gjennom en åpen «work log» i månedene før konferansen.
  📹 Inngår i [Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I) – egen video forventet senere.

* **1015 Dissecting Kotlin: 2026** – *Huyen Tue Dao*
  Ti år etter Kotlin 1.0 fortsetter språket å utvikle seg raskt. Huyen Tue Dao plukket fra hverandre nylige stabile og preview-features, og brukte design og implementasjon som linse for å forstå hvor språket er på vei. Tilhørerne fikk en dypere forståelse av hvordan Kotlin formes – og hvordan denne innsikten kan påvirke koden de selv skriver.
  📹 2026-utgaven ikke publisert ennå. Forrige utgave: [Dissecting Kotlin: Surveying the Latest Stable and Experimental | Huyen Tue Dao (KotlinConf 2025)](https://www.youtube.com/watch?v=sDA28kH6AIc)

* **1115 Idiomatic Kotlin applications with Spring Boot 4**
  Et dypdykk i hvordan man skriver idiomatisk Kotlin oppå Spring Boot 4. Sentralt sto null-safety: JSpecify-annoteringer brukes nå konsekvent på tvers av Spring-porteføljen og oversettes automatisk til Kotlin-nullability, slik at hele rammeverket føles ekte Kotlin-aktig. Foredraget viste også migreringen av den offisielle Spring Boot Kotlin-tutorialen fra Spring Data JPA til Spring Data JDBC for å tillate mer idiomatisk kode, samt bruk av coroutines og virtuelle tråder for å bygge raske og skalerbare APIer uten reaktiv kompleksitet.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1300 Eval-Driven Development: The Fine Line Between Agentic Success and Failure** – *Urs Peter*
  Senior Software Engineer og JetBrains-sertifisert Kotlin-trainer Urs Peter introduserte Eval-Driven Development (EDD) – en engineering-først tilnærming til å gjøre AI-agenter pålitelige. Med Koog som verktøykasse viste han hvordan man tester agenter på flere lag, samler meningsfulle metrikker, oppdager regresjoner, genererer syntetiske testtilfeller med LLM-er og bygger kontinuerlige evalueringssløyfer som hindrer at agentene degraderer stille i produksjon.
  📹 Video ikke publisert ennå – se [Urs Peter på Sessionize](https://sessionize.com/urs-peter/) for tidligere opptak om EDD.

* **1400 Context parameters and API design** – *Alejandro Serrano Mena*
  Alejandro Serrano Mena viste hvordan context parameters – som stabiliseres i Kotlin 2.4.0 – endrer måten vi designer APIer på. Foredraget fokuserte på hvordan featuren lar API-design fokusere på kjernelogikken og holde implisitt kontekst (transaksjoner, logging, scopes, autorisasjon) ute av signaturene, med praktiske eksempler på når det fungerer godt og når man bør holde seg til vanlige parametre.
  📹 Video ikke publisert ennå. Bakgrunn fra samme taler: [Kotlin Context Receivers Explained | Alejandro Serrano Mena](https://www.youtube.com/watch?v=2oiRCYnqhDs)

* **1515 gRPC, Made for Kotlin**
  En presentasjon av den eksperimentelle førsteparts gRPC-støtten i kotlinx-rpc som JetBrains viste fram i keynoten. Foredraget gikk gjennom hvordan gRPC nå føles ekte Kotlin-aktig – med coroutines, Flow for streaming og strukturert samtidighet – i stedet for den genererte Java-stub-følelsen som har vært normalen, og demonstrerte ende-til-ende-flyt mellom Kotlin-klient og Kotlin-server.
  📹 Video ikke publisert ennå – bakgrunn: [kotlinx-rpc gRPC-dokumentasjon](https://kotlin.github.io/kotlinx-rpc/grpc-configuration.html).

* **1545 KotlinLLM: Leveraging AI for Runtime Logic Delegation in Kotlin**
  Et lyntalk om å delegere deler av forretningslogikken til en LLM i runtime, presentert i konteksten av JetBrains sin Tracy-observabilitets-bibliotek og resten av Kotlin AI-stacken. Tankegangen: ikke alle problemer trenger eksplisitt imperativ kode – noen funksjoner kan beskrives med naturlig språk og tolkes av en LLM bak en typesikker Kotlin-fasade, med fallback, caching og observasjon som førsteklasses borgere.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1615 Spec-Driven Development with AI Agents: From High-Level Requirements to Working Software** – *Anton Arhipov*
  Arhipov presenterte "spec-driven development" som en strukturert måte å jobbe med AI-kodeagenter på. Metoden går ut på å starte med høyt-nivå krav, raffinere dem til en utviklingsplan, og bryte planen ned i en sporbar oppgaveliste – alt som artefakter (`requirements.md`, `plan.md`, `tasks.md`) som agenten jobber fra. Et rammeverk for å gjøre AI-koding forutsigbar og reviewbar i stedet for kaotisk.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin). Lysbilder: [Speaker Deck](https://speakerdeck.com/antonarhipov/spec-driven-development-with-ai-agents-from-high-level-requirements-to-working-software-e397ad2e-3484-4bfa-a80b-6c47c593ed11).

---

## Foredrag jeg vil se opptak av

Foredrag jeg gikk glipp av (parallelle spor / kollisjoner) og som jeg vil se når videoene kommer på YouTube.

### May 21

* **1015 A tale of the Gradle DSLs**
  En historisk og praktisk gjennomgang av Gradle sine DSL-er – fra Groovy-arven, via introduksjonen av Kotlin DSL i Gradle 3.0 (2016) og 1.0-stabiliseringen i Gradle 5.0, til at Kotlin DSL nå er default for nye Gradle-builds. Foredraget plukker fra hverandre mønstrene som har stått tidens prøve i Kotlin DSL-økosystemet og hvorfor type-sikker build-konfigurasjon har blitt grunnstammen i moderne JVM-prosjekter.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1015 Tiny Models, Big Impact: On-Device AI for Real Apps**
  En av de 16 AI-foredragene på årets program, denne gangen om små språkmodeller (SLM-er) som kjører fullt og helt på enheten – uten skyavhengighet. Foredraget viser hvordan Kotlin-utviklere kan integrere on-device LLM-er gjennom verktøy som Llama Stack sin Kotlin SDK, hvilke avveininger man må gjøre rundt latency, batteri, modellstørrelse og kvalitet, og hvordan dette spiller sammen med JetBrains sin AI-stack (Koog, Tracy, ACP).
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1045 Run, Kotlin, Run!**
  Et performance-orientert foredrag om hva som faktisk skjer når Kotlin-koden din kjører – på tvers av plattformene Kotlin støtter (JVM, Native, Wasm/JS). Sannsynligvis innom temaer som compile-time kontra runtime-kostnader, hvordan multiplattform-binærer påvirker både kompileringstid og kjøretidsytelse, og praktiske grep for å gjøre Kotlin-prosjekter raskere uten å miste idiomatikken.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1115 Kotlin/Wasm: Finally, the missing piece for a full stack Kotlin webapp!** – *Dan Kim*
  Dan Kim viser hvordan Kotlin/Wasm i beta endelig gjør det praktisk å skrive hele web-stacken i Kotlin. Han bygger en fullstack-app fra topp til bunn med Kotlin/Wasm, Compose Multiplatform, Coroutines, Exposed og Ktor, og diskuterer hvorfor Wasm er den manglende brikken for pikselperfekt frontend. Foredraget er en praktisk introduksjon til hele stacken, inkludert mindre kjente rammeverk som Exposed og Ktor.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1300 Real-World Data Science With Kotlin Notebook** – *Adele Carpenter*
  Adele Carpenter går gjennom en reell data science-arbeidsflyt på et powerlifting-datasett, helt uten å forlate IDE-en. Hun dekker dataforståelse, validering av resultater, henting og manipulering med Postgres og DataFrame, samt visualisering med Kandy-biblioteket. Hovedbudskapet er at Kotlin-økosystemet er modent nok til å konkurrere med Python for praktisk dataanalyse.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1330 SwiftPM support for Kotlin Multiplatform** – *Timofey Solonin*
  Lynforedrag om den nye Swift Package Manager-støtten i Kotlin Multiplatform. Solonin viser hvordan du kan importere SwiftPM-avhengigheter som FirebaseFirestore, Sentry og Google Maps i KMP-koden, konfigurere Xcode-prosjekter og publisere KMP-biblioteker som bruker SwiftPM. Han forklarer også hvordan Swift- og Objective-C-kildefiler gjøres tilgjengelige for Kotlin/Native-kompileringer og linker under panseret.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1400 Codex for Kotlin Engineers** – *Benedict Kerres*
  Kort sesjon om hvordan OpenAI Codex passer godt sammen med Kotlin sitt strenge typesystem, tydelige domenemodeller og testbare struktur når man genererer, refaktorerer og gjennomgår kode. Kerres demonstrerer hvordan man bruker Codex effektivt i en Kotlin-arbeidsflyt. Praktisk innretning mot AI-assistert utvikling for Kotlin-utviklere.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1430 Building AI‑Powered Web Apps in Kotlin/Wasm** – *Zalim Bashorov*
  Bashorov ser på de nye, native AI-API-ene som moderne nettlesere er i ferd med å standardisere, og hvordan man kan bygge fullt klientside-baserte AI-apper uten serverinfrastruktur. Han dekker fordelene (personvern, responsivitet, offline-bruk) og begrensningene ved Web AI, og demonstrerer eksempler som sanntidsoppsummering og oversettelse kjørt rett i nettleseren – alt fra Kotlin/Wasm.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1515 Expedited Shipping: Accelerating iOS Development with KMP at Amazon** – *Jessalyn Wang*
  Wang forteller hvordan Amazon Delivery bruker KMP og deres open-source-rammeverk "App Platform" til å levere apper på tvers av enheter og plattformer for millioner av pakker daglig. Hun dykker spesielt ned i den nye iOS-støtten: SwiftUI-integrasjon, navigasjonsmønstre og hvordan de skalerer utvikling på tvers av hundrevis av utviklere og dusinvis av team. Konkret erfaringsdeling om KMP i stor skala på iOS.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1515 The State of Amper** – *Joffrey Bion*
  Statusoppdatering på JetBrains sitt nye byggesystem Amper. Bion går gjennom det siste årets nyheter som plugins, publisering og IDE-funksjoner, samt et glimt av veien videre. Et must for de som vurderer Amper som alternativ til Gradle.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1515 Compose beyond UI : Display and Print!** – *Salomon Brys*
  Lynforedrag om å bruke Compose til mer enn vanlige skjermer. Brys viser hvordan man kan generere animerte presentasjoner, looping-displays, bilder til sosiale medier og til og med PDF-er og brettspillkort med Compose-toolinget. Et kreativt blikk på Compose som generelt rendrings-rammeverk.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1615 Increasing quality of AI generated Kotlin code** – *Sergei Rybalkin (Meta)*
  Rybalkin fra Meta deler praktiske strategier for å heve kvaliteten på Kotlin-kode generert av AI-modeller, basert på arbeid i store kodebaser. Han dekker vanlige utfordringer, evalueringsmetoder og verktøy som hjelper med å sikre lesbarhet, vedlikeholdbarhet og pålitelighet. Konkret om hvordan man måler og forbedrer AI-generert Kotlin-kode i produksjon.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1615 Swift Export: Where We Stand** – *Pamela Hill-Galloway*
  Statusoppdatering på Swift Export-prosjektet fra JetBrains, som skal erstatte den gamle Objective-C-broen og gi mer idiomatisk Swift-tilgang til delt Kotlin-kode. Hill-Galloway viser kodeeksempler på overgangen, hvilke features som støttes i dag, og hvilke kant-tilfeller som fortsatt mangler arbeid. Målet er at du selv skal kunne vurdere om Swift Export er klar for ditt team.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1645 Can Kotlin Swift Interop Ever Be Perfect?** – *Gleb Lukianets*
  Lukianets dykker ned i de dype semantiske forskjellene mellom Kotlin og Swift, og diskuterer kompromissene disse tvinger fram i designet av Swift Export. Selv om språkene virker like på overflaten, har de fundamentale forskjeller som gjør perfekt interop vanskelig. Et bra teknisk komplement til "Swift Export: Where We Stand"-foredraget.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1715 The Lord of Collection Functions - The Fellowship of Kotlin** – *Ben Kadel*
  Lett, Tolkien-inspirert gjennomgang av Kotlins collection-funksjoner. Kadel viser hvordan funksjoner som `filter`, `map`, `partition`, `flatMap`, `zip`, `groupBy`, `associateWith`, `windowed` og `runningFold` lar deg jobbe deklarativt med Set, Map og List. Målet er å gi tilhørerne et solid funksjonelt verktøysett, blant annet for Advent of Code-utfordringer.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

### May 22

* **1015 Automate upgrading to Kotlin 2 with OpenRewrite** – *Rooz SF, Jonathan Schneider*
  Moderne/OpenRewrite-teamet viser den nye Kotlin 2-støtten i OpenRewrite. Med "recipes" som opererer på Lossless Semantic Trees kan refaktorerings-motoren automatisk håndtere avhengighetsoppgraderinger, API-endringer og stilkonsistens på tvers av store kodebaser. Praktisk relevant for alle som skal oppgradere eldre Kotlin-prosjekter til 2.x uten manuelt arbeid.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1015 Advanced Kotlin Native Integration** – *Tadeas Kriz (Touchlab)*
  Kriz tar for seg en kjent begrensning i Kotlin/Native: at det egentlig bare skal være én KMP-native-binærfil per app. Han diskuterer konsekvensene av å inkludere flere KMP-binærfiler, viser måter å splitte kompileringen i mindre biter, og foreslår løsninger for større prosjekter med komplekse repo-strukturer. Avansert innhold rettet mot KMP-team som har vokst forbi standard-oppsettet.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1015 10 Gradle Best Practices Every Kotlin Developer Should Know** – *Stefan Wolf*
  Lynforedrag med 10 viktige Gradle-praksiser basert på offisielle anbefalinger fra JetBrains, Google og Gradle-teamene. Wolf dekker prosjektstruktur, trygg avhengighetshåndtering, vedlikeholdbar build-logikk, vanlige konfigurasjonsfeller og CI-optimalisering – pluss en sniktitt på IntelliJ IDEAs sanntids-build-inspeksjoner. Greit oppslagsverk for både Android-, backend- og multiplatform-utviklere.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1045 A First Look at the Kotlin Ecosystem Plugin for Declarative Gradle** – *Marcin Mycek*
  Mycek presenterer en tidlig prototyp av Kotlin Ecosystem Plugin, bygget på Declarative Gradle. Foredraget viser hvordan den deklarative og opinionated tilnærmingen gjør det mulig å radikalt forenkle Kotlin- og Multiplatform-build-konsepter som tidligere var smertefulle, samt resonnementet bak de viktigste endringene. Relevant for de som følger med på fremtiden for Gradle-builds i Kotlin-verdenen.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1115 How I Learned to Stop Worrying and Love Value Semantics (in Kotlin)** – *Marat Akhin*
  Akhin forklarer hva value semantics faktisk er, og hvorfor det er nyttig i Kotlin – kontrastert med reference semantics (identitet vs likhet, mutasjon vs kopi). Han kobler dette til kjente Kotlin-features som `data class.copy()`, kommende value classes og immutable collections, og viser med kodeeksempler og enkle benchmarks at value-orientert design både er praktisk og ytelses-akseptabelt på JVM. Avveiningene rundt allokering og API-design dekkes konkret.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1115 Redefining Machine Learning with Kotlin: A Device-First Approach to AI** – *Michal Harakal*
  Harakal introduserer SKaiNET, et nytt open-source ML-rammeverk skrevet fra bunnen av i Kotlin Multiplatform. Han viser hvordan man definerer nevrale nettverk med en typesikker DSL, kompilerer dem til compute-grafer, og kjører lette modeller som konvolusjonsnett og kompakte LLM-er fullstendig offline på enheten. Fokus er på personvern, lav latency og hvordan Kotlins coroutines, typesikkerhet og multiplatform-støtte muliggjør on-device-AI.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1115 Reflection is Evil** – *Jeffrey van Gogh*
  Lynforedrag der Jeffrey van Gogh argumenterer for at refleksjon – som finnes i JVM, .NET og andre høynivå-plattformer – ofte er problematisk. Han presenterer caser for hvorfor man bør unngå refleksjon i moderne Kotlin-kode, og hvilke alternativer som finnes (typisk compiler plugins, code generation, value semantics). Provokativ tittel, men hovedbudskapet handler om compile-time-sikkerhet og forutsigbarhet.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1330 Hot-Reloading Kotlin/Native** – *Gabriele Pappalardo*
  Pappalardo dokumenterer den eksperimentelle reisen med å få Compose Hot-Reload til å fungere på iOS-simulatorer uten en JVM. I stedet for å bygge en egen Kotlin Virtual Machine utnytter teamet LLVM ORC v2 for å gjøre hot-reload direkte på Darwin. Han går inn på compiler-endringer som split compilation, det nye hot-reload-runtime-moduletet, og hvordan state preservation og endringer i class layout håndteres.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1400 Full-Stack Kotlin AI: Powering Compose Multiplatform apps with Koog & MCP** – *John O'Reilly*
  O'Reilly viser hvordan Koog (JetBrains sitt AI agent-rammeverk) kan utgjøre den intelligente kjernen i en Compose Multiplatform-app. Han demonstrerer bruk av "local tools" som gir agenten ekstra capabilities på Android, iOS og desktop, kobling til MCP-servere via Kotlin MCP SDK, og bruk av både skybaserte og lokale on-device LLM-er. Praktisk demo av en full-stack Kotlin AI-arkitektur.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1400 What Nobody Told Us About Shipping Kotlin to iOS** – *Suhyeon (Leah) Kim*
  Tre Android-utviklere uten iOS-erfaring fikk to måneder på å levere en intern app til begge plattformene med Compose Multiplatform – UI-laget gikk bra, men grensesnittet mot Swift var en annen historie. Kim deler tre konkrete case studies etter et år i produksjon: native state-observasjon med StateFlow som bro, delegate-mønster for Firebase (som mangler KMP SDK), og SPM Umbrella Export som fiks for binary isolation. Inkluderer en Swift-Kotlin interop-pitfall-cheatsheet.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1400 Flow with Exposed: Life Finds a Way** – *Chantal Loncle*
  Loncle bruker en zero-player automaton-simulering til å vise hvordan Exposed (database-tilgangsbibliotek) takler høy throughput og asynkrone database-operasjoner. Hun kombinerer Kotlin Flow over Exposed DSL-spørringer for å observere kontinuerlige state-updates, og bruker DataFrame og Kandy til analyse og visualisering. Til slutt vises den nye Exposed Gradle-pluginen for å forenkle database-migrasjoner.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1430 The Backend Immune System - Rich Errors, Ktor Observability and Safe Local Remediation** – *Meike Felicia Hammer*
  Hammer presenterer "Backend Immune System" – et Kotlin-nativt resilience-mønster basert på rich errors, Ktor-observability og lokale, deterministiske agenter som utfører trygg automatisk reparasjon innenfor request-grensen. Eksplisitt ikke en LLM eller self-healing-infrastruktur: agenten gjør kun avgrensede, idempotente mikro-remediations og eskalerer ved behov. Demoen sammenligner legacy-modus, immune-modus uten verifisering og full immune-modus med verifisering.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1515 How Kotlin Powers Functional Design: MCP Edition** – *David Denton*
  Denton (http4k) argumenterer for at MCP SDK-er gjentar feilene fra HTTP-rammeverk i 2015 – refleksjon, tett kobling til transport, runtime-feil for type-mismatcher. Han viser hva som skjer når man bruker http4k sine funksjonelle prinsipper på MCP: lag-deling mellom protokoll og transport, funksjonelle capabilities, in-memory-testing, compile-time-sikkerhet og gjenbruk av komponenter som OAuth, Lenses og JSON-RPC. Et godt forsvar for funksjonell, komposisjonell design med Kotlins extension functions og type aliases.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1515 TestBalloon: Kotlin testing is easier (and more fun) than you think** – *Oliver Okrongli, Bernd Prünster*
  Introduksjon til TestBalloon, et nytt Kotlin-test-rammeverk med liten API-flate, hierarkisk teststruktur og en utvidbar DSL. Foredragsholderne viser parameteriserte tester, data-driven testing, fixtures, og hvordan TestBalloon støtter alle plattformer opp til Wasm/WASI – inkludert nestede, samtidige og parallelle tester på plattformer som ikke har native støtte for det. Dekker også samspill med JUnit 4/6 og hvordan migrere eksisterende testsuiter.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1615 Koin + Kotlin Compiler = ♥️** – *Arnaud Giuliani*
  Giuliani presenterer Koins største endring på åtte år: integrasjon med Kotlin Compiler. Det tunge arbeidet flyttes til kompileringstid, med automatisert DSL, forhåndsberegnede avhengighetsindekser og ekte compile-time-sikkerhet. Samme enkelhet, men med vesentlig bedre garantier og ytelse.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1645 Powering Up Your Assertions** – *Brian Norman*
  Norman viser de store endringene i Power-Assert som kommer med Kotlin 2.4: enklere Gradle-konfigurasjon, tydeligere meldingsdiagrammer og bedre bibliotek-integrasjon. Forfattere av assertion-biblioteker får se hvordan de kan legge til førstepartsstøtte for Power-Assert i sine biblioteker, slik at alle får samme gode out-of-the-box-opplevelse. Avslutter med en sniktitt på hva som kommer videre.
  📹 Video ikke publisert ennå – se [Kotlin-kanalen](https://www.youtube.com/@Kotlin).

* **1715 Golden Kodee Awards**
  Den offisielle avslutningen på KotlinConf 2026 med utdeling av Golden Kodee Community Awards. Vinnere ble kåret i fem kategorier – Creativity, Online Presence, In-Person Presence, Education og Positive Societal Impact – som hyllest til folk og communities som har bidratt til Kotlin-økosystemet gjennom kunnskapsdeling, eventarrangement og inspirasjon.
  📹 Inngår i [Day 2 Livestream](https://www.youtube.com/watch?v=S3CjlmpsC0I).

---

## Kilder

- [KotlinConf 2026 – offisiell side](https://kotlinconf.com/)
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
