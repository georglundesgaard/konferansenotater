# We're making this a lot harder than it needs to be

*Dag 2, 3. september 2026 · kl 13:00 · Robin Heggelund Hansen · 📋 [i programmet](../program.md#d2-1300) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/ac8124ed-cfdb-4a28-a68a-8e2a6518b76c)*

Robin Heggelund Hansen (skaperen av programmeringsspråket Gren) argumenterte for at bransjen gjør webutvikling langt mer komplisert enn nødvendig – vi lager sjelden et MTP (Minimum Technical Product), selv når det vi bygger er en MVP. Utgangspunktet var at nyutdannede utviklere kan React og mikrotjenester, men aldri har laget en enkel nettside med et skjema. Han bygget packages.grenlang.org som en tradisjonell multi-page-app og ble overrasket over produktiviteten: ett prosjekt, ett byggesystem, og ruting, tilstand, feilhåndtering og lasting håndteres av nettleser og backend i stedet for å dupliseres i frontend.

I en live demo viste han en to-do-app skrevet nesten helt uten JavaScript – dialoger, animasjoner og skjemavalidering løst med moderne HTML og CSS, hele appen inkludert Java-backend på rundt 250 linjer. Deretter la han på HTMX: ett attributt gjorde checkbox-oppdateringer til «fire and forget» uten sideoppfriskning, og server-sent events ga sanntidssynkronisering med én eneste endring i frontend. Anbefalingen var å starte med ren HTML, legge til litt HTMX ved behov, og begrense React/Vue til enkeltsider som faktisk trenger mye interaktivitet – da blir også React-komponentene enklere. Service workers gir dessuten offline-støtte også for multi-page-apper.

Andre halvdel var et frontalangrep på mikrotjenester: han gikk gjennom AWS' offisielle argumenter (smidighet, fleksibel skalering, enkel deploy, teknologifrihet, gjenbruk, resiliens) og avviste de fleste ut fra egen erfaring – team kan jobbe autonomt i en monolitt, og en monolitt kan deployes til flere mål bak en load balancer. Kostnadene er reelle: mer kode, HTTP-kall i stedet for funksjonskall, dårligere IDE-støtte og vanskelig refaktorering på tvers av tjenestegrenser. Konklusjonen: norske selskaper har ikke Facebook-skala problemer, kompleksitet rammer AI-assistenter like hardt som mennesker, og vi må jevnlig revurdere om gamle teknologivalg fortsatt er gyldige i dag.

**Tags:** `Minimalisme` · `Forenkling` · `Web` · `Frontend` · `Live demo` · `Arkitektur`

**📹** [We're making this a lot harder than it needs to be – Robin Heggelund Hansen](https://vimeo.com/1223683965)

*[← 1140 Heis.fm LIVE](day2-1140-heis-fm-live.md) · [1540 Retro Meets AI →](day2-1540-retro-meets-ai.md)*
