# Fremtidens applikasjoner lages for maskiner

*Dag 1, 2. september 2026 · kl 10:20 · Stig Lau · 📋 [i programmet](../program.md#d1-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/b20063ea-3d4b-49a9-97b2-70801f070139)*

Lau fra Skatteetaten tok utgangspunkt i en kantinesamtale om at noen snart kan slippe løs en KI-agent på skattemeldingen sin, og viste hvordan han på en time bygde «maskinen som lager maskinen»: et Claude Code-basert open source-verktøy som sonderer en applikasjon (for eksempel via Playwright mot en nettbutikk), kartlegger REST-kallene under overflaten og lagrer kunnskapen strukturert – i tråd med KCP (Knowledge Context Protocol) – slik at neste agentkjøring starter med alt klart. Arbeidsflyten hans er å iterere en prosess sammen med agenten noen ganger, persistere den som skills, og til slutt be om et 50–80 prosent-skript som feiler raskt med stack trace – da minimeres tokenbruk og data slipper å sendes til LLM-leverandøren.

Han argumenterte for at fremtidens tjenester heller bør eksponere strukturert kunnskap om vanlige REST-API-er enn å følge MCP-protokollen, og at rimeligere, fokuserte modeller støttet av dokumentlager og skills vil erstatte de dyreste modellene i applikasjonsstøtte – med kontekstvindu og minnehåndtering som det største problemet fremover. Han viste konkrete eksempler fra egen hverdag, som en agent som henter Jira-issues, sjekker ut relaterte brancher, verifiserer Jenkins-bygg og deployer til Kubernetes, og skisserte en fremtid der en saksbehandler i Skatteetaten kan beskrive en idé tekstlig, la agenten integrere mot tjenesteregisteret i syntetisk miljø, og gradvis løfte et verifisert skript mot test og produksjon – uten at LLM-en blir med opp.

Sikkerhet var et gjennomgående poeng: autentiseringsnøkler flyttes ut av agentens rekkevidde, og han advarte mot prompt injection-varianter av Log4j/deserialiseringsproblematikken, der ondsinnede data kan ligge lagret i måneder før en LLM plukker dem opp. Konklusjonen var å ta kontroll over verktøyet: ikke forelske seg i én modell, bruke LLM-en til det den er god til, og at de viktigste AI-medarbeiderne blir de som stiller de vanskelige spørsmålene.

**Tags:** `AI-agenter` · `API-design` · `Arkitektur` · `REST` · `LLM` · `Sikkerhet` · `Casestudie`

**📹** [Fremtidens applikasjoner lages for maskiner – Stig Lau](https://vimeo.com/1223287917)

*[← JavaZone 2026](../README.md)*
