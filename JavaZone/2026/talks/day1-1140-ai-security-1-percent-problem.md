# The 1% Problem: An Introduction to AI Security

*Dag 1, 2. september 2026 · kl 11:40 · Lars Smeby · 📋 [i programmet](../program.md#d1-1140) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/a9fa06ab-0bdc-46dd-979d-616608f0f0ed)*

Smeby fra Blank ga en innføring i AI-sikkerhet med utgangspunkt i at nesten alle nå bygger AI inn i produktene sine, mens sikkerheten henger etter. Han startet med hvordan LLM-er faktisk fungerer – en probabilistisk neste-token-prediktor uten fakta, hukommelse eller garantier – og forklarte hvorfor dette gir en helt ny angrepsflate: naturlig språk som angrepsvektor og et flatt kontekstvindu der systeminstruksjoner, hentede dokumenter og brukerinput ankommer som udifferensiert tekst. Prompt injection er derfor det største problemet, illustrert med Bing Chat som lekket systemprompten sin, Chevrolet-chatboten som gikk med på å selge en bil for én dollar, og Lenovos supportbot som ble lurt til å stjele sesjonscookies via XSS.

Han gikk gjennom hvorfor angrepene lykkes (konkurrerende mål mellom hjelpsomhet og sikkerhet, og sikkerhetstrening som ikke dekker omskrivinger som Base64 eller fiksjonsrammer), og skilte mellom direkte og indirekte prompt injection – sistnevnte demonstrert med Gemini-angrepet der skjulte instruksjoner i en kalenderinvitasjon kapret assistenten. Via OWASP Top 10 for LLM-applikasjoner dekket han også denial-of-wallet, LLM-jacking av stjålne API-nøkler, hallusinerte kilder (som i skolerapportene i Tromsø), usikker AI-generert kode og «slopsquatting» – at angripere registrerer pakkenavn modeller konsekvent hallusinerer.

Siste del handlet om agenter: verktøy, MCP-servere, skills og regelfiler utvider kontekstvinduet med innhold en angriper kan plante instruksjoner i – til og med usynlige Unicode-tegn – og en kapret kodeagent kjører med utviklerens fulle rettigheter. Mottiltakene er delimitere, AI-brannmurer, minste privilegium, rate limits og logging som skiller agent- fra brukerhandlinger – men selv modeller som stopper 99 % av angrepene feiler: i applikasjonssikkerhet er 99 % strykkarakter, for angriperen prøver bare hundre ganger. Konklusjonen: prompt injection er et uløst problem, så design systemene ut fra at AI-sikkerhetskontrollene vil svikte – for det gjør de, 1 % av tiden.

**Tags:** `AI` · `Sikkerhet` · `LLM` · `AI-agenter` · `MCP`

**📹** [The 1% Problem: An Introduction to AI Security – Lars Smeby](https://vimeo.com/1223383834)

*[← JavaZone 2026](../README.md)*
