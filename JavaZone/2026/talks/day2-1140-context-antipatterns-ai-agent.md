# The Right 300 Tokens Beat 100k Noisy Ones: Four Context Antipatterns That Kill Your AI Agent

*Dag 2, 3. september 2026 · kl 11:40 · Baruch Sadogursky · 📋 [i programmet](../program.md#d2-1140) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/36db26e6-297f-467e-b1bb-74aeae59a0bc)*

Baruch Sadogursky (Port) viste gjennom en serie live-demoer med Claude Code hvorfor agenter feiler av arkitektoniske grunner, ikke modellgrunner: problemet er konteksten modellen ser, og større kontekstvindu hjelper ikke fordi oppmerksomheten uansett er begrenset. Han gikk gjennom fire antimønstre. Først «stuffed prompt» – en enorm superprompt med alt om konvensjoner, sikkerhet, deploy og testing, som forvirrer modellen; løsningen er skills med progressiv oppdagelse, der en god beskrivelse i front matter lar agenten laste rett kunnskap først når den trengs. Deretter «feil verktøy»: RAG-demoen fant det mest *lignende* dokumentet (feil bibliotekversjon) fordi likhet ikke er det samme som korrekthet – bruk versjonerte docs for korrekthet, skills for prosess, skript for determinisme og LLM-resonnering kun for skjønn.

Tredje antimønster er «gullfiskagenten»: /clear, kompaktering og innebygd minne er utenfor din kontroll, så inspirert av filmen Memento lærte han agenten å skrive arkitekturbeslutninger til en egen, versjonert minnebank (.memory med kontekst, beslutning og konsekvenser) som også er portabel mellom agenter. Fjerde er «vibe eval» – å anta at konteksten ble bedre uten å måle: LLM-en genererer scenarioer og rubrikker, mennesket reviewer dem (pass på lekkasje av svaret i spørsmålet, og ta med negative scenarioer), og LLM-en dømmer; hans oppsett gikk fra 35 % uten kontekst til 89 % med. Han anbefalte å bundle skills, skript, regler og hooks som «context plugins» og behandle dem som artefakter – versjonert, testet og distribuert – og å kjøre evals jevnlig, siden bedre modeller kan gjøre en skill overflødig. Konklusjon: context engineering er et arkitekturproblem, og de riktige få tokenene slår store mengder støy.

**Tags:** `AI-agenter` · `LLM` · `Context engineering` · `Live demo` · `Tooling`

**📹** [The Right 300 Tokens Beat 100k Noisy Ones: Four Context Antipatterns That Kill Your AI Agent – Baruch Sadogursky](https://vimeo.com/1223667266)

*[← JavaZone 2026](../README.md)*
