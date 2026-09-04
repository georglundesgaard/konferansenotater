# Bootiful Spring Boot 4

*Dag 1, 2. september 2026 · kl 11:40 · Josh Long · 📋 [i programmet](../program.md#d1-1140) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/29c54f57-6378-4665-8737-522f944c657d)*

Long åpnet med en alvorlig oppfordring: AI-modeller har utløst en flom av CVE-funn i åpen kildekode – Spring har gått fra rundt 1,5 CVE-er i måneden til en jevn strøm – og det viktigste publikum kan gjøre er å oppgradere til Spring Boot 4 umiddelbart og etablere en rask vei til produksjon slik at sikkerhetsfikser kan rulles ut på timer, ikke måneder. Selv lavgraderte sårbarheter kan kjedes sammen på tvers av lag til alvorlige angrep.

Resten var live-koding av en «adoptions»-tjeneste (inspirert av hunden Prancer) som viste frem nyheter i Spring Boot 4 og Spring Framework 7: auto-konfigurasjon flyttet ut i mer granulære startere (bl.a. egen REST-klient-starter uten webserver), Spring AOT som genererer lesbar og debugbar repository-kode ved kompilering, innebygd API-versjonering i kontrollere, deklarative HTTP-klienter via grensesnitt, og nye resiliens-annotasjoner som @Retryable og concurrency limit – motivert av fjorårets AWS- og Cloudflare-nedetider. Han viste også den nye BeanRegistrar-mekanismen for programmatisk og dynamisk bean-registrering.

Siste del handlet om Spring Security 7: automatisk migrering av utdaterte passord-hasher (SHA-256 til bcrypt) ved innlogging, den nye customizer-tilnærmingen som bygger videre på sikre standardinnstillinger i stedet for å overstyre dem, engangstoken-innlogging, passkeys/WebAuthn med biometri, og granulær multifaktor-autentisering der ulike deler av applikasjonen kan kreve ulike faktorer. Konklusjonen: patch alltid, dropp rene passord, og bruk plattformens innebygde sikkerhets- og resiliens-støtte.

**Tags:** `Spring Boot` · `Java` · `Kotlin` · `Live coding` · `Backend` · `AI` · `Performance` · `Sikkerhet` · `API-design`

**📹** [Bootiful Spring Boot 4 – Josh Long](https://vimeo.com/1223346611)

*[← JavaZone 2026](../README.md)*
