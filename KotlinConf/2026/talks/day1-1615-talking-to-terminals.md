# Talking to terminals (and how they talk back)

*Dag 1, 21. mai 2026 · kl 16:15 · Jake Wharton · 📋 [i programmet](../program.md#d1-1615) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1084621/)*

Jake Wharton tar oss med på et dypdykk i hvordan CLI-programmer faktisk snakker med moderne terminaler, langt utover det å skrive ut tekst i en farge. Han rammer inn terminal-I/O gjennom ANSI-escape-sekvenser, kontrollkoder, raw/cooked mode, isatty og TTY-devicen, og innkommende input som må parses byte for byte – mens Windows-konsollen ifølge ham er «et eget 45-minutters foredrag» han bevisst lot ligge.

Kjernen i foredraget er hans egen Mosaic, en Compose-basert TUI-stack for Kotlin, sammen med det underliggende mosaic-terminal-laget som nå kjører en egenutviklet parser slik at KMP-apper får lik oppførsel både på JVM og Kotlin/Native. Wharton går gjennom praktiske fallgruver: hvordan man leser museklikk og utvidede tastetrykk ved å aktivere egne moduser, hvordan man reagerer momentant på resize-, fokus- og temaendringer, og hvorfor man må spørre terminalen direkte om hva den støtter – ulike terminaler svarer helt ulikt på de samme forespørslene.

Underveis viser han levende demoer med bilder rendret rett i terminalen og små interaktive apper bygd rundt `runMosaic` og Compose-state-håndtering. Hovedlærdommen for Kotlin-utviklere som lager CLI- eller TUI-verktøy er å ikke skrive sitt eget escape-lag fra bunnen, men heller bygge på Mosaic og den delte Multiplatform-terminalabstraksjonen slik at OS-forskjellene og de kroniske edge-casene håndteres én gang for alle. Han avslutter med en viktig advarsel: tekst er ikke automatisk tilgjengelig – TUI-rammeverk som repainter hele skjermen (slik mange LLM-verktøy gjør) er nærmest ubrukelige med skjermleser, mens diff-baserte oppdateringer à la Vim fungerer. Sett live: et morsomt og imponerende teknisk foredrag, live-kodet fra ende til annen.

**Tags:** `TUI` · `CLI` · `Mosaic` · `Compose` · `KMP` · `Dypdykk`

**📹** [Talking to terminals (and how they talk back) – Jake Wharton](https://www.youtube.com/watch?v=QYlzKV0Oe1A)

*[← 1515 Why Most AI Agents Never Scale?](day1-1515-why-ai-agents-never-scale-koog.md) · [1715 Robocoders: The [K]agematch →](day1-1715-robocoders-kagematch.md)*
