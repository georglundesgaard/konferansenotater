# 10 Things I Hate About Java

*Dag 1, 2. september 2026 · kl 15:40 · Adele Carpenter · 📋 [i programmet](../program.md#d1-1540) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/58719c5f-f01f-46b1-bd00-ca8df0df8d7b)*

Carpenter fra Trifork Amsterdam holdt en kjærlig-kritisk gjennomgang av Javas mest frustrerende designvalg, med tittel og ramme lånt fra filmen «10 Things I Hate About You» – og med C# som gjennomgående sammenligningsgrunnlag, inspirert av en middag med C#-sjefdesigner Mads Torgersen. Hun startet med historien fra Sun og Green Team på 90-tallet, Javas fem opprinnelige designmål og arven fra Xerox PARC-språkene Smalltalk, Mesa og Cedar, som ga Java blant annet objektorientering, garbage collection og trådmodellen.

Hovedankepunktene var type erasure i generics (et kompromiss fra 2004 for å bevare bakoverkompatibilitet og unngå JVM-endringer, i kontrast til C# som oppdaterte runtimen og fikk reifiserte generics – noe som muliggjør elegante konstruksjoner som LINQ), checked exceptions (som kolliderer med lambdaer og streams og tvinger frem stygge workarounds), boilerplate-kulturen der biblioteker som Lombok avslører språkmangler, gotchas i virtual threads som thread pinning (rettet først i Java 24), og Project Valhalla – som etter tolv år fortsatt ikke har levert value types, noe C# har hatt siden starten.

Tonen var humoristisk, men konklusjonen forsonende: Java-teamet tok stort sett rimelige valg gitt informasjonen de hadde, bakoverkompatibilitet og konsensusdrevet utvikling har en pris, og Java driver fortsatt kritiske systemer verden over. Hun avsluttet med en egen versjon av filmens dikt: mest av alt hater hun at hun ikke hater Java i det hele tatt.

**Tags:** `Java` · `Språkdesign` · `Historikk` · `JVM` · `Underholdning`

**📹** [10 Things I Hate About Java – Adele Carpenter](https://vimeo.com/1223438630)

*[← JavaZone 2026](../README.md)*
