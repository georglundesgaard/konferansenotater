# Snake in 10 Lines: Learning More by Coding Less

*Dag 1, 2. september 2026 · kl 18:20 · Guus de Wit · 📋 [i programmet](../program.md#d1-1820) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/9121cedf-00e2-478c-833d-3f1554a55bc9)*

De Wit tok utgangspunkt i konseptet «six-word stories» og satte seg som utfordring å skrive Snake i bare ti linjer kode (maks 130 tegn per linje, kun JDK-et, ingen eksterne biblioteker), i Kotlin – uten noen gang å ha laget et spill før. Han definerte spillet i seks ord («Snake moves, steers, eats, grows, dies») og bygde det først fritt: terminalutskrift viste seg utilstrekkelig for sanntids tastaturinput, så han lærte seg Swing (KeyAdapter, JTextArea og JFrame) og krympet boilerplaten fra 40+ linjer til tre.

Nedskaleringen drev frem stadig smartere løsninger: snake-bevegelse ble redusert til «legg til nytt hode, fjern halen», og det virkelige gjennombruddet var å droppe 2D-koordinater helt og representere brettet som én endimensjonal liste av heltall, der Swings line wrap får det til å se ut som 2D. Med inlining, generateSequence i stedet for while-løkker og en del kreativ tegnsparing endte han på nøyaktig ti linjer – og laget siden varianter på 120 og til og med 80 tegn per linje. Han rakk også å fikse en ekte bugg (å snu rett inn i seg selv), la poengsum i exit-koden, og viste at samme ti-linjers struktur med små endringer gir Pong, Breakout og Tetris – pluss en «leet»-variant på 1337 tegn totalt, og en Java-versjon på spørsmål fra salen.

Hovedbudskapene var tre: du lærer ved å gjøre det selv i stedet for å kopiere fra nettet eller en agent; begrensninger skaper kreativitet – den første løsningen er sjelden den beste; og konsishet gir forståelse, både i kode og i spesifikasjoner. Kodene ligger åpent på GitHub som invitasjon til å prøve selv.

**Tags:** `Kotlin` · `Live coding` · `Underholdning` · `JVM` · `Språkdesign`

**📹** [Snake in 10 Lines: Learning More by Coding Less – Guus de Wit](https://vimeo.com/1223467159)

*[← JavaZone 2026](../README.md)*
