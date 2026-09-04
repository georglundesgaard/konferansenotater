# Talk to me Java!

*Dag 1, 2. september 2026 · kl 11:40 · Martin Skarsaune · 📋 [i programmet](../program.md#d1-1140) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/299ff47c-4359-4233-a74c-3f174c10da9c)*

Skarsaune, konsulent i Kantega og bidragsyter til flere JVM-verktøy, testet i år en annen vinkel på JVM-feilsøking: å slippe Claude løs på en Spring Petclinic-applikasjon med innplantede feil, for å se om AI-en klarer å spore dem opp med standardverktøy. Motivasjonen er at JVM-feilsøking er komplekst, at ekspertverktøy som Java Mission Control har høy terskel, og at AI kan håndtere store datamengder uten menneskets bekreftelsestendens. I terminalen brukte Claude JDK-verktøy som jps og jcmd – via thread dump fant den tråder som hang evig på samme objektmonitor, og med OS-kommandoer avslørte den en fillekkasje der input-strømmer aldri ble lukket. Med Flight Recorder-opptak analysert via jfr-kommandolinjen fant den også exceptions og allokerings-hotspots, blant annet ineffektiv strengkonkatenering i løkke.

Deretter viste han hvordan samme tilnærming fungerer i låste containermiljøer: med kubectl debug kan man injisere en midlertidig sidecar-container med full JDK og la Claude kjøre jcmd-kommandoene «via via». En renere vei er Jolokia, som eksponerer JMX over HTTP med JSON-svar og nå også har en MCP-server – da kan Claude kjøre i sandkasse og til og med strømme ut en flight recording-fil bit for bit via en MBean-operasjon. Til slutt demonstrerte han JFR Microscope, et nytt webverktøy for flight recordings med innebygd AI-chat, som fant den tilsiktede strengkonkatenerings-feilen. Konklusjonen hans er at fremtiden trolig ligger i interaktive verktøy med innebygde MCP-er for agentene.

**Tags:** `Java` · `Observability` · `Tooling` · `JVM` · `MCP` · `AI` · `Live demo`

**📹** [Talk to me Java! – Martin Skarsaune](https://vimeo.com/1223363059)

*[← JavaZone 2026](../README.md)*
