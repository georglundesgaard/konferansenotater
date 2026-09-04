# Bra tools, ubrukelige svar: Læring fra ett år med MCP

*Dag 1, 2. september 2026 · kl 17:00 · Bjørn Nordlund, Eirik Fagtun Kjærnli · 📋 [i programmet](../program.md#d1-1700) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/1f42fc0f-4e1a-4aaf-b397-1c6a965e3b31)*

Nordlund og Kjærnli fra Cisco delte erfaringer fra et år med å bygge en MCP-server for Control Hub, administrasjonsløsningen for Ciscos videomøteromsystemer, som samler data fra hundretusenvis av møterom. Målet var å eksponere funksjonalitet og data som verktøy for AI-agenter, slik at kundene selv kan løse problemer uten forhåndsdefinerte flyter. Gjennom en demo-organisasjon med 150 000 enheter viste de hvordan selv enkle spørsmål gikk galt: agenten ga et selvsikkert, men feil svar fordi den trakk konklusjoner fra én enkelt paginert side med data, og et telle-spørsmål brant to millioner tokens før de stoppet den.

Lærdommene er i stor grad «godt gammeldags API-design»: et kraftig, fleksibelt søkeverktøy basert på etablerte standarder (de kopierte Elasticsearch-søkespråket), idiotsikre og konsekvent navngitte parametere, overtydelig pagineringsmetadata, og forsvarlig kontekstbruk med enkle/fulle responsformater. Nytt var å designe feil som en feature: i stedet for en naken 400-feil returnerer de feilmeldinger med forslag og retry-hint, slik at agenten selv retter seg. Tunge aggregeringer flyttet de inn i egne, optimaliserte verktøy nær dataene, med tolkningshint i responsen.

For skriveoperasjoner var bekymringen at brukeren ikke skjønner hva den godkjenner, så de utforsket elicitation (kraftig, men få klienter støtter det) og MCP apps som supplement til klientenes native godkjenningsdialoger. De delte også et uløst versjoneringsproblem der klienter som ChatGPT ikke plukker opp skjemaendringer – deres policy er nå rett og slett ingen breaking changes. Konklusjonen: gjør det lett for agenten å velge riktig, og vanskelig for den å gjøre feil – og test i flere agenter, for de oppfører seg svært ulikt.

**Tags:** `MCP` · `AI-agenter` · `Observability` · `Casestudie` · `API-design`

**📹** [Bra tools, ubrukelige svar – Bjørn Nordlund, Eirik Fagtun Kjærnli](https://vimeo.com/1223444307)

*[← JavaZone 2026](../README.md)*
