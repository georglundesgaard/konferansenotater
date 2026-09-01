# Dissecting Kotlin: 2026

*Dag 2, 22. mai 2026 · kl 10:15 · Huyen Tue Dao · 📋 [i programmet](../program.md#d2-1015) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1110200/)*

Ti år etter Kotlin 1.0 tar Huyen Tue Dao publikum gjennom et knippe ferske stabile og forhåndsvisningsfunksjoner – med hovedvekt på context parameters som stabiliseres i Kotlin 2.4, sammen med tilhørende KEEP-forslag og andre nyheter fra språkets siste utviklingsrunder.

Hennes signaturmetode er å bruke både design og implementasjon som linse: hun leser KEEP-diskusjonene for å forstå hvorfor komiteen valgte som de gjorde, og dissekerer deretter den genererte bytekoden for å vise hva funksjonen faktisk koster og betyr på JVM. Underveis peker hun på konkrete overraskelser – som hvordan context parameters måtte erstatte context receivers etter praktiske problemer, og hvilke fallgruver som oppstår når kildekoden ser elegant ut mens kompilatoren gjør noe helt annet bak kulissene.

Hun leser dette som et signal om at Kotlin nå prioriterer ekspressiv, kontekstsensitiv kode og mer disiplinert språkdesign framfor rene syntaktiske godbiter. Hovedbudskapet er at Kotlin-utviklere blir bedre av å lese både KEEP-forslag og bytekode: å forstå hvordan en funksjon ble designet og hvordan den lander i praksis, gjør deg til en tydeligere forfatter av din egen Kotlin.

**Tags:** `Kotlin 2.4` · `Context parameters` · `KEEP` · `Språkdesign` · `Dypdykk`

**📹** [Dissecting Kotlin: 2026 – Huyen Tue Dao](https://www.youtube.com/watch?v=PB2YYHpEhkQ)

*[← Dag 2, 0900 We were meant to be](day2-0900-we-were-meant-to-be.md) · [1115 Idiomatic Kotlin, Spring Boot 4 →](day2-1115-idiomatic-kotlin-spring-boot-4.md)*
