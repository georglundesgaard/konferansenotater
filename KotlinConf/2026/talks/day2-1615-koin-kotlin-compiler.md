# Koin + Kotlin Compiler = ♥️

*Dag 2, 22. mai 2026 · kl 16:15 · Arnaud Giuliani*

Arnaud Giuliani presenterte den største endringen i Koin på åtte år: en tett integrasjon med Kotlin-kompilatoren som flytter mesteparten av arbeidet fra kjøretid til kompileringstid. Med en ny kompilator-plugin blir DSL-oppsettet automatisert, slik at utviklerne slipper å skrive og vedlikeholde like mye modul-boilerplate for hånd.

Pluginen bygger også forhåndsberegnede avhengighetsindekser, noe som gir merkbart raskere oppstart og redusert overhead i grafoppslag. Samtidig får man ekte kompileringstidssikkerhet – manglende eller sirkulære bindinger avdekkes før appen kjører – uten at det velkjente og lettleste API-et endres.

Resultatet er at Koin beholder sin pragmatiske ergonomi, men flytter seg fra ren runtime-DI til en løsning som konkurrerer med kompilator-genererte rammeverk på ytelse og sikkerhet.

**Tags:** `Koin` · `DI` · `Compiler plugin` · `Compile-time` · `Performance`

**📹** [Koin + Kotlin Compiler = ♥️ – Arnaud Giuliani](https://www.youtube.com/watch?v=eBu9i2MYWWM)
