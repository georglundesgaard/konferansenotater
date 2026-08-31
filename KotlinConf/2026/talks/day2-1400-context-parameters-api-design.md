# Context parameters and API design

*[← KotlinConf 2026](../README.md) · Dag 2, 22. mai 2026 · kl 14:00 · Alejandro Serrano Mena*

Context parameters ble stabilisert i Kotlin 2.4 og skrives foran signaturen som `context(users: UserService) fun User.getFriends()`, slik at verdien tres implisitt gjennom kallkjeden uten manuell videresending på hvert nivå. Serrano Mena bruker en teater-metafor – «spotlight-prinsippene» – for å skille hovedroller (mottakere, `this`) fra biroller (context parameters): en mottaker kan fylle et kontekstargument implisitt, men aldri motsatt, og Kotlin begrenser bevisst antall «hovedroller» på scenen for å unngå at det implisitte scopet blir uoversiktlig, slik det tidligere context receivers-forslaget led under.

Context parameters egner seg best i to mønstre: usynlige kontekster som `Logger` eller Arrows `Raise` (der understreknavnet `_` kan brukes), og «leaf-only»-tjenester som `UserService` eller sjekker-kontekster i selve Kotlin-kompilatoren – altså typesikker, «fattigmanns» dependency injection, transaksjons-, logg- og autorisasjonsscoper. Byggere og DSL-er som `buildList` eller `kotlinx.html` skal derimot forbli mottakere, for objektet som bygges er hovedrollen på scenen, og bruk av `DslMarker` og nøsting bryter ellers sammen.

Anti-mønsteret Serrano advarer mot er «bridge function hell» – å duplisere hele API-et både som medlemmer/extensions på writer-typen og som kontekstuelle funksjoner – og å konvertere alt fra mottakere til context parameters bare fordi språket nå tillater det; når rekkefølgen på mottakere skaper trøbbel i rekursive kall, bør man heller lage små «dance»-hjelpere som gjør `with { ... }`-vendingen for kalleren. Hovedbudskapet til API-designere er derfor konseptuelt, ikke syntaktisk: velg mottaker når verdien fortjener rampelyset, og context parameter når den bare skal skygges bak kulissene.

**Notater fra konferansen:**
- Godt foredrag om en nyttig ny feature i Kotlin (stabil i 2.4)

**Tags:** `Kotlin 2.4` · `Context parameters` · `API-design` · `DSL` · `Språkdesign`

**📹** [Context parameters and API design – Alejandro Serrano Mena](https://www.youtube.com/watch?v=O1nTwf0QPj4)
