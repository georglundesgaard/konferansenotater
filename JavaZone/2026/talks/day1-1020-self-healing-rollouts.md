# Self-Healing Rollouts: Automating Production Fixes with Agentic AI

*Dag 1, 2. september 2026 · kl 10:20 · Kevin Dubois · 📋 [i programmet](../program.md#d1-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/e7a9e513-a5a5-48b3-866d-5e195e8935a9)*

Dubois (IBM) tok utgangspunkt i CrowdStrike-utfallet for å motivere progressiv leveranse: i stedet for big bang-utrulling rulles nye versjoner gradvis ut til en andel av brukerne via GitOps-verktøy som Argo CD med Argo Rollouts (eller Flagger), som automatisk ruller tilbake hvis suksesskriteriene ikke oppfylles. Problemet er at disse kriteriene tradisjonelt må håndskrives som Prometheus-spørringer for hver tenkelig feilsituasjon – og det blir fort uhåndterlig.

Løsningen han og en kollega fra Adobe bygde, er et agentisk system i Quarkus og LangChain4j (Python ble forkastet som for tregt) som kobles inn via en egenutviklet Argo Rollouts-plugin. Flere agenter samler logger og metrikker fra stable- og canary-podene i parallell, en LLM sammenligner versjonene og avgjør promotering eller rollback, og en scoringsagent kvalitetssikrer analysen i en loop. Asynkront klassifiserer systemet deretter rotårsaken: er det en kodefeil, lager en remediation-agent automatisk en pull request med foreslått fiks (med menneske i loopen); er det operasjonelt, opprettes en beskrivende GitHub-issue. I live-demoen rullet han ut en versjon med NullPointerException som ble oppdaget og rullet tilbake på sekunder med automatisk PR, deretter en minnelekkasje som ga rollback pluss issue, og til slutt en frisk versjon som ble promotert til 100 %.

Lærdommene: små modeller (Qwen på 27B, tidvis helt ned i 4B) holder fint til analysen og gir svar på et par sekunder; prompten var det vanskeligste – den tok nesten lengre tid enn selve systemet; og deterministiske workflows med ikke-AI-agenter for datainnhenting slo både MCP-verktøy og GitHubs offisielle MCP-server på hastighet. Alt kjører som en vanlig Java-applikasjon på Kubernetes, og koden er åpen som proof of concept.

**Tags:** `AI-agenter` · `Java` · `Kubernetes` · `CI/CD` · `Observability` · `Feilhåndtering` · `JVM` · `Live demo` · `LLM`

**📹** [Self-Healing Rollouts – Kevin Dubois](https://vimeo.com/1223322662)

*[← JavaZone 2026](../README.md)*
