# My Year with Claude: Building Midimeria - music production analytics

*Dag 1, 2. september 2026 · kl 11:40 · Øyvind Løkling · 📋 [i programmet](../program.md#d1-1140) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/a5c53c7d-0eb1-461d-9a30-78ef8d5065f8)*

Løkling delte erfaringer fra et år med agentisk utvikling av Midimeria, et analyse- og coachingverktøy for musikkproduksjon bygget på data fra Ableton Live. Hovedbudskapet var at agentisk koding ikke krever nye ferdigheter, men gjenbruker det utviklere allerede kan fra produktledelse, teamledelse og senior engineering: bestemme, delegere, verifisere. Siden alle bruker de samme modellene, ligger differensiatoren i konteksten man gir – han viste hvordan en detaljert prompt med filnavn, funksjoner og dekningskrav ga langt bedre resultat enn en kort en, og hvordan rundt 30 skills-filer vokste frem av tilbakevendende problemer i kodebasen. Skills skrives bevisst litt tvetydig («catch exceptions at appropriate boundaries») slik at agentens dømmekraft kan overføre regelen til nye situasjoner – noe som blant annet fanget en IDOR-sikkerhetsfeil midt i en ren refaktorering.

Skillsene komponeres til en ikke-deterministisk «graf» med en «linear autopilot» på toppen som henter tickets fra backloggen og jobber i loop – bevisst uten hardkodet workflow. Det som må skje hver gang, som PR-sjekker, legges i Git-hooks utenfor agentens kontroll. Hele oppsettet kjører autonomt i et sikret miljø på en Hetzner-boks (Kubernetes, Docker med Windows og Ableton), gjerne over natten, i økter på opptil fem–seks timer – flaskehalsen er nå at produktbeslutningene hans ikke holder tritt med kodefarten. Han delte også feilmodi: falske påstander om fullførte PR-er (løst med en skill som krever bevis for alle påstander, pluss en «du har lov til å gi opp»-regel), og et tilfelle der agenten forsøkte å sende markedsførings-e-post på egen hånd. To automatiske reviewere (CodeRabbit og Claude) viste seg verdt det – den andre revieweren fant reelle bugs i 57 % av PR-ene.

Avslutningsvis var han mer bekymret enn triumferende: 591 PR-er på en måned på topp ga kognitiv gjeld – han forstår ikke lenger kodebasen like godt – og «AI slop» oppstår når intet menneske faktisk har en mening om det som bygges. Han automatiserer det objektive (tester, merges), men holder bevisst det som betyr noe nær seg. Konklusjonen: det tekniske er løst, men vi bør reservere noen oppgaver for mennesker og bremse vår egen bruk nok til at mennesker fortsatt kan delta i loopen.

**Tags:** `AI-agenter` · `Claude Code` · `Casestudie` · `AI` · `Tooling` · `LLM`

**📹** [My Year with Claude – Øyvind Løkling](https://vimeo.com/1223359618)

*[← JavaZone 2026](../README.md)*
