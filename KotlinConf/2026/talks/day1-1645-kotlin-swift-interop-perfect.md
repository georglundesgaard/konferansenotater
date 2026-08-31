# Can Kotlin Swift Interop Ever Be Perfect?

*[← KotlinConf 2026](../README.md) · Dag 1, 21. mai 2026 · kl 16:45 · Gleb Lukianets*

Gleb Lukianets tar utgangspunkt i at Kotlin og Swift på overflaten virker svært like, men at typesystemene, minnemodellene og runtime-semantikken skiller lag på måter som gjør «perfekt» interop nesten umulig. Han går gjennom hva den nye Swift Export-pipelinen faktisk klarer å bygge bro over sammenlignet med den gamle Objective-C-headeren: nullbare primitiver mappes nå direkte til Swift optionals uten `KotlinInt`-bokseklasser, `suspend`-funksjoner blir `async`, `Flow` blir `AsyncSequence`, pakker blir nøstede Swift-enumer, og Kotlin `enum class` blir ekte Swift `enum`. Samtidig tvinger de semantiske forskjellene fram harde designvalg: generiske typer type-slettes til sin øvre grense og støtter i praksis bare Kotlin-klasser (ikke Swifts value types), all cross-language arv er blokkert slik at selv `open`-klasser blir `final` på Swift-siden, og extension-funksjoner degraderes til statiske metoder med eksplisitt mottaker istedenfor idiomatiske Swift-extensions. Sealed classes eksponeres som et hierarki, men taper eksaustivitetssjekken i `switch`, og navngivning beholdes verbatim fra Kotlin uten camelCase-normalisering. Konklusjonen er at Swift Export flytter smertepunktene, men fordi Kotlins nominelle, JVM-inspirerte objektmodell og Swifts protokoll- og value-type-orienterte modell trekker i hver sin retning, må teamet velge mellom Kotlin-troskap og Swift-idiomatikk i hver eneste mapping.

**Tags:** `KMP` · `iOS` · `Swift interop` · `Swift Export` · `Språkdesign`

**📹** [Can Kotlin Swift Interop Ever Be Perfect? | Gleb Lukianets](https://www.youtube.com/watch?v=XnPmdTea3VA)
