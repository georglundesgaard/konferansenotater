# KotlinConf 2026

## May 21

* **0900 Opening Keynote**
  Åpningskeynoten i München presenterte de store linjene for Kotlin-økosystemet det neste året. Sjefsspråkdesigner Michail Zarečenskij ga en forhåndstitt på Kotlin 2.4.0 med fokus på tryggere og mer ergonomisk kode, og introduserte en ny 18-måneders sikkerhetspolicy for standardbiblioteket. Mye av tiden gikk til AI-drevet utvikling: JetBrains er medledere for den åpne standarden Agent Client Protocol (ACP), Junie-agenten har fått dedikert Android-støtte, og Vadim Briliantov annonserte den stabile 1.0-utgivelsen av Koog. Det overordnede budskapet var at Kotlin har vokst fra et språk til et komplett økosystem for backend, mobil, web, AI og multiplattform.

* **1015 Bootiful Kotlin** – *Josh Long*
  Spring-veteranen Josh Long viste hvordan Kotlin og Spring Boot spiller sammen for å gi en renere og mer produktiv utvikleropplevelse. Foredraget gikk dypere inn i hvordan Spring- og Kotlin-teamene har jobbet for å gjøre Spring Boot til en førsteklasses opplevelse for Kotlin-utviklere som vil i produksjon raskere og tryggere – med levende koding i typisk Josh Long-stil.

* **1115 Opinionated Ktor Services**
  Ktor er bevisst lite opinionert, men de fleste team ender opp med å finne opp de samme strukturene på nytt. Foredraget viste et sett med meninger om hvordan man bygger Ktor-tjenester som forblir modulære, testbare og enkle å utvide – med en pragmatisk arkitektur som dekker modulinndeling, DDD-inspirert domeneisolasjon og Gradle multi-module oppsett som standardrigg for nye prosjekter.

* **1300 How google.com/search builds on Kotlin coroutines for highly scalable, streaming, concurrent servers**
  En Senior Staff Software Engineer fra Google Search Infra fortalte hvordan Google Søk bruker server-side Kotlin og coroutines for å oppnå asynkrone, streamende kodebaner med lav latens i ekstrem skala. Sentralt sto Qflow – et data-graph-grensesnittspråk som kobler asynkrone definisjoner med Kotlin-forretningslogikk – samt instrumentering av coroutines for latency-sporing og kritisk-vei-analyse.

* **1400 Local Lifetimes for Kotlin** – *Ross Tate*
  Ross Tate presenterte et designforslag for å gi Kotlin håndhevbar lokalitet: lettvekts-objekter med begrenset levetid som garantert ikke unnslipper sitt tiltenkte scope. Utover lekkasje- og bug-forebygging åpner mekanismen for avanserte kontrollmønstre, effekt-lignende oppførsel og sterk bakoverkompatibilitet – og er designet for å passe rent inn i dagens Kotlin-økosystem.

* **1515 Why Most AI Agents Never Scale? Building Enterprise-Ready AI with Koog** – *Vadim Briliantov*
  Teknisk leder og forfatter av Koog viste hvorfor de fleste AI-agenter aldri kommer seg ut av prototypestadiet, og hvordan Koog løser problemene med idiomatisk Kotlin. Foredraget dekket feiltoleranse med innebygde retries og agent-persistens, intelligent historikkomprimering for å kontrollere token-kostnader, sterkt typede arbeidsflyter, observabilitet via OpenTelemetry og Langfuse, og enterprise-integrasjoner med Spring Boot og Ktor. Samtidig ble Koog 1.0 annonsert som stabil utgivelse.

* **1615 Talking to terminals (and how they talk back)** – *Jake Wharton*
  Jake Wharton tok publikum med under panseret på terminalen – fra ANSI escape-sekvenser og kontrollkoder til moderne TUI-rammeverk i Kotlin. Foredraget viste hvordan man skriver Kotlin-kode som faktisk samhandler med terminalen toveis: tegner UI, leser input og oppfører seg riktig på tvers av plattformer, terminaler og rare edge-cases.

* **1715 Robocoders: The [K]agematch**
  En underholdende avslutning på dag én der ulike AI-kodeagenter ble satt opp mot hverandre i en «cage match» (med K for Kotlin). Agentene fikk samme Kotlin-oppgaver og publikum kunne se i sanntid hvordan ulike modeller, prompts og verktøykjeder takler reelle programmeringsutfordringer – like mye en demonstrasjon av status for AI-kodeassistenter som av hvor langt agentene ennå har igjen.

## May 22

* **We were meant to be** – *Lena Reinhard* (Day 2 Keynote)
  Lederutvikler og tidligere VP of Engineering Lena Reinhard holdt dag 2-keynoten med et menneskelig blikk på tech-bransjen i 2026. Hun adresserte usikkerheten mange føler i AI-tidsalderen – produktivitetsdebatten, hvordan karriereveier endrer seg, og spørsmålet om disse karrierene i det hele tatt vil eksistere som før. Et reflekterende foredrag om teknologi, mennesker, krise og fremtiden, formet gjennom en åpen «work log» i månedene før konferansen.

* **Dissecting Kotlin: 2026** – *Huyen Tue Dao*
  Ti år etter Kotlin 1.0 fortsetter språket å utvikle seg raskt. Huyen Tue Dao plukket fra hverandre nylige stabile og preview-features, og brukte design og implementasjon som linse for å forstå hvor språket er på vei. Tilhørerne fikk en dypere forståelse av hvordan Kotlin formes – og hvordan denne innsikten kan påvirke koden de selv skriver.

* **Idiomatic Kotlin applications with Spring Boot 4**
  Et dypdykk i hvordan man skriver idiomatisk Kotlin oppå Spring Boot 4. Sentralt sto null-safety: JSpecify-annoteringer brukes nå konsekvent på tvers av Spring-porteføljen og oversettes automatisk til Kotlin-nullability, slik at hele rammeverket føles ekte Kotlin-aktig. Foredraget viste også migreringen av den offisielle Spring Boot Kotlin-tutorialen fra Spring Data JPA til Spring Data JDBC for å tillate mer idiomatisk kode, samt bruk av coroutines og virtuelle tråder for å bygge raske og skalerbare APIer uten reaktiv kompleksitet.

---

## Kilder

- [KotlinConf 2026 – offisiell side](https://kotlinconf.com/)
- [KotlinConf'26 Keynote Highlights](https://blog.jetbrains.com/kotlin/2026/05/kotlinconf26-keynote-highlights/)
- [KotlinConf'26 Speakers: In Conversation with Josh Long](https://blog.jetbrains.com/kotlin/2026/03/kotlinconf-26-speakers-in-conversation-with-josh-long/)
- [KotlinConf'26 Speakers: In Conversation With Lena Reinhard](https://blog.jetbrains.com/kotlin/2026/04/kotlinconf-26-speakers-in-conversation-with-lena-reinhard/)
- [Koog på GitHub](https://github.com/JetBrains/koog)
- [Next level Kotlin support in Spring Boot 4](https://spring.io/blog/2025/12/18/next-level-kotlin-support-in-spring-boot-4/)
- [KotlinConf 2026: Talks to Help You Navigate the Schedule](https://blog.jetbrains.com/kotlin/2026/03/kotlinconf-2026-talks-schedule/)
