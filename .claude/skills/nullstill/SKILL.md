---
name: nullstill
description: Use when someone has forked this repo and wants to reset it for their own use — wash away the original author's notes and data while keeping skills, templates and site structure. Triggers: "nullstill", "reset forken", "bruk verktøyet selv", "fjern notatene".
---

# nullstill

Nullstiller en fork: fjerner originalforfatterens konferansenotater og persondata, beholder skills, maler og struktur, og peker repo-URL-ene til forkerens eget repo. Brukerens språk: norsk.

Bruk: `/nullstill` – kjøres i forken, rett etter fork/clone.

## Steps

1. **Fork-vakt.** Kjør `git remote get-url origin`. Peker den på originalrepoet (`georglundesgaard/konferansenotater`), stopp: «Dette ser ut som originalrepoet – /nullstill er laget for forks.» Ellers: utled `<bruker>/<repo>` fra remote-URL-en; Pages-URL antas `https://<bruker>.github.io/<repo>/`.

2. **Kartlegg og vis plan – FØR noe røres.** List konferansemappene (toppnivåmapper som inneholder årsmapper med `talks/`). Spør via `AskUserQuestion` hva som skal skje med hver: «Slett helt» eller «Behold uten notater» (aktuelt når forkeren selv skal på konferansen – programcachen gjenbrukes). Vis deretter en samlet plan: hva som slettes, hva som vaskes, hva som endres i forsidene – og krev eksplisitt ja på planen før noe som helst slettes eller endres. At brukeren ba om nullstilling, er IKKE bekreftelse på planen: omfanget (antall filer, hvilke mapper) skal være sett og godkjent først.

3. **Slett konferanser valgt for sletting** – hele mappen inkludert årgangsindeksen (`<Konferanse>/README.md`).

4. **Vask konferanser som beholdes:**
   - Slett alle filer i `talks/` (legg tilbake `.gitkeep`) og alle `plan-dag*.md`.
   - `program.md`: fjern radklassene (`attended`/`wishlist`), ✅/👀-badgene, 📝-notatlenkene og all tekst i Notater-cellene (lenkene ville pekt på slettede filer). Behold foredragsbeskrivelser, meta-linjer og tegnforklaringen – konvensjonen vedlikeholdes videre av skills.
   - Konferanse-README: behold faktaingress (sted, datoer, format/spor), programlenke og Kilder. Fjern førstepersonsformuleringer i ingressen, «Min plan»-linjen og eventuell «Oppsummering»-seksjon. Tøm «Foredrag jeg gikk på», ønskelisten og Topp 5 til plassholdere som i `_mal/README.md`.

5. **Nullstill forsidene og URL-ene.**
   - `README.md` og `index.md`: reduser konferanselisten til det som består – eller `*(ingen ennå – kjør /ny-konferanse)*` hvis alt ble slettet. Sett badges til faktisk tilstand (`konferanser-<N>`, `foredrag-0`).
   - Bytt alle forekomster av originalens `<bruker>/<repo>` (badge-URL-er, commit-lenke, Pages-lenker, index-footeren) til forkerens.
   - Tag-vokabularet i rot-README: behold **Format**- og **Tema**-linjene (skills leser seksjonen), men erstatt **Tek**-linjen med en nøytral startliste (`Java` · `Kotlin` · `Spring Boot` · `JVM` · `MCP`) – den gamle er akkumulert fra originalforfatterens notater.

6. **Rapportér.** Oppsummer slettet/vasket/endret, og verifiser med grep at originalens brukernavn ikke forekommer noe sted. Minn forkeren på at originalnotatene fortsatt ligger i git-historikken (bevisst valg – de er offentlige fra før). Ikke commit – la forkeren committe selv (f.eks. «Nullstilt for egen bruk») og kjøre `/ny-konferanse <url>` som neste steg.

## Ikke gjør

- ALDRI slett eller endre noe før brukeren har sett den samlede planen og bekreftet – «nullstill»-oppdraget i seg selv er ikke bekreftelse, og skjønnsvalg om omfang tas ikke på egen hånd.
- Ikke rør `.claude/skills/`, `_mal/`, `_layouts/`, `_includes/`, `assets/`, `_config.yml`, `Gemfile`, `.gitignore`, `404.md` eller dokumentasjonsseksjonene i rot-README (Skills, Tips, Format, Tag-vokabular-strukturen).
- Ikke skriv om git-historikken.
- Ikke commit eller push.
