# Opinionated Ktor Services

*Dag 1, 21. mai 2026 · kl 11:15 · Simon Vergauwen · 📋 [i programmet](../program.md#d1-1115) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1087289/)*

Simon Vergauwen tar utgangspunkt i at Ktor bevisst er et lite meningssterkt rammeverk – kjernen er coroutines, et plugin-system og modulfunksjoner – og bruker økten til å legge sine egne meninger oppå denne fleksible grunnmuren. Han argumenterer for å strukturere en Ktor-tjeneste rundt små, utskiftbare `Application`-moduler som er extension-funksjoner, kombinert med eksplisitt dependency injection (håndkodet DI som førstevalg, med Metro eller Koin som alternativer med kompileringstidssjekker), slik at man kan bytte ut infrastruktur og laste moduler forskjellig i test og produksjon.

For feilhåndtering anbefaler han å unngå exceptions for domenefeil og heller returnere eksplisitte verdier fra tjenestelaget – i dag nullable typer eller sealed interfaces, med Kotlins kommende rich errors som et lovende alternativ – som mappes eksplisitt til HTTP-statuskoder i rutelaget. Han viser en domenesentrert lagdeling der ruter er tynne og tjenester og repositories holder logikken; strukturert samtidighet fra coroutines brukes samtidig til å håndtere ressurslivssyklus og graceful shutdown, med en påminnelse om alltid å sette dispatcher eksplisitt, siden Ktor-applikasjonen ikke har noen som standard. Testing baseres på å gjenbruke samme app-funksjon med en test-avhengighetsgraf, TestContainers for produksjonslikhet – og stubs fremfor mocks, som han eksplisitt unngår. En stor del av økten vies dessuten sikkerhet og drift: JWT-validering mot en OpenID-provider med JWK-nøkkelhenting, OAuth-loginflyt med tjenerside-sesjoner, og deployment via Ktor Gradle-pluginens Docker-støtte bygget på Jib, inkludert OpenTelemetry-agent for automatisk instrumentering.

Hovedbudskapet er at en Ktor-utvikler bør velge sitt eget «meningssett» tidlig – modulær DI, typede feil og en tydelig domenekjerne – slik at tjenesten forblir enkel å teste, refaktorere og skalere når den vokser. For min del traff temaet ikke helt denne gangen – solid, praktisk Ktor-håndverk, men mest relevant om man bygger Ktor-tjenester i det daglige.

**Tags:** `Ktor` · `Backend` · `Arkitektur` · `Feilhåndtering` · `DDD`

**📹** [Opinionated Ktor Services – Simon Vergauwen](https://www.youtube.com/watch?v=JOZFZ__3M7Q)

*[← 1015 Bootiful Kotlin](day1-1015-bootiful-kotlin.md) · [1300 Google Search-coroutines →](day1-1300-google-search-coroutines.md)*
