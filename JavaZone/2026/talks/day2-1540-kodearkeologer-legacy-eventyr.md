# Kodearkeologer på legacy eventyr

*Dag 2, 3. september 2026 · kl 15:40 · Elisabeth Irgens, Robin Kåveland · 📋 [i programmet](../program.md#d2-1540) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/7a7da44d-1198-4751-b0a0-e712dec09e14)*

Elisabeth Irgens og Robin Kåveland fortalte historien om hvordan de som et topersonsteam i Amedia reddet Rubrikk-applikasjonene – tolv applikasjoner bygd på restene av markedsplassen Zett fra 2002, med noen hundre tusen linjer kode i Java, Ruby, Node, CoffeeScript og PHP, og 1386 åpne critical/high-sårbarheter. Koden var glemt, men leverte fortsatt målbare inntekter gjennom stillings- og eiendomsannonser, og mange mennesker i organisasjonen – selgere, brukerstøtte og annonseprodusenter – var avhengige av systemene.

Strategien var å plukke lavthengende frukter først for å skape fart og trygghet: oppgradere serialiseringsbibliotek og Docker-images, bruke Trivy for korte feedback-looper på CVE-er, rigge lokalt utviklingsmiljø med Mise og Docker Compose, og slette ubrukt kode med IntelliJs statiske analyse. Videre skrudde de av hele applikasjoner der det gikk – et skreddersydd statistikkdashboard ble erstattet med 100 linjer SQL og Looker, og med OpenTelemetry-traces som beviste internbruk kunne to integrasjonsapper smeltes inn i «elefanten i rommet», noe som til slutt lot dem slette over 40 000 linjer kode. Tyngre oppgraderinger fra Spring Boot 1/Java 8 til moderne versjoner ble automatisert med OpenRewrite, og et hjemsøkt Rails-adminsystem fra 2012 ble erstattet med et bevisst enkelt, server-rendret HTML-grensesnitt i Java, utviklet i tette iterasjoner med ekspertbrukerne. Underveis fant de også persondata fra 2003 og lærte riktig prosess med personvernombudet.

Etter åtte måneder var de opprinnelige sårbarhetene håndtert og tolv applikasjoner redusert til syv. Lærdommene: finn momentum med små, hyppige prodsettinger, slett mye kode og sluntre unna arbeid som ikke trengs, bygg tillit hos brukerstøtte og brukerne som trenger systemene, og jobb tett i par – to personer som samarbeider mye trenger nesten ingen prosess.

**Tags:** `Modernisering` · `Legacy` · `Casestudie` · `Tooling`

**📹** [Kodearkeologer på legacy eventyr – Elisabeth Irgens, Robin Kåveland](https://vimeo.com/1223725300)

*[← JavaZone 2026](../README.md)*
