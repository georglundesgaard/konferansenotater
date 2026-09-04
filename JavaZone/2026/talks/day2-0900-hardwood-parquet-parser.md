# Hardwood: Building a Parquet Parser From Scratch (With a Little Help From AI)

*Dag 2, 3. september 2026 · kl 09:00 · Gunnar Morling · 📋 [i programmet](../program.md#d2-0900) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/268b3ef0-ff34-4c5d-b856-3c9a807c5168)*

Morling presenterte Hardwood, et nytt bibliotek han har bygget siden nyttår for å lese – og fra denne uken også skrive – Apache Parquet-filer på JVM-en uten å dra inn hele Hadoop-økosystemet. Han startet med en innføring i kolonneorienterte filformater: hvordan Parquet lagrer data kolonne for kolonne i row groups, column chunks og pages, muliggjør effektive kodinger som run length- og delta-koding, støtter nøstede data via definisjons- og repetisjonsnivåer, og hvorfor formatet dominerer i datasjøer som Iceberg og Delta Lake. Motivasjonen var todelt: eksisterende Parquet-Java har et tungt avhengighetsfotavtrykk (fort over 100 JAR-er, med versjonskonflikter og forsyningskjederisiko) og er entrådet, mens moderne maskiner har mange kjerner.

Hardwood tilbyr både et radbasert API med lettvekts cursor-mønster som unngår objektallokering og autoboxing, og et kolonnebasert API som leverer batcher JIT-kompilatoren kan vektorisere, pluss predicate pushdown med filtre og statistikk. Nøkkelen til skalering er parallellisering på page-nivå, og biblioteket utnytter moderne Java-funksjoner som virtuelle tråder, Vector API, JFR-events og GraalVM-binærer for en lynrask CLI/TUI. Benchmarks på NYC-taxidata viste at Hardwood er raskere enn Parquet-Java både på én kjerne og betydelig raskere på flere, og en spesialoptimalisering for lister med fast lengde (f.eks. vektorembeddinger) ga 2–3,7 ganger raskere lesing.

Prosjektet er tungt AI-bygget, og Morling delte erfaringene: lavnivåkode med en klar spesifikasjon og en omfattende testsuite (differensiell testing mot Parquet-Java og DuckDB) er en ypperlig match for verktøy som Claude Code, og AI endrer «bygg selv vs. gjenbruk»-kalkylen – han one-shottet for eksempel S3-signering i stedet for å dra inn AWS SDK. Samtidig advarte han mot vibe-koding: verktøyene dupliserer kode, deaktiverer feilende tester, og fungerer som en multiplikator – de forsterker styrkene til en senior utvikler, men også sloppen til en slurvete en. Selv holder han full kontroll på arkitektur og API-design, og bruker en Claude-skill basert på sin «code review pyramid».

**Tags:** `Java` · `Performance` · `AI` · `Live coding` · `JVM` · `Database` · `Tooling`

**📹** [Hardwood – Gunnar Morling](https://vimeo.com/1223604291)

*[← JavaZone 2026](../README.md)*
