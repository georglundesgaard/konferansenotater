# Managing the chaos: Automating internal dependency upgrades with OpenRewrite

*Dag 1, 2. september 2026 · kl 14:20 · Jago de Vreede · 📋 [i programmet](../program.md#d1-1420) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/66e04b5d-bc02-433c-ab37-f750622a28bb)*

De Vreede fra TenneT, den nederlandske operatøren av høyspentnettet, beskrev utfordringen med å vedlikeholde rundt 60 applikasjoner og 50 interne biblioteker fordelt på 10 team – der ett API-brudd i et mye brukt bibliotek (som deres outbox-bibliotek, brukt i 63 applikasjoner) kan tvinge alle teamene til å gjøre den samme manuelle oppgraderingen. Første grep var rapporter over hvem som vedlikeholder og bruker hvert bibliotek, pluss disiplin rundt semantisk versjonering – en publikumsquiz viste hvor mye tolkningsrom som finnes, og han har laget en Maven-plugin som sammenligner mot forrige publiserte versjon og sjekker at versjonsnummeret stemmer med de faktiske API-endringene.

Hoveddelen var en live demo av OpenRewrite: ferdige recipes som «equals avoid null» og oppgradering til Java 25 (inkludert omskriving til switch pattern matching), dry run som produserer en Git-patch CI/CD-pipelinen kan applisere automatisk, og en egen «code style»-kjøring med recipes som fjerner ubrukte imports, innfører var og bytter Collectors.toList med toList – slik slipper man stildiskusjoner i pull requests. Deretter bygde han en egen YAML-recipe for å migrere konsumenter av et internt bibliotek etter en typo-fiks, og viste at recipes bør ligge i en egen Maven-modul i bibliotekets multi-modul-prosjekt, slik at hver bibliotekrelease automatisk får tilhørende migreringsrecipes. Renovate/Dependabot settes til å ignorere selve biblioteket og bare oppgradere rewrite-avhengigheten.

Til slutt skrev han en kodebasert recipe (en Java-visitor som renamer variabler) ved først å definere OpenRewrite-tester med før/etter-kode, og lot så en relativt liten AI-modell (Qwen) implementere selve recipen i ett forsøk mot testene. Rådet hans: lag recipes ikke bare ved major-endringer, men også når du deprecater metoder, og dekk både YAML- og properties-konfigurasjon. Versjonsmigreringer kjedes sekvensielt (v1→v2→v3), og applikasjoner oppgraderer aldri biblioteket manuelt – kun recipe-versjonen.

**Tags:** `OpenRewrite` · `Build tools` · `Maven` · `Tooling` · `Live demo` · `Casestudie`

**📹** [Managing the chaos – Jago de Vreede](https://vimeo.com/1223419239)

*[← JavaZone 2026](../README.md)*
