# Trust, But Verify: Skill-Driven Development for the Sceptical Java Developer

*Dag 2, 3. september 2026 · kl 10:20 · Totto – Thor Henning Hetland · 📋 [i programmet](../program.md#d2-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/7ba94a91-4db9-4451-82f8-f300b3f978a0)*

Totto åpnet med et AI-generert «memoir of the ghost in the machine» før han fortalte om sitt agentiske kaninhull: i januar pushet han Claude Code til å bygge et bibliotek for mønsterkortproduksjon (PCB) – et domene han ikke kan selv. Da Claude sa «ferdig», brukte han ti dager på å prøve å knekke det med åtte industriformater, tusenvis av virkelige filer, 2D/3D-visualisering og borehullsimulering. Fra denne prosessen ekstraherte han «Skill Development Six Pillar»-metodikken, som han siden har kjørt workshop på for 100–150 personer. Grunnprinsippet er «trust, but verify»: for hver frykt du har overfor agenten, bygg et system som håndterer den – round-trip-tester med ekle reelle data, property-based testing og Monte Carlo-simuleringer, slik at agenten ikke kan jukse.

Han viste teknikker for å henge med i agent-tempoet: la Claude skrive dype rapporter som kryssjekkes i ChatGPT Deep Research mot eksisterende forskning, og generere user guides som mates inn i NotebookLM for infographics og presentasjoner man kan mappe mot sin egen mentale modell – slik fant han blant annet at IP-beskyttelse var bygget men aldri wiret opp. Videre presenterte han sin agentiske infrastruktur: Exo Cortex (riggen hans), Synthesis (kontekst-/tilgangsstyring på tvers av 247 kodebaser med blast radius-analyse), og fremfor alt KSP – Knowledge Context Protocol – en åpen, grafbasert spesifikasjon for å strukturere kunnskap til agenter, med tilhørende command-wrappere og episodisk agentminne. Alt ligger open source på GitHub.

Siste del handlet om produksjonsagenter og compliance: via kunden Mindor bygde han deterministiske KSP-plannere, styrte «agent-hender» og til slutt Sunstone Atlas – et slags operativsystem for produksjonsagenter med governance, CISO-dashboard og en «troverdighetsstige» der agenter må lykkes gjentatte ganger før de får kjøre autonomt. Konklusjonen: yolo-hipsterne feiler og de paranoide står stille – det er de redde ingeniørene som bygger systemer rundt frykten sin som frigjør 10–40x produktivitet.

**Tags:** `AI` · `Skills` · `Testing` · `Java` · `AI-agenter` · `LLM` · `Tooling`

**📹** [Trust, But Verify – Totto - Thor Henning Hetland](https://vimeo.com/1223642971)

*[← JavaZone 2026](../README.md)*
