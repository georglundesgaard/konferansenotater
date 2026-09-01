# Increasing quality of AI generated Kotlin code

*Dag 1, 21. mai 2026 · kl 16:15 · Sergei Rybalkin (Meta) · 📋 [i programmet](../program.md#d1-1615) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1081924/)*

Sergei Rybalkin fra Meta viste hvorfor bedre AI-generert Kotlin-kode krever mer enn smartere prompter, og delte hvordan teamet hans løfter kodekvalitet i stor skala. Han beskrev typiske utfordringer som at modellene produserer plausibel, men inkonsistent kode, bruker foreldede API-er eller bryter etablerte idiomer og konvensjoner i en enorm kodebase.

For å måle forbedringer bygger Meta systematiske evalueringer som kombinerer automatiske signaler – kompilering, tester og statisk analyse – med menneskelige vurderinger av lesbarhet og vedlikeholdbarhet. Rybalkin la vekt på verktøykjeden rundt agentene: kontekstfiler med Kotlin-idiomer, integrasjon mot lintere og statisk analyse, og feedback-løkker som lar agenten rette opp feil før koden når en reviewer.

Casestudien fra Meta viste at kombinasjonen av kuraterte retningslinjer, målrettet evaluering og tett kobling mot eksisterende utviklerverktøy gir mer forutsigbar og pålitelig kode enn ren promptoptimalisering, og at oppsettet må tilpasses etter hvert som modellene utvikler seg.

**Tags:** `AI` · `Kodekvalitet` · `Meta` · `Skala` · `Evaluering` · `Casestudie`

**📹** [Increasing quality of AI generated Kotlin code – Sergei Rybalkin](https://www.youtube.com/watch?v=rZvEuqUiPnw)
