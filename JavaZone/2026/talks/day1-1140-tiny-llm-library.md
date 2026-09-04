# Let’s create a tiny LLM library together

*Dag 1, 2. september 2026 · kl 11:40 · Johannes Bechberger · 📋 [i programmet](../program.md#d1-1140) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/2b2b442c-1dca-4cf3-9461-3be35a03daf0)*

Bechberger fra SAPs SapMachine-team viste hvordan man bygger et lite LLM-bibliotek i Java fra bunnen av, fordi han ikke ville skipe et 100 MB rammeverk for enkel LLM-funksjonalitet i et lite verktøy. Poenget hans var at LLM-API-er egentlig er «kjedelige»: alt er HTTP og JSON mot to OpenAI-kompatible endepunkter – models og chat completions – og en chatbots «hukommelse» er bare en voksende meldingsliste som sendes på nytt hver gang. Streaming skjer med server-sendte events, bilder legges inn som base64-URL-er, og live-demoene kjørte både mot en hostet Kimi-modell og lokale småmodeller via llama.cpp.

Deretter bygget han ut klienten steg for steg: tool calling med verktøy beskrevet i JSON Schema og en enkel løkke der LLM-en ber om verktøykall (med advarsel om at verktøy er kodeeksekvering og må sandkasses), håndtering av kontekstoverflyt via token-sporing og oppsummering – der beste praksis er å beholde systemprompt og de første brukermeldingene, komprimere midten og beholde de siste meldingene – samt MCP, som han beskrev som «fjernversjonen» av tool calling over JSON-RPC.

Til slutt demonstrerte han en liten kodeagent bygget på de samme to API-ene: en egen tilstandsmelding etter systemprompten som agenten selv kan modifisere (mål, planer, to-dos), planleggingsmodus med research-, spørsmåls- og planfase der skriveverktøy fjernes, og skills som «pluggbare systemprompter» i skill.md-format med YAML-frontmatter. Konklusjonen: kjedelige API-er er en styrke fordi de er debugbare, men ikke bruk demoverktøyene i produksjon, og tenkebudsjett bør begrenses siden små modeller kan resonnere seg i sirkel.

**Tags:** `LLM` · `Java` · `Live coding` · `AI` · `API-design` · `JVM` · `AI-agenter` · `MCP`

**📹** [Let's create a tiny LLM library together – Johannes Bechberger](https://vimeo.com/1223358361)

*[← JavaZone 2026](../README.md)*
