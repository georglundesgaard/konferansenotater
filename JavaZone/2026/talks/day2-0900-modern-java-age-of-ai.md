# Modern Java in the age of AI

*Dag 2, 3. september 2026 · kl 09:00 · Georges Saab · 📋 [i programmet](../program.md#d2-0900) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/81600832-deed-4cc5-8bcf-97880d961046)*

Saab, SVP for Java i Oracle og styreleder i OpenJDK, ga en statusrapport for Java i 2026: seksmåneders-releasemodellen leverer 8–20 nye features og 2000–2800 fikser per versjon, JDK 27 kommer uken etter foredraget, og utviklingen skjer helt åpent i OpenJDK-fellesskapet der Oracle er største, men langt fra eneste, bidragsyter. Features utvikles nå iterativt i mindre biter – pattern matching og lambdas ble brukt som eksempler på at tålmodig forenkling gir løsninger som føles naturlige i språket.

På AI-fronten skilte han mellom å bruke AI fra eksisterende Java-applikasjoner og å kjøre AI-arbeidslaster på selve JVM-en, der prosjekter som Valhalla (value types kommer i mainline for JDK 28), Leiden (raskere oppstart uten kodeendringer), Babylon (GPU-distribusjon av Java-kode) og Detroit (interop med Python og JavaScript) adresserer minnebruk, ytelse og økosystem-integrasjon. Han trakk også frem ressurser som dev.java, Inside Java og den ferske Java-dokumentaren fra Cult Repo.

Hoveddelen var en visjon om «tip and tail»-releasemodellen (JEP 14): nye features legges kun i tip-versjonen, mens tail-versjoner bare får sikkerhetspatcher og kritiske fikser – i motsetning til «one size fits all»-modellen som verken tjener de som vil ha stabilitet eller de som vil ha ny funksjonalitet. JDK selv følger modellen (tails hvert annet år: 17, 21, 25, neste blir 29), Helidon ble vist som rammeverk som gjør det samme, og Saab oppfordret biblioteksutviklere til å adoptere modellen slik at hele Java-økosystemet kan bevege seg fremover sammen.

**Tags:** `Java` · `AI` · `JVM` · `Keynote` · `Språkdesign`

**📹** [Modern Java in the age of AI – Georges Saab](https://vimeo.com/1223621051)

*[← JavaZone 2026](../README.md)*
