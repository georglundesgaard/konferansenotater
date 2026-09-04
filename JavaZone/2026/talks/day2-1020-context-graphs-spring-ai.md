# The Decision Layer: Context Graphs for Spring AI

*Dag 2, 3. september 2026 · kl 10:20 · James Ward, Ryan Knight · 📋 [i programmet](../program.md#d2-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/71a26d1c-2b8a-41ec-a02e-e119830a75a0)*

Ward (AWS) og Knight (Neo4j) tok for seg hvorfor AI-automatisering av forretningsprosesser stort sett har mislyktes: ren datatilgang via RAG, verktøy og MCP er ikke nok, fordi AI-en mangler konteksten rundt policyer og hvorfor tidligere beslutninger ble tatt. Løsningen deres er et «beslutningslag» – en kontekstgraf i Neo4j som fanger evidens, policyer, unntak, faktiske beslutninger og presedens, slik at agenten kan resonnere seg frem til stadig mer autonome avgjørelser. Siden modellene selv er statiske, skjer «læringen» ved at grafen vokser for hver iterasjon og beriker prompten med stadig rikere kontekst.

De demonstrerte konseptet med en lånesøknadsdemo bygget på Spring AI mot Bedrock, der advisors – Spring AIs middleware-mekanisme for å intercepte kall til og fra LLM-en – gjør jobben: en «precedent advisor» henter selskapets historikk, policyer og tidligere avslag fra grafen og injiserer dem i prompten, mens en «decision trace advisor» skriver beslutningen med begrunnelse og autorisasjonssti tilbake til Neo4j. Dermed blir grafen en strukturert beslutningslogg som agenter kan traversere med flerstegs-resonnering via Cypher og semantisk vektorsøk. De viste også hvordan samme beslutningslag kan deles på tvers av flere agenter som beriker hverandres kontekst.

Konklusjonen var at strukturert grafkontekst gir bedre presisjon, mindre hallusinering, lavere tokenkostnader (unngår «context rot») og en evolusjonær sløyfe mot økende autonomi – med mennesket i loopen i starten, gradvis mindre etter hvert som tilliten bygges. På spørsmål fra salen erkjente de at ren AI-generert beslutningshistorikk kan forsterke skjevheter, og at menneskelige vurderinger bør modelleres som egne noder i grafen.

**Tags:** `AI-agenter` · `Spring Boot` · `Arkitektur` · `Live demo` · `Spring AI` · `Neo4j` · `LLM`

**📹** [The Decision Layer: Context Graphs for Spring AI – James Ward, Ryan Knight](https://vimeo.com/1223644281)

*[← JavaZone 2026](../README.md)*
