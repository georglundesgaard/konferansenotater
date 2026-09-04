# Å skifte vinger i lufta eller hjul mens sykkelen er i nedoverbakke: Modernisering av samfunnskritiske systemer uten høye skuldre

*Dag 1, 2. september 2026 · kl 14:20 · Johannes Brodwall, Hafsa Elkam · 📋 [i programmet](../program.md#d1-1420) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/02dd2bd6-0ff8-4642-89fa-6fdfcf82ea5b)*

Hafsa Elkam og Johannes Brodwall fra Politiets IT-enhet – i en underholdende dialog mellom «smidig byråkrat» og «teknologitrollmann» – fortalte om moderniseringen av to av politiets viktigste systemer: det politioperative systemet PO og straffesakssystemet BL – 90-tallssystemer som VG omtalte som «italiensk spaghetti», og som en intern rapport knyttet til Elverum-drapet. Etter feilslåtte storsatsinger som Merverdiprogrammet bygger de nå nytt med tre enkle grep: nærhet til brukerne, å få nytt og gammelt til å fungere sammen, og produktorienterte autonome team som skaper resultater – for resultater gir tillit og handlingsrom.

Teknisk viste de to ulike strategier. På det operative systemet gjenbrukte de det gamle systemets eventmekanisme for skjermsynkronisering, slik at det nye systemet opptrer som en «bruker» av den gamle databasen og data flyter begge veier – brukerne kan dermed veksle fritt mellom nytt og gammelt, noe som ga organisk adopsjon uten opplæring (Vest politidistrikt ba selv om prod-tilgang etter en times demo). Som det ble sagt fra scenen: «brukerne elsker uferdige systemer» – når de selv får påvirke dem, med det gamle systemet som trygg fallback – mens ferdige systemer «hater» de. Straffesakssystemet er egentlig tre monolitter i Smalltalk, COBOL og en no code-plattform; der erstatter de kjernesystemet først, kjører den gamle COBOL-koden i JVM og prosesserer data parallelt mot gammel og ny database, med black box-tester i JUnit som avdekker skjulte rariteter – som at saker i fuglereservatet på Svalbard fikk omkodet landkode.

Status: rundt 96 prosent av oppdragene registreres nå i de nye operative løsningene (mål om full utfasing i 2026), mens straffesakskjernen er om lag 46 prosent ferdig, med 98 prosent samsvar på skriveoperasjoner. Konklusjonen: man må bygge den nye vingen før man tar av den gamle – samfunnskritiske systemer kan moderniseres trygt, uten fakkeltog og uten høye skuldre.

**Tags:** `Casestudie` · `Modernisering` · `Arkitektur` · `Legacy-modernisering` · `Testing`

**📹** [Å skifte vinger i lufta eller hjul mens sykkelen er i nedove – Johannes Brodwall, Hafsa Elkam](https://vimeo.com/1223410462)

*[← 1300 Java Patterns](day1-1300-java-patterns-why-how-and-when-not.md) · [1700 Dream Machines & Walled Gardens →](day1-1700-dream-machines-walled-gardens.md)*
