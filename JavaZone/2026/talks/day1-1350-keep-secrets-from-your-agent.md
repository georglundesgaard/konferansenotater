# How to Keep Secrets from your Agent

*Dag 1, 2. september 2026 · kl 13:50 · Nikolai Norman Andersen · 📋 [i programmet](../program.md#d1-1300) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/c14b5db1-9c44-4258-a39d-70aadfb2c2e9)*

Andersen fra Variant tok utgangspunkt i et dilemma: AI-agenter blir mest nyttige når de kan bruke hemmeligheter – tokens, klientlegitimasjon, databasepassord – men siden modellene kjører på «noen andres datamaskin», bør plaintext-hemmeligheter aldri havne i konteksten. Han argumenterte for å behandle modell- og harness-leverandøren mentalt som en skyleverandør med databehandleravtale, og advarte samtidig mot skygge-IT der ansatte tar i bruk private AI-verktøy utenfor bedriftens kontroll. MCP-servere løser deler av problemet via OAuth, men er som en restaurantmeny med forhåndsdefinerte retter – han vil heller beholde friheten i shellen.

Løsningen hans bygger på SOPS (CNCF-verktøy med nøkkelhåndtering via KMS, f.eks. Azure Key Vault og Entra ID), som krypterer verdiene i filer sjekket inn i Git og kan dekryptere og sende hemmeligheter videre som miljøvariabler, filer eller pipes – uten at de noensinne vises i terminalen. Kombinert med en skill som instruerer agenten i sikker hemmelighetshåndtering, pluss auto-godkjenning som blokkerer kommandoer som ville printet nøkler, skriver agenten i praksis «MCP-verktøy på sparket» og bruker hemmelighetene uten å se dem – og motsto alle forsøkene hans på å lure dem ut. Han understreket likevel at dette ikke er idiotsikkert: agenten opererer fortsatt som deg med dine tilganger, så minst mulig privilegier gjelder fortsatt.

**Tags:** `Lyntale` · `AI-agenter` · `Sikkerhet` · `Tooling`

**📹** [How to Keep Secrets from your Agent – Nikolai Norman Andersen](https://vimeo.com/1223407333)

*[← JavaZone 2026](../README.md)*
