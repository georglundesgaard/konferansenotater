# Hvordan logger kan felle en Nav-direktør

*Dag 1, 2. september 2026 · kl 15:40 · Trond Arve Wasskog, Audun Fauchald Strand · 📋 [i programmet](../program.md#d1-1540) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/5618fc48-5345-414c-9f47-1503c856264a)*

Wasskog og Strand fortalte historien bak Nav-direktør Hans Christian Holtes avgang i november 2025, som skyldtes manglende kontroll på manuelle databaseendringer og auditlogger – ikke personvernsnoking, men statens økonomireglement, som med den innskutte leddsetningen «herunder logging» krever logging av endringer gjort utenom applikasjonens normale funksjoner. Da Riksrevisjonen i desember 2024 begynte å revidere IT-systemene fremfor bare regnskapene, oppdaget Nav at loggene manglet, skrudde dem på og meldte avviket lukket – men høsten 2025 viste det seg at logging manglet for systembrukere i Oracle og DB2, at parametere og langtidslagring manglet i Postgres, og at en glemt DL/I-database fra stormaskinæraen ikke engang var vurdert. Å måtte melde til departementet at man hadde feilinformert ble skjebnesvangert, selv om det aldri var indikasjoner på mislighold – problemet var at Nav ikke kunne bevise at ingenting hadde skjedd.

Andre del handlet om opprydningen: Nav har klassifisert 146 systemer som «økonomisystemer» (alt som påvirker utbetalinger), og bygger etterlevelse inn i arbeidsmåten fremfor regneark-teater – verktøy som Gal (godkjenningsflyt rundt auditlogg-innslag i produksjonsdatabaser), NDA (Nav Deployment Audit, som sporer endringer fra behov via pipeline til produksjon) og KISS for kontrollrammeverket, pluss årlig trening på gjenoppretting fra backup. Foredragsholderne erkjente at teknologene kollektivt hadde ansvaret for å implementere lovene som styrer systemene, men advarte også om kostnaden: tiden som nå brukes på internkontroll går på bekostning av Navs egentlige oppdrag. Rådet til revisjonsklare: beskriv prosessen din og bevis at du følger den. Foredraget ble avrundet med at Strand takket for seg etter ti år i Nav.

**Tags:** `Observability` · `Casestudie` · `Etterlevelse` · `Database`

**📹** [Hvordan logger kan felle en Nav-direktør – Trond Arve Wasskog, Audun Fauchald Strand](https://vimeo.com/1223425579)

*[← JavaZone 2026](../README.md)*
