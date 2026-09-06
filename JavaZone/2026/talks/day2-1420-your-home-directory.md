# You're absolutely right, it was your home directory!

*Dag 2, 3. september 2026 · kl 14:20 · Oleg Šelajev · 📋 [i programmet](../program.md#d2-1420) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/e92e66b5-4ba1-4643-a3a8-d0f22b9f1b32)*

Oleg Šelajev fra Docker tar utgangspunkt i ferske havarier – som agenten som slettet en utviklers hjemmekatalog på 800 GB mens den skulle teste en sandkasse den selv hadde skrevet – for å vise hvorfor AI-agenter på utviklermaskiner er et sikkerhetsproblem. Mer autonomi gir mer produktivitet, men agenter kombinerer tilgang til private data, eksponering for ukontrollert eksternt innhold og evne til å kommunisere utad – den «dødelige trifektaen» som gjør prompt injection farlig. Han demonstrerer at instruksjonsbaserte guardrails ikke holder: agenter omgår kommandoblokkeringer via bash-triks, og i hans eget eksperiment nektet agenten å kjøre et sikkerhetssensitivt skript helt til én /clear-kommando tømte konteksten – da kjørte den villig en full opptelling av SSH-nøkler, tokens og shell-historikk.

Konklusjonen er at grensene må være harde, og løsningen han presenterer er Dockers sbx: et gratis verktøy som kjører agenter (Claude, Codex, OpenCode, Antigravity m.fl.) i en microVM med isolert filsystem, nettverksproxy med allow-lister og secrets-injeksjon der agenten bare ser plassholderverdier mens den ekte nøkkelen settes inn av proxyen på verten. «Kits» er et deklarativt plugin-system (YAML) som gjør sandkassene brukbare i praksis – installer JDK/Maven, åpne hull mot Maven Central, konfigurer credentials – og sbx env komponerer flere kits à la Docker Compose; kits kan pakkes som OCI-artefakter og deles, og sbx støttes nå også som runtime i GitHubs agentiske workflows.

Han er ærlig på begrensningene: sandkasser vil alltid tape mot «ingen sandkasse» på bekvemmelighet, og applikasjonsnivå-angrep (agenten sender en e-post med hemmeligheter) stoppes ikke av infrastrukturisolasjon – men poenget er å begrense skaderadiusen med minste privilegium, slik vi alltid har gjort med vanlig programvare. Som en illustrasjon av at data er kode la han til og med inn en muntlig instruksjon i selve foredraget, rettet mot AI-agenter som senere leser transkripsjonen.

**Tags:** `AI-agenter` · `Sikkerhet` · `Produktivitet` · `Tooling` · `Live demo`

**📹** [You're absolutely right, it was your home directory! – Oleg Šelajev](https://vimeo.com/1223707059)

*[← JavaZone 2026](../README.md)*
