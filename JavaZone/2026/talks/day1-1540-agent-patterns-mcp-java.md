# Building Intelligent Java Apps: Agent Patterns, MCP, and the Future of AI Native Design

*Dag 1, 2. september 2026 · kl 15:40 · Daniel Oh · 📋 [i programmet](../program.md#d1-1540) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/1a6f75e1-b192-4b86-b2a3-3932aa1baf60)*

Oh fra Red Hat/IBM argumenterte for at Java fortsatt er høyst relevant i AI-æraen: agenter er i praksis en ny type mikrotjenester, og enterprise-plattformer stiller de samme kravene til sikkerhet, observability og stabilitet som Java-økosystemet har levert i 30 år. Han skisserte utviklingen fra enkeltmodell-chatboter og prompt engineering til multiagent-systemer med resonnerende modeller, og oppfordret utviklere til å innta rollen som orkestrator over AI-verktøyene.

Han gjennomgikk de grunnleggende agent-mønstrene – sekvens, parallell, ruting/betinget, løkke og supervisor – og trakk paralleller til tradisjonell forretningslogikk (if/else, for-løkker, metodekall). MCP ble avmystifisert som et rent transportlag mellom modeller og verktøy: nyttig for discoverability i komplekse systemer, men ikke alltid riktig valg, siden ekstra nettverkshopp gir latens og tokenkostnad, og en sentralisert MCP-server fort blir en tett koblet monolitt. A2A (agent-to-agent) ble presentert som løsningen for språkagnostisk kommunikasjon mellom agenter bygget av ulike team, med agent-kort (JSON) for å beskrive identitet og kapabiliteter.

I live-demoen viste han et incident-dashboard bygget med Quarkus og LangChain4j, der 12 agenter kombinerte supervisor-, sekvens- og parallellmønstre, MCP mot en PostgreSQL-database og A2A mot en fjernagent – inkludert human-in-the-loop-godkjenning av en eskalering med estimert forretningskonsekvens på 360 000 dollar, rapportgenerering via en løkke der én agent skriver utkast og en annen vurderer mot en poenggrense, og sporing av agentkjøringene i Jaeger. Konklusjonene: bruk MCP og A2A der de faktisk passer, legg alltid inn deterministisk verifisering (dommer-API, human-in-the-loop, guardrails mot prompt injection), begrens agentenes fullmakter med terskler og kill switch, og bygg inn tracing og observability fra start.

**Tags:** `AI-agenter` · `MCP` · `Java` · `Quarkus` · `Live demo` · `LangChain4j`

**📹** [Building Intelligent Java Apps – Daniel Oh](https://vimeo.com/1223428250)

*[← JavaZone 2026](../README.md)*
