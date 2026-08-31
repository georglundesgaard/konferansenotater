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
│   └── talks/
│       ├── day1-HHMM-slug.md      # Ett foredrag per fil (flerdags-konferanse)
│       └── HHMM-slug.md           # Ett foredrag per fil (endags-konferanse)
└── README.md                      # Denne filen
```

## Format for et foredrag

Hver talk-fil følger samme skjelett:

```markdown
# {Tittel}

*[← {Konferanse} {år}](../README.md) · Dag {N}, {dato} · kl {tid} · {Taler(e)}*

Sammendrag (1–7 setninger, én paragraf).

**Notater fra konferansen:**       (kun for foredrag jeg var på)
- Punkt 1
- Punkt 2

**Tags:** `tag1` · `tag2` · `tag3`

**📹** Video-lenke eller status.
```

## Tag-vokabular

Holdes konsistent på tvers av konferanser:

- **Format:** `Keynote` · `Lyntale` · `Live demo` · `Live coding` · `Casestudie` · `Underholdning` · `Panel`
- **Tema:** `AI` · `LLM` · `AI-agenter` · `Backend` · `Frontend` · `Web` · `Mobil` · `Performance` · `Testing` · `Tooling` · `Build tools` · `Språkdesign` · `Database` · `Observability` · `API-design` · `Arkitektur` · `Skala` · `Feilhåndtering` · `Karriere`
- **Tek:** `Kotlin 2.4` · `Compose` · `Compose Multiplatform` · `KMP` · `Ktor` · `Spring Boot` · `Coroutines` · `Kotlin/Wasm` · `Kotlin/Native` · `iOS` · `Android` · `JVM` · `Koog` · `MCP`

Listen er ikke uttømmende — legg til nye tags etter behov.

## Bruke malen

Kopier malen og bytt ut plassholderne:

```sh
cp -R _mal/. "<Konferanse>/<ÅÅÅÅ>/"
# Fyll ut README.md og legg én fil per foredrag under talks/.
```

Plassholdere i malen er på formen `<Konferanse>`, `<ÅÅÅÅ>`, `<HHMM>` og `<slug>` — enkle å finne med søk og erstatt.
