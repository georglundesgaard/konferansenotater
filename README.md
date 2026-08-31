# Konferansenotater

Personlige notater fra konferanser jeg har vært på – sammendrag av foredrag, egne observasjoner, tags og lenker til opptak. Skrevet på norsk.

## Konferanser

- **[JavaZone 2026](JavaZone/2026/README.md)** — Lillestrøm, 2.–3. september 2026
- **[SmidigDig 2026](SmidigDig/2026/README.md)** — Oslo, 27. mai 2026
- **[KotlinConf 2026](KotlinConf/2026/README.md)** — München, 21.–22. mai 2026

Hver konferanse har sin egen README med Topp 5-anbefalinger, deltakelsesliste og ønskeliste. Klikk deg videre inn til én fil per foredrag.

## Mappestruktur

```
konferansenotater/
├── _mal/                          # Maler for nye konferanser
│   ├── README.md                  #   – konferanse-README
│   └── talks/HHMM-slug.md         #   – én talk-fil
├── <Konferanse>/<ÅÅÅÅ>/
│   ├── README.md                  # Konferanse-oversikt: Topp 5, deltakelse, ønskeliste, kilder
│   ├── program.md                 # (valgfri) Lokal cache av offisielt program – offline-matching
│   ├── plan-dagN.md               # (valgfri) Personlig timeplan per dag, fra /planlegg-dagen
│   └── talks/
│       ├── day1-HHMM-slug.md      # Ett foredrag per fil (flerdags-konferanse)
│       └── HHMM-slug.md           # Ett foredrag per fil (endags-konferanse)
└── README.md                      # Denne filen
```

## Skills

Repoet har prosjekt-skills i `.claude/skills/` som automatiserer arbeidsflyten (kjøres som `/kommando` i Claude Code):

- **`/ny-konferanse <url>`** — sett opp en ny konferanse fra forside- eller program-URL: scaffold, README-ingress med sted/datoer/kilder, og lokal programcache i `program.md`.
- **`/nytt-foredrag`** — registrer et foredrag under/etter konferansen. Ta med en fri beskrivelse (`/nytt-foredrag gunnar morling parquet`); skillen matcher mot programmet (lokal `program.md` først, ellers nettsiden), antar dagens dato, og looper til du er ferdig.
- **`/planlegg-dagen`** — kvelden før / på morgenen: velg foredrag per tidsluke og få en personlig timeplan i `plan-dagN.md`. Kollisjoner kan registreres rett i ønskelisten.
- **`/berik-foredrag`** — etter konferansen, når opptakene er ute: fyller inn sammendrag i talk-filer basert på videoene, og foreslår Topp 5 til README-en.
- **`/video-sjekk`** — sjekker om utestående opptak har blitt publisert og lenker dem inn. Egner seg som ukentlig rutine via `/schedule`.
- **`/konferanse-stats`** — nøkkeltall på tvers av konferansene: antall foredrag, attended vs. interest, videodekning, tag-fordeling.

Typisk livssyklus: `/ny-konferanse` → `/planlegg-dagen` → `/nytt-foredrag` (under konferansen) → `/video-sjekk` (ukene etter) → `/berik-foredrag` → Topp 5.

## Format for et foredrag

Skjelettet for en talk-fil er definert i [`_mal/talks/HHMM-slug.md`](_mal/talks/HHMM-slug.md) – det er den kanoniske kilden. Kort oppsummert: tittel, metadata-linje med tilbakelenke, sammendrag (1–7 setninger, én paragraf – eller en placeholder til `/berik-foredrag` kjøres), eventuelle egne notater, tags, og en `**📹**`-linje med video-lenke eller status.

Metadata-linjen bruker `Dag {N}, {dato}` for flerdagskonferanser og bare `{dato}` for endagskonferanser. Filnavn: `HHMM-slug.md` (endags) eller `dayN-HHMM-slug.md` (flerdags).

## Tag-vokabular

Holdes konsistent på tvers av konferanser:

- **Format:** `Keynote` · `Lyntale` · `Live demo` · `Live coding` · `Casestudie` · `Underholdning` · `Panel`
- **Tema:** `AI` · `LLM` · `AI-agenter` · `Backend` · `Frontend` · `Web` · `Mobil` · `Performance` · `Testing` · `Tooling` · `Build tools` · `Språkdesign` · `Database` · `Observability` · `API-design` · `Arkitektur` · `Skala` · `Feilhåndtering` · `Karriere`
- **Tek:** `Kotlin 2.4` · `Compose` · `Compose Multiplatform` · `KMP` · `Ktor` · `Spring Boot` · `Coroutines` · `Kotlin/Wasm` · `Kotlin/Native` · `iOS` · `Android` · `JVM` · `Koog` · `MCP`

Listen er ikke uttømmende — legg til nye tags etter behov.

## Ny konferanse

Enkleste vei: `/ny-konferanse <url til konferansen eller programmet>` — setter opp mappen, fyller README-en med fakta fra nettsiden og cacher programmet lokalt. (`/nytt-foredrag` sitt «Ny konferanse»-valg gjør det samme.)

Manuelt:

```sh
mkdir -p "<Konferanse>/<ÅÅÅÅ>/talks"
cp _mal/README.md "<Konferanse>/<ÅÅÅÅ>/README.md"
touch "<Konferanse>/<ÅÅÅÅ>/talks/.gitkeep"
# Fyll ut README.md. Talk-filer opprettes fra _mal/talks/HHMM-slug.md
# (én kopi per foredrag – ikke kopier selve malfilen inn i talks/).
```

Plassholdere i malen er på formen `<Konferanse>`, `<ÅÅÅÅ>`, `<HHMM>` og `<slug>` — enkle å finne med søk og erstatt.
