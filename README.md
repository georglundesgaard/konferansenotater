# Konferansenotater

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-2ea44f?logo=github)](https://georglundesgaard.github.io/konferansenotater/)
[![Sist oppdatert](https://img.shields.io/github/last-commit/georglundesgaard/konferansenotater?label=sist%20oppdatert)](https://github.com/georglundesgaard/konferansenotater/commits/main)
[![Konferanser](https://img.shields.io/badge/konferanser-3-blue)](https://georglundesgaard.github.io/konferansenotater/)
[![Foredrag](https://img.shields.io/badge/foredrag-102-blue)](https://georglundesgaard.github.io/konferansenotater/)
[![Språk](https://img.shields.io/badge/spr%C3%A5k-norsk-red)](README.md)
[![Lisens](https://img.shields.io/github/license/georglundesgaard/konferansenotater?label=lisens)](#lisens)

Personlige notater fra konferanser jeg deltar på – sammendrag av foredrag, egne observasjoner, tags og lenker til opptak. Skrevet på norsk.

## Konferanser

- **[JavaZone 2026](JavaZone/2026/README.md)** — Lillestrøm, 2.–3. september 2026
- **[SmidigDig 2026](SmidigDig/2026/README.md)** — Oslo, 27. mai 2026
- **[KotlinConf 2026](KotlinConf/2026/README.md)** — München, 21.–22. mai 2026

Hver konferanse har sin egen README med deltakelsesliste og ønskeliste – konferanser med parallelle spor har i tillegg Topp 5-anbefalinger fra ønskelisten. Klikk deg videre inn til én fil per foredrag.

## Mappestruktur

```
konferansenotater/
├── _mal/                          # Maler for nye konferanser
│   ├── README.md                  #   – konferanse-README
│   └── talks/HHMM-slug.md         #   – én talk-fil
├── _utkast/                       # Utkast til blogginnlegg o.l. (upublisert av Jekyll)
├── blogg/                         # Publiserte blogginnlegg (lenket fra index.md)
├── <Konferanse>/
│   ├── README.md                  # Årgangsindeks for konferansen
│   └── <ÅÅÅÅ>/
│       ├── README.md              # Konferanse-oversikt: Topp 5, deltakelse, ønskeliste, kilder
│       ├── program.md             # (valgfri) Lokal cache av offisielt program – offline-matching
│       ├── plan-dagN.md           # (valgfri) Timeplan per dag, fra /planlegg-dagen; slettes av /avslutt-konferanse
│       ├── _notater/              # Rånotater arkivert ordrett etter verifisert beriking (upublisert)
│       │   └── <slug>.md
│       └── talks/
│           ├── day1-HHMM-slug.md  # Ett foredrag per fil (flerdags-konferanse)
│           └── HHMM-slug.md       # Ett foredrag per fil (endags-konferanse)
└── README.md                      # Denne filen
```

## Skills

Repoet har prosjekt-skills i `.claude/skills/` som automatiserer arbeidsflyten (kjøres som `/kommando` i Claude Code). Andre kodeagenter (Codex, Cursor, Gemini m.fl.) plukker opp de samme arbeidsflytene via [AGENTS.md](AGENTS.md), som peker dem til skill-filene:

- **`/ny-konferanse <url>`** — sett opp en ny konferanse fra forside- eller program-URL: scaffold, README-ingress med sted/datoer/kilder, og lokal programcache i `program.md`.
- **`/nytt-foredrag`** — registrer et foredrag under/etter konferansen. Ta med en fri beskrivelse (`/nytt-foredrag gunnar morling parquet`); skillen matcher mot programmet (lokal `program.md` først, ellers nettsiden), antar dagens dato, og looper til du er ferdig.
- **`/planlegg-dagen`** — kvelden før / på morgenen: velg foredrag per tidsluke og få en personlig timeplan i `plan-dagN.md`. Kollisjoner kan registreres rett i ønskelisten.
- **`/berik-foredrag`** — etter konferansen, når opptakene er ute: fyller inn sammendrag i talk-filer basert på videoene, og foreslår Topp 5 til README-en.
- **`/oppdater-program`** — sjekker om det offisielle konferanseprogrammet har endret seg og oppdaterer `program.md`-cachen; melder fra hvis registrerte foredrag er berørt.
- **`/avslutt-konferanse`** — rett etter siste konferansedag: kvalitetssjekk av notatene, «Oppsummering»-seksjon i konferanse-README-en (med din godkjenning) og opprydding av dagsplanene.
- **`/video-sjekk`** — sjekker om utestående opptak har blitt publisert og lenker dem inn. Egner seg som ukentlig rutine via `/schedule`.
- **`/topp-5`** — foreslår eller regenererer «Anbefalt: Topp 5» fra ønskelisten basert på temaene du faktisk fulgte; kjøres helst etter `/berik-foredrag`.
- **`/konferanse-stats`** — nøkkeltall på tvers av konferansene: antall foredrag, deltatt vs. ønskeliste, videodekning, tag-fordeling.
- **`/nullstill`** — for forks: vasker bort notatene og dataene mine, beholder skills/maler/struktur og peker sidene til din fork (se «Bruk verktøyet selv»).

Typisk livssyklus: `/ny-konferanse` → `/planlegg-dagen` → `/nytt-foredrag` (under konferansen) → `/avslutt-konferanse` → `/video-sjekk` (ukene etter) → `/berik-foredrag` → `/topp-5`.

## Tips og triks

**Før konferansen:**
- Sett opp konferansen med `/ny-konferanse <url>` så snart programmet er publisert – da får du både mappe, README og lokal programcache i én operasjon.
- Kvelden før hver dag: kjør `/planlegg-dagen` og plukk foredrag per tidsluke. Foredrag du ikke rekker på grunn av kollisjoner, havner rett i ønskelisten.
- Commit gjerne planen med en gang, men vent med å pushe til dagen er i gang – en pushet dagsplan forteller offentlig hvor du kommer til å være.
- Kjør `/oppdater-program` på morgenen – programmer endres gjerne siste døgn, og cachen bør stemme med virkeligheten før du registrerer noe.

**Under konferansen:**
- Registrer foredrag i pausene med `/nytt-foredrag <noen stikkord>` – skillen matcher mot den lokale programcachen (fungerer på dårlig konferanse-WiFi), så et par ord om tittel eller taler holder. Den spør «Ett til?» så du kan ta hele formiddagen i én kjøring.
- Ikke skriv sammendrag selv – lim inn stikkordsnotater og la placeholder-linjen stå. `/berik-foredrag` skriver sammendraget fra opptaket senere.
- Commit og push på slutten av dagen – notatene ligger da på nettsiden samme kveld.

**Etter konferansen:**
- Rett etter siste dag: kjør `/avslutt-konferanse` – kvalitetssjekk, oppsummering og opprydding mens inntrykkene er ferske.
- Sett opp `/video-sjekk` som ukentlig rutine med `/schedule` til alle opptakene er publisert og lenket inn.
- Når opptakene er ute: kjør `/berik-foredrag` – den skriver sammendrag fra videoene (dine egne notater røres aldri) – og avslutt med `/topp-5` for oppdaterte anbefalinger.
- `/konferanse-stats` gir deg tall og tag-fordeling på tvers av alle konferansene når du vil ha oversikt.

## Format for et foredrag

Skjelettet for en talk-fil er definert i [`_mal/talks/HHMM-slug.md`](_mal/talks/HHMM-slug.md) – det er den kanoniske kilden. Kort oppsummert: tittel, metadata-linje (dag, tid, taler), sammendrag (1–3 korte avsnitt – eller en placeholder til `/berik-foredrag` kjøres), eventuelle egne notater, tags, og en `**📹**`-linje med video-lenke eller status. Notatblokken har en livssyklus: den bor i talk-filen fra `/nytt-foredrag` til `/berik-foredrag` har verifisert punktene mot opptaket og flettet dem inn i sammendraget – deretter arkiveres rånotatene ordrett i `<Konferanse>/<År>/_notater/<slug>.md` (upublisert understrek-mappe), med kursiverte merknader ved korreksjoner. Statuslinjer uten eget opptak har tre godkjente varianter – skills gjenkjenner nøyaktig disse: «Video ikke publisert ennå – se [kilde]», «Individuell video ikke publisert ennå – se [kilde]» og «Inngår i [samlesending] – individuell video forventet senere.»

Metadata-linjen bruker `Dag {N}, {dato}` for flerdagskonferanser og bare `{dato}` for endagskonferanser, og kan avsluttes med en ankerlenke inn i `program.md`. Filnavn: `HHMM-slug.md` (endags) eller `dayN-HHMM-slug.md` (flerdags).

Foredrag i «gikk på»-listen avsluttes med en forrige/neste-navigasjonslinje (`*[← <forrige>](<fil>) · [<neste> →](<fil>)*`) i kronologisk rekkefølge; `/nytt-foredrag` vedlikeholder kjeden. `program.md` har for flersporede konferanser én tabell per tidsluke, der tidsluke-headingen bærer ankeret (`<h3 id="d<dag>-<hhmm>">`) som talk-sidene lenker til; enkeltsporede konferanser har én samlet tabell uten tidsluke-ankere.

## Tag-vokabular

Holdes konsistent på tvers av konferanser:

- **Format:** `Keynote` · `Lyntale` · `Live demo` · `Live coding` · `Casestudie` · `Underholdning` · `Panel`
- **Tema:** `AI` · `LLM` · `AI-agenter` · `Backend` · `Frontend` · `Web` · `Mobil` · `Performance` · `Testing` · `Tooling` · `Build tools` · `Språkdesign` · `Database` · `Observability` · `API-design` · `Arkitektur` · `Skala` · `Feilhåndtering` · `Karriere`
- **Tek:** `Kotlin 2.4` · `Compose` · `Compose Multiplatform` · `KMP` · `Ktor` · `Spring Boot` · `Coroutines` · `Kotlin/Wasm` · `Kotlin/Native` · `iOS` · `Android` · `JVM` · `Koog` · `MCP`

Listen er ikke uttømmende – legg til nye tags etter behov.

## Bruk verktøyet selv

Lyst til å bruke opplegget til egne konferansenotater? Fork repoet, åpne forken i Claude Code (eller en annen kodeagent som leser [AGENTS.md](AGENTS.md)), og kjør `/nullstill` – den fjerner notatene og dataene mine, beholder skills/maler/struktur, og peker sidene til din fork. Skal du på en av de samme konferansene, kan du beholde konferansemappen med programcachen (uten notatene). Deretter er `/ny-konferanse <url>` neste steg.

## Ny konferanse

Enkleste vei: `/ny-konferanse <url til konferansen eller programmet>` – setter opp mappen, fyller README-en med fakta fra nettsiden og cacher programmet lokalt. (`/nytt-foredrag` sitt «Ny konferanse»-valg gjør det samme.)

Manuelt:

```sh
mkdir -p "<Konferanse>/<ÅÅÅÅ>/talks"
cp _mal/README.md "<Konferanse>/<ÅÅÅÅ>/README.md"
touch "<Konferanse>/<ÅÅÅÅ>/talks/.gitkeep"
# Fyll ut README.md. Talk-filer opprettes fra _mal/talks/HHMM-slug.md
# (én kopi per foredrag – ikke kopier selve malfilen inn i talks/).
```

Plassholdere i malen er på formen `<Konferanse>`, `<ÅÅÅÅ>`, `<HHMM>` og `<slug>` – enkle å finne med søk og erstatt.

## Lisens

Repoet har tre lag med ulikt eierskap:

- **Verktøyet** – skills (`.claude/`), maler (`_mal/`), sidefiler (`_layouts/`, `_includes/`, `assets/`, konfig) og dokumentasjonen: [MIT](LICENSE). Fork og gjenbruk fritt.
- **Mine notater og sammendrag** – prosaen i talk-filene og konferanse-README-ene: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.no) – del og siter gjerne, med navngivelse.
- **Konferanseinnhold** – offisielle programbeskrivelser, abstracts og omtaler (i `program.md` og details-blokkene) tilhører de respektive konferansene og foredragsholderne. De er gjengitt med kildehenvisning som lokal cache og er **ikke** omfattet av lisensene over.
