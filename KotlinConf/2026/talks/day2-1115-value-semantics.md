# How I Learned to Stop Worrying and Love Value Semantics (in Kotlin)

*Dag 2, 22. mai 2026 · kl 11:15 · Marat Akhin*

Marat Akhin fra JetBrains sitt Kotlin Language Evolution-team argumenterer for hvorfor value-semantikk fortjener en langt mer sentral plass i Kotlin, i motsetning til den referansesemantikken JVM-utviklere er vant til å sjonglere. Han viser hvordan `data class` og `.copy()` allerede gir et snev av value-tankegang, men at nøstede `.copy()`-kall raskt blir tungvinte når domenemodellen vokser.

Løsningen som er på vei er multi-field value classes (eksperimentelt fra Kotlin 2.5), som gir ekte in-place, uforanderlig-først-logikk uten allokeringsoverhead. Han knytter dette sammen med uforanderlige samlinger og peker på Compose som et konkret eksempel der immutability-by-default gjør endringsdeteksjon dramatisk mer effektiv.

Benchmarks i foredraget viser at value-orientert design ikke er en akademisk luksus, men fullt praktisk på JVM: ytelsen holder tritt med, og ofte slår, tradisjonelle mutable referanser. Konklusjonen er at Kotlin er i ferd med å bli et språk der man trygt kan slutte å bekymre seg for delt mutabel tilstand og heller lene seg på verdier.

**Tags:** `Språkdesign` · `Value classes` · `Immutability` · `Performance` · `Data class`

**📹** [How I Learned to Stop Worrying and Love Value Semantics – Marat Akhin](https://www.youtube.com/watch?v=YeQijxpnI3E)
