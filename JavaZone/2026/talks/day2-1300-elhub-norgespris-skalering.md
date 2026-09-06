# Fra 123 entusiastiske brukere daglig, til 3.7 millioner, Norgespris som arkitektur katalysator i Elhub

*Dag 2, 3. september 2026 · kl 13:00 · Trond Strømme, Michael Akinde · 📋 [i programmet](../program.md#d2-1300) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/3d14ed40-7c5c-48d3-8fb7-0a99693801df)*

Trond Strømme og Michael Akinde fra Elhub (Statnetts datterselskap som forvalter 3,7 millioner målepunkter og hundrevis av milliarder måleverdier) fortalte hvordan lanseringen av Norgespris i 2025 ble en katalysator for modernisering. Min side-løsningen fra 2019 var tett koblet til kjernesystemet («spaghettimonolitt»), tålte knapt hundre samtidige brukere og hadde rundt 123 brukere på en god dag – men over natten kunne de få millioner. I stedet for å flikke på det gamle valgte de å bygge nytt, og fordi moderniseringsprogrammet Evergreen allerede hadde eksperimentert frem byggeklosser som Kubernetes, Postgres, Kafka og en observabilitetsplattform med Grafana/Prometheus/Loki, sto de klare da oppdraget kom – med i praksis bare noen måneder fra endelig vedtak til frist 1. oktober.

Den nye løsningen fikk moderne autentisering og autorisasjon (OpenID Connect i stedet for SAML, Open Policy Agent, backend-for-frontend slik at tokens aldri lekker til nettleseren), API-først-design der Min side bare er én klient, WAF, nettverkssegmentering og isolerte Kubernetes-clustre per workload. De prekalkulerte besparelsestall for hele Norge for å slippe tunge oppslag i sanntid, og modellerte ytelse ut fra reell brukeradferd i stedet for urealistiske mål – lanseringsdagen 24. september toppet trafikken på 19,5 innlogginger i sekundet, CPU-lasten lå rundt 20 prosent, og 380 000 brukere var innom uten nedetid; trafikken kom i tydelige topper etter TV-nyhetssendingene, og i dag har 1,8 millioner inngått Norgespris-kontrakt.

Fra postmortemen trakk de frem at autonome verdistrømteam ga fart og eierskap, men også koordineringsutfordringer og «introverte team» som glemte å varsle plattformsiden; nøkkelpersonavhengighet forsterkes kraftig under tidspress, testmiljøer med konsistente data er vanskelig i et komplekst legacy-domene, og personvernanalysen kom sent fordi regelverket først ble vedtatt i statsråd 15. september. Hovedbudskapet: senioren og arkitektens viktigste jobb er å tenke fire år frem, slik at byggeklossene ligger klare når det uventede kommer.

**Tags:** `Casestudie` · `Skala` · `Arkitektur` · `Performance`

**📹** [Fra 123 entusiastiske brukere daglig, til 3.7 millioner, Norgespris som arkitektur katalysator i Elhub – Trond Strømme, Michael Akinde](https://vimeo.com/1223685030)

*[← JavaZone 2026](../README.md)*
