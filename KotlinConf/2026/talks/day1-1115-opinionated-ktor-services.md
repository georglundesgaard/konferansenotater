# Opinionated Ktor Services

*[← KotlinConf 2026](../README.md) · Dag 1, 21. mai 2026 · kl 11:15 · Simon Vergauwen*

Simon Vergauwen tar utgangspunkt i at Ktor bevisst er et lite meningssterkt rammeverk – kjernen er coroutines, et plugin-system og modulfunksjoner – og bruker økten til å legge sine egne meninger oppå denne fleksible grunnmuren. Han argumenterer for å strukturere en Ktor-tjeneste rundt små, utskiftbare `Application`-moduler som er extension-funksjoner, kombinert med eksplisitt dependency injection (den nye Ktor 3.2 DI-pluginen, eller Koin/Kodein), slik at man kan bytte ut infrastruktur og lastes moduler forskjellig i test og produksjon. For feilhåndtering anbefaler han typede feil via Arrow sin Raise-DSL i stedet for kastede exceptions, slik at forretningsfeil blir en del av signaturen og kan mappes eksplisitt til HTTP-statuskoder i rute-laget. Han viser en domenesentrert lagdeling der ruter er tynne, tjenester og repositories holder logikken, og persistens gjøres med SqlDelight og KotlinX Serialization; strukturert samtidighet fra coroutines brukes samtidig til å håndtere ressurslivssyklus og graceful shutdown. Testing baseres på TestContainers og at man kan mocke enkeltavhengigheter uten å røre resten av grafen. Hovedbudskapet er at en Ktor-utvikler bør velge sitt eget «meningssett» tidlig – modulær DI, typede feil og en tydelig domenekjerne – slik at tjenesten forblir enkel å teste, refaktorere og skalere når den vokser.

**Notater fra konferansen:**
- Greit foredrag, men ikke spesielt interessant

**Tags:** `Ktor` · `Backend` · `Arkitektur` · `Arrow` · `Feilhåndtering` · `DDD`

**📹** [Opinionated Ktor Services – Simon Vergauwen](https://www.youtube.com/watch?v=JOZFZ__3M7Q)
