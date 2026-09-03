# The Decision Layer: Context Graphs for Spring AI

*Dag 2, 3. september 2026 · kl 10:20 · James Ward, Ryan Knight · 📋 [i programmet](../program.md#d2-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/71a26d1c-2b8a-41ec-a02e-e119830a75a0)*

Ward og Knight adresserer et hull i multiagent-systemer med Spring AI: agentene deler data, men ikke resonnering – begrunnelsen bak et svar har ingen varig form, og neste agent arver dataene uten konteksten de andre bygget.

Løsningen er en Context-Aware Advisor bygget på Spring AI Advisor-API-et som «Decision Layer»: hvert spørsmål fanges, et strukturert beslutningsspor persisteres til Neo4j, og senere spørsmål berikes med grafsøk. Poenget er grafen: vektorsøk finner beslutninger som ligner, graftraversering følger relasjonene som gjør en tidligere beslutning anvendelig.

*(Sammendrag basert på programomtalen – oppdateres via /berik-foredrag når opptaket er publisert.)*

**Tags:** `AI-agenter` · `Spring Boot` · `Arkitektur`

**📹** [The Decision Layer: Context Graphs for Spring AI – James Ward, Ryan Knight](https://vimeo.com/1223644281)

*[← JavaZone 2026](../README.md)*
