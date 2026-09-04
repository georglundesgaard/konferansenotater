# Sanntidsinformasjon i saksbehandlingssystemer

*Dag 1, 2. september 2026 · kl 10:20 · Jørgen Sølvernes Sandnes, Dragana Stojkovic · 📋 [i programmet](../program.md#d1-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/074fa6da-2ad5-4efa-a482-120e80351bb9)*

Sandnes og Stojkovic fra Husbanken presenterte hvordan Kobo – det felles saksbehandlingssystemet for kommunale boliger som erstattet 300 kommuners ulike løsninger – har fått sanntidsoppdatering av data. Foredraget åpnet med en humoristisk sketsjdemo der kolleger spilte figurer som en misfornøyd influenser, «Kokken Claude», Petter Stordalen og Magnus Carlsen for å illustrere frustrasjonen ved å måtte laste siden på nytt, og gevinsten ved varsler og samtidighetsstøtte.

Teknisk bygget de løsningen opp i byggeklosser oppå en tradisjonell frontend/backend-arkitektur: to HATEOAS-inspirerte konsepter – «tillatte operasjoner» (backend forteller frontend hvilke handlinger som er lov, som forenkler frontend og sentraliserer logikken) og «updated objects» (backend returnerer referanser til alle objekter en operasjon endret, så frontend kan invalidere cachen). Deretter la de på en sanntidskanal basert på Server-Sent Events med heartbeat, filtrert per kommune (multitenancy) og per klient-ID, og brukte den til å distribuere updated objects, personlige varsler og «brukerhandlinger» – små hendelser om hva andre saksbehandlere gjør, som gir advarsler ved samtidig redigering av samme skjema.

Til slutt drøftet de skalering ærlig: de åpne SSE-tilkoblingene og in-memory-tilstanden gjør backend vanskelig å skalere horisontalt, men dataestimater for hele Norge tyder på at de kanskje aldri trenger det. Viktigere er ytelse: de måler responstider jevnlig mot forskningsbaserte terskler (100 ms, 400 ms–1 s, 2–10 s) og prioriterer ut fra det, illustrert med et Hibernate N+1-problem som ga over ti sekunders responstid på varsellisten før fiksen.

**Tags:** `Arkitektur` · `Skala` · `Performance` · `Casestudie` · `Live demo` · `API-design`

**📹** [Sanntidsinformasjon i saksbehandlingssystemer – Sandnes, Stojkovic](https://vimeo.com/1223320660)

*[← JavaZone 2026](../README.md)*
