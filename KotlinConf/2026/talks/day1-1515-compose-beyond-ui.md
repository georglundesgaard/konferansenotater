# Compose beyond UI : Display and Print!

*[← KotlinConf 2026](../README.md) · Dag 1, 21. mai 2026 · kl 15:15 · Salomon Brys*

Salomon Brys strukturerte lyntalen rundt to konkrete sideprosjekter som viser at Compose kan brukes langt utover vanlige app-grensesnitt: presentasjonsrammeverket CuP (Compose ur Pres), som lar ham programmere lysbilder med de samme komponentene som han bygger UI med til daglig, og Card-Composer, et Compose Desktop-bibliotek for å designe og trykke brettspillkort. For kortprosjektet erstattet han Material-temaet med et eget CardTheme, redefinerte enhetssystemet slik at 1 dp tilsvarer 1 PostScript-punkt (1/72 tomme) for å tenke direkte i millimeter og tommer, og la til `FormattedText` for tag-basert rik tekst tilpasset trykk. Selve rendringen skjer i en `cardComposerApplication()`-funksjon som gir forhåndsvisning og eksportdialog med PNG per kortgruppe og PDF klar for profesjonell trykking med bleed-marger, mens CuP demonstrerer hvordan den samme Compose-kjøretiden animerer kildekode og progressive fremhevninger i stedet for Keynote-slides. Den bærende innsikten er at Compose i praksis er en tegne-motor bundet til Skia – så snart utvikleren peker den mot en PDF- eller bilde-flate i stedet for et vindu, blir hele det deklarative UI-verktøysettet plutselig et fullverdig verktøy for grafisk design og produksjon.

**Tags:** `Lyntale` · `Compose Multiplatform` · `Kreativt` · `PDF` · `Print`

**📹** [Compose beyond UI: Display and Print! | Salomon Brys](https://www.youtube.com/watch?v=gi3R122UpgM)
