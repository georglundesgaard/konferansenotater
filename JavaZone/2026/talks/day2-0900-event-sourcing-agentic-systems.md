# Event Sourcing: The Only Sane Way to Run Agentic Systems

*Dag 2, 3. september 2026 · kl 09:00 · Einar Ingebrigtsen · 📋 [i programmet](../program.md#d2-0900) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/13fb6b2e-35e2-4fec-9e82-b28cebf73c7e)*

Ingebrigtsen argumenterte for at event sourcing er nødvendig når agenter handler autonomt i systemene våre: logger og CRUD-databaser viser hva som skjedde og sluttresultatet, men aldri hvorfor – og uten intensjon, kausalitet og hvem som autoriserte en endring kan man ikke stole på et agentisk system. Han demystifiserte konseptet med kjente paralleller (Git som eventstrøm med projeksjon til filsystemet, regnskapets hovedbok tilbake til 3100 f.Kr.) og skilte skarpt mellom domenehendelser i Eric Evans' forstand – navngitt i fortid, med kun meningsbærende egenskaper – og ting som IoT-målinger, som han mener er tidsserier, ikke events.

Kjernen i opplegget er en immutabel event store som sannhetskilde, formålsbygde read models per feature (gjerne polyglot persistens), outbox/inbox-oversettelse mellom systemer, og rik metadata med kommando, identitet og kausasjonskjede – der også agenter formaliseres som teammedlemmer med egen identitet. Han viste verktøy for å pivotere i eventdata, «time machine»-scrubbing gjennom historiske tilstander og heatmaps over aktivitetsmønstre for både brukere og agenter. LLM-er elsker dessuten event sourcing fordi eventsekvenser er ren språklig mening de kan analysere. Videre demonstrerte han event modeling med fire slice-typer (state change, state view, automation, translation) og Kotlin-kode fra hans open source-rammeverk Cratis.

I en lang spørsmålsrunde var han ærlig om hvorfor event sourcing knapt finnes i produksjon: 40–50 år med relasjonsdatabase-vane og nesten fraværende verktøyøkosystem – noe rammeverket hans prøver å bøte på med pragmatiske mekanismer som redact og revision, et deskriptivt «Screenplay»-språk, og «prologue»-verktøy som bruker LLM-er til å utlede events fra logger og databasetransaksjoner i eksisterende systemer.

**Notater fra konferansen:**
- Fra skaperen av [cratis.io](https://cratis.io)
- Intro om event sourcing for å fange alt som skjer i et system
- Events er domain events (fra DDD)
- Eventene lagres i en event store – den holder sannheten
- Observers, read models, outbox, inbox og «source box»
- Interessant foredrag om event sourcing og hvorfor det er viktig for å holde styr på hva agentene gjør og hvorfor i agentiske systemer

**Tags:** `AI-agenter` · `Event sourcing` · `Arkitektur` · `Database` · `Observability` · `Live demo`

**📹** [Event Sourcing: The Only Sane Way to Run Agentic Systems – Einar Ingebrigtsen](https://vimeo.com/1223620243)

*[← Dag 1, 1820 Hacking i «gamle» dager](day1-1820-hacking-i-gamle-dager.md) · [1140 Heis.fm LIVE →](day2-1140-heis-fm-live.md)*
