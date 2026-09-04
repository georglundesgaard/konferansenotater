# Flyt i AI-ens tid: når det blir lettere å lage, men vanskeligere å bevege seg

*Dag 2, 3. september 2026 · kl 10:20 · Christian Neverdal · 📋 [i programmet](../program.md#d2-1020) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/1d782b1f-62e4-4c7e-ba37-f2186f812262)*

Neverdal utforsker hva flyt betyr når AI gjør det trivielt å produsere kode – han styrer selv en AI-agent («Kerrigan») via Discord som lager slides underveis i foredraget. Hovedargumentet er hentet fra lean-tenkning: flaskehalsen er ikke lenger å lage ting, men all ventingen mellom stegene – på review, tilganger, avklaringer og beslutninger. Ti ganger mer output gir ti ganger mer kø, folk som er 100 % belastet skaper kø overalt, og vi bør heller sikte mot rundt 80 % utnyttelse med bevisst slack-tid. Aktivitet er ikke effekt: antall pull requests hadde før et naturlig tak, men med agenter i loop døgnet rundt blir produksjon i seg selv en plage. Å game metrikker mener han er helt greit – svaret er å foreslå mer humane målinger i stedet, som hvor smertefullt det er å deploye, hvor lang tid en beslutning tar, og tid fra mål (OKR) til effekt i stedet for tid fra PR til prod.

Han illustrerer poengene med en rekke vibe-kodede hobbyapper: fjernkontroll.tv (last opp bilde av fjernkontrollen og finn source-knappen), derdetblinker.com (flipperspilltips fra bilde) og især fire konkurrerende oversettelsesapper født av et reelt problem – en bilsamtale i Brasil med tre språk i spill. Erfaringene viser AI-ens svakheter: manglende sunn fornuft, evig medgjørlighet uansett forslag, tautologiske tester (som han foreslår å countere med mutasjonstesting), og en tendens til å legge på og spre kompleksitet. Han anbefaler skjønn fremfor rigide release-gates, og å gi agenter handlingsrom – «make it so» er et mandat, ikke bare en ordre – men med manuell overstyring når det trengs.

Konklusjonen er helintegrering og null overlevering: friksjonspunkter som å laste ned zip-filer eller lime inn manuelt dreper flyten, og målet er noe like smidig som PHP-over-FTP i gamle dager – lagre, og det er live. Han drømmer om trunk-basert utvikling uten issues, PR-er og CI-venting, der agenter med observability ruller tilbake feil raskere enn mennesker. Til slutt løfter han blikket: individuell flyt er bare starten – hjelp teamet, verdistrømmen og hele organisasjonen med flyt, for det er der AI-gevinsten egentlig ligger.

**Tags:** `AI` · `Karriere` · `Produktivitet` · `AI-agenter` · `Tooling` · `Testing`

**📹** [Flyt i AI-ens tid – Christian Neverdal](https://vimeo.com/1223643966)

*[← JavaZone 2026](../README.md)*
