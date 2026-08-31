# Talking to terminals (and how they talk back)

*[← KotlinConf 2026](../README.md) · Dag 1, 21. mai 2026 · kl 16:15 · Jake Wharton*

Jake Wharton tar oss med på et dypdykk i hvordan CLI-programmer faktisk snakker med moderne terminaler, langt utover det å skrive ut tekst i en farge. Han rammer inn terminal-I/O gjennom ANSI-escape-sekvenser, kontrollkoder, terminfo-databasen og innkommende input som må parses byte for byte, og viser hvor stor forskjell det er mellom Windows-konsollen og Unix-pty-er.

Kjernen i foredraget er hans egen Mosaic, en Compose-basert TUI-stack for Kotlin, sammen med det underliggende mosaic-terminal-laget som nå kjører en egenutviklet parser slik at KMP-apper får lik oppførsel både på JVM og Kotlin/Native. Wharton går gjennom praktiske fallgruver: hvordan man leser museklikk og utvidede tastetrykk via Kitty-keyboardprotokollen, hvordan man reagerer momentant på resize-, fokus- og temaendringer, og hvorfor terminfo ofte lyver om hva terminalen faktisk støtter.

Underveis viser han levende demoer med bilder rendret rett i terminalen, jevn frame sync, og små interaktive apper bygd rundt `runMosaic` og Compose-state-håndtering. Hovedlærdommen for Kotlin-utviklere som lager CLI- eller TUI-verktøy er å ikke skrive sitt eget escape-lag fra bunnen, men heller bygge på Mosaic og den delte Multiplatform-terminalabstraksjonen slik at OS-forskjellene og de kroniske edge-casene håndteres én gang for alle.

**Notater fra konferansen:**
- Morsomt teknisk foredrag

**Tags:** `TUI` · `CLI` · `Mosaic` · `Compose` · `KMP` · `Dypdykk`

**📹** [Talking to terminals (and how they talk back) – Jake Wharton](https://www.youtube.com/watch?v=QYlzKV0Oe1A)
