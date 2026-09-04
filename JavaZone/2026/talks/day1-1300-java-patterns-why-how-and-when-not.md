# Java Patterns: Why, How, and When Not

*Dag 1, 2. september 2026 · kl 13:00 · Cay Horstmann · 📋 [i programmet](../program.md#d1-1300) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/6092efef-0afe-4681-9b6b-1a2d5c8cdbf6)*

Horstmann, mangeårig forfatter av Core Java, ga en ren Java-prat om dataorientert programmering (DOP) og pattern matching. Med et lekseksempel med banktransaksjoner viste han hvordan sealed interfaces, records og switch-uttrykk med rekord-dekonstruksjon lar deg modellere data uten innkapsling – og hvordan kompilatorens exhaustiveness-sjekk fanger opp nye subtyper. Hovedbudskapet var at DOP og OOP ikke er i krig: arv og polymorfisme er fortsatt riktig når hierarkiet er åpent for utvidelse, mens DOP passer når antallet varianter er endelig og kjent. Han anbefalte Chris Kiehls bok «Data-Oriented Programming», og avmystifiserte begrepet algebraiske datatyper (sum- og produkttyper) som nettopp slike «kam-formede» sealed record-hierarkier – records kan ikke arve records, så hierarkiet blir flatt som en kam.

Andre halvdel gikk gjennom praktiske detaljer og fallgruver: ikke legg inn default i pattern-switcher (det saboterer exhaustiveness-sjekken – la heller MatchException varsle om nye subtyper), null-håndtering med case null, nestede mønstre, guards med when, type-mønstre kontra instanceof og dominansregler for rekkefølgen på cases. Som casestudie sammenlignet han sin egen DOP-modellering av JSON med JEP 540, det kommende JSON-biblioteket i JDK-en, der Java-arkitektene bevisst valgte klassisk OOP med skjulte implementasjoner.

Han avsluttet med switch-historikk (fra C-ens jump tables til dagens sekvensielle pattern matching) og noen «puzzlers» som viser sære kanttilfeller, inkludert primitiv pattern matching fra JEP 532 – der et `int`-mønster mot en `double`-komponent stille bare matcher verdier som får plass i en int. Konkrete råd: bruk alltid var i dekonstruksjonene, unngå fall-through, og la switch i moderne Java signalisere nettopp pattern matching over sealed-hierarkier. En helt grei talk – men noe smalere tema enn jeg hadde ventet på forhånd.

**Tags:** `Java` · `Pattern matching` · `Språkdesign` · `Backend` · `API-design` · `JVM`

**📹** [Java Patterns: Why, How, and When Not – Cay Horstmann](https://vimeo.com/1223388783) Lysbilder: [horstmann.com](https://horstmann.com/presentations/2026/javazone/).

*[← 1020 The positive value of negative space](day1-1020-the-positive-value-of-negative-space.md) · [1420 Å skifte vinger i lufta →](day1-1420-skifte-vinger-i-lufta.md)*
