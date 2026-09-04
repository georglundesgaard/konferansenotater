# Kotlin extension functions - en advarsel fra skyttergravene

*Dag 1, 2. september 2026 · kl 11:00 · Anders Karlsen · 📋 [i programmet](../program.md#d1-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/c1b449a3-139b-4c70-9852-7b203d4ffae0)*

Karlsen fra Jaypro (og JavaZone-arrangør) brukte lyntalen til å advare mot ukritisk bruk av Kotlins extension functions, basert på egne erfaringer. Han anerkjente at muligheten til å legge egne metoder på klasser man ikke kontrollerer – som String – er kul, men pekte på flere feller: en uskyldig utseende getter kan skjule nettverks- eller databasekall som plutselig tar minutter i en løkke, og logikken i en klasse kan bli spredt utover titalls filer slik at det som ser ut som en liten klasse med to metoder i realiteten har 200 – noe som undergraver objektorienteringen og gjør refaktorering smertefull.

Han advarte spesielt mot inline extension functions: siden koden limes inn ved kompilering, peker stack tracer ved exceptions til feil linjenummer – lite gøy ved produksjonsfeil midt på natta. Extension functions på generiske lister er også farlige, fordi ulike typeparametre kompileres til samme statiske metode og gir kompileringsfeil IDE-en ikke alltid fanger opp; utveien med @JvmName gjør refaktorering vond. Rådene hans: legg heller metoden inn i klassen når du eier den, ikke skjul IO bak extensions, «ikke lyv» for den som leser koden etterpå – og spar extension functions til klasser du faktisk ikke kontrollerer, som eksterne biblioteker og String, der de fungerer utmerket.

**Tags:** `Lyntale` · `Kotlin` · `Språkdesign` · `Performance` · `JVM`

**📹** [Kotlin extension functions – en advarsel – Anders Karlsen](https://vimeo.com/1223334643)

*[← JavaZone 2026](../README.md)*
