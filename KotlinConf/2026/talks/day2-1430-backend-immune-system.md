# The Backend Immune System - Rich Errors, Ktor Observability and Safe Local Remediation

*Dag 2, 22. mai 2026 · kl 14:30 · Meike Felicia Hammer*

Meike Felicia Hammer presenterte et Kotlin-native motstandsmønster hun kaller «The Backend Immune System», bygd på tre samvirkende lag: rike, typede feil som bærer presis diagnostisk kontekst, Ktor-basert observability som gjør symptomene synlige i sanntid, og lokale deterministiske «agenter» som utfører små, idempotente og strengt avgrensede mikroutbedringer innenfor selve request-grensen. Hun var eksplisitt på at disse agentene ikke er LLM-drevne – det er ren Kotlin-logikk med forutsigbar oppførsel, klare invarianter og korte tidsvinduer, slik at oppførselen kan testes og revideres på vanlig måte.

Demoen kjørte samme tjeneste i to moduser: i «legacy mode» ble en forbigående feil sluppet gjennom som en 500-respons, mens «immune mode» fanget den samme feilen, klassifiserte den via de rike feiltypene og gjennomførte en avgrenset lokal utbedring før svaret forlot serveren. Poenget er at motstandsdyktighet bør bygges inn nær årsaken framfor å overlates til retries lenger ute i kjeden eller til uforutsigbare AI-mekanismer, slik at kjente feilmodi håndteres automatisk uten menneskelig inngripen.

**Tags:** `Backend` · `Ktor` · `Resilience` · `Observability` · `Feilhåndtering` · `Rich errors`

**📹** [The Backend Immune System – Meike Felicia Hammer](https://www.youtube.com/watch?v=oPKxwwppnuA)
