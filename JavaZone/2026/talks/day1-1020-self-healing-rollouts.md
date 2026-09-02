# Self-Healing Rollouts: Automating Production Fixes with Agentic AI

*Dag 1, 2. september 2026 · kl 10:20 · Kevin Dubois · 📋 [i programmet](../program.md#d1-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/e7a9e513-a5a5-48b3-866d-5e195e8935a9)*

Kevin Dubois viser hvordan progressive delivery med Argo Rollouts i Kubernetes kan tas et steg videre ved å koble på agentisk AI. Utgangspunktet er kjente teknikker som gradvise utrullinger og automatisk analyse av om en ny versjon oppfører seg som forventet – men der en mislykket rollout normalt bare rulles tilbake og venter på et menneske, lar Dubois en AI-agent ta over neste steg.

Agenten er skrevet i Java og trår til når en deploy feiler: den undersøker hva som gikk galt i produksjon og automatiserer selve fiksen, slik at utrullingen blir «selvhelbredende» i stedet for bare selvbeskyttende. Foredraget demonstrerer dermed et mønster der Java-utviklere kan bygge driftsagenter som lukker løkken fra feildeteksjon til utbedring, uten å forlate JVM-økosystemet de kjenner.

*(Sammendrag basert på programomtalen – oppdateres via /berik-foredrag når opptaket er publisert.)*

**Tags:** `AI-agenter` · `Java` · `Kubernetes` · `CI/CD` · `Observability` · `Feilhåndtering` · `JVM`

**📹** [Self-Healing Rollouts – Kevin Dubois](https://vimeo.com/1223322662)

*[← JavaZone 2026](../README.md)*
