# Konferansenotater

Personlige notater fra konferanser jeg har vært på – sammendrag av foredrag, egne observasjoner, tags og lenker til opptak når de blir publisert. Skrevet på norsk.

## Konferanser

- **[KotlinConf 2026](KotlinConf/2026/)** – München, 21.–22. mai 2026
- **[SmidigDig 2026](SmidigDig/2026/)** – Oslo, 27. mai 2026

## Mappestruktur

```
konferansenotater/
├── _mal/                      # Maler for nye konferanser
├── <Konferanse>/
│   └── <ÅÅÅÅ>/
│       ├── <Konferanse> <ÅÅÅÅ>.md                       # Hovedsammendrag
│       ├── <Konferanse> <ÅÅÅÅ> - talks attended.md      # Liste over foredrag jeg gikk på
│       └── <Konferanse> <ÅÅÅÅ> - talks interest.md      # Foredrag jeg vil se opptak av
└── README.md
```

Hver konferanse får sin egen mappe, med en undermappe per år.

## Filtypene

**`<Konferanse> <ÅÅÅÅ> - talks attended.md`** – kort, råtekstaktig liste over foredragene jeg deltok på, med kjappe stikkord under hvert. Brukes som arbeidsfil under konferansen.

**`<Konferanse> <ÅÅÅÅ> - talks interest.md`** – foredrag som ble droppet på grunn av parallelle spor eller andre kollisjoner, og som jeg vil se på opptak senere.

**`<Konferanse> <ÅÅÅÅ>.md`** – hovedsammendraget. Hvert foredrag har sin egen `###`-blokk:

```markdown
### HHMM Tittel — Presenter(s)

Sammendrag (1–3 setninger fra det offisielle programmet).

**Notater fra konferansen:**       (kun for foredrag jeg var på)
- Punkt 1
- Punkt 2

**Tags:** `tag1` · `tag2` · `tag3`

**📹** Video-lenke eller status.
```

## Tag-vokabular

For å holde det konsistent på tvers av konferanser brukes følgende vokabular:

- **Format:** `Keynote` · `Lyntale` · `Live demo` · `Casestudie` · `Underholdning`
- **Tema:** `AI` · `LLM` · `AI-agenter` · `Backend` · `Frontend` · `Web` · `Mobil` · `Performance` · `Testing` · `Tooling` · `Build tools` · `Språkdesign` · `Database` · `Observability` · `API-design` · `Arkitektur` · `Skala`
- **Tek:** `Kotlin 2.4` · `Compose` · `KMP` · `Ktor` · `Spring Boot` · `Coroutines` · `Kotlin/Wasm` · `Kotlin/Native` · `iOS` · `Android` · `JVM`

Listen er ikke uttømmende – legg til nye tags etter behov.

## Bruke malen

Kopier malen og bytt ut plassholderne:

```sh
cp -r _mal/. "<Konferanse>/<ÅÅÅÅ>/"
# rename filer og rediger innhold
```

Plassholdere i malen er på formen `<Konferanse>`, `<ÅÅÅÅ>` og `<HHMM>` – enkle å finne med søk og erstatt.
