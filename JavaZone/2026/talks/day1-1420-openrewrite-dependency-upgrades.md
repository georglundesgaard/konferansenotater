# Managing the chaos: Automating internal dependency upgrades with OpenRewrite

*Dag 1, 2. september 2026 · kl 14:20 · Jago de Vreede · 📋 [i programmet](../program.md#d1-1420) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/66e04b5d-bc02-433c-ab37-f750622a28bb)*

Jago de Vreede beskriver et gjenkjennelig innersource-problem: 30+ delte biblioteker brukt av dusinvis av nedstrøms applikasjoner, der versjonsbumper alene ikke holder når API-er brytes eller konfigurasjon må migreres. Dependabot oppdaterer avhengigheter, men kan ikke refaktorere kode – så utviklere leser changelogger, jager kompileringsfeil og gjør de samme fiksene i repo etter repo.

Løsningen er OpenRewrite: oppgraderingsoppskrifter som følger med biblioteket, slik at breaking changes blir eksplisitte og migreringen automatiseres på tvers av alle konsumentene.

*(Sammendrag basert på programomtalen – oppdateres via /berik-foredrag når opptaket er publisert.)*

**Tags:** `OpenRewrite` · `Build tools` · `Maven` · `Tooling`

**📹** [Managing the chaos – Jago de Vreede](https://vimeo.com/1223419239)

*[← JavaZone 2026](../README.md)*
