# How I built my own intelligent Robot Arm from Scratch

*Dag 2, 3. september 2026 · kl 17:00 · Iulia Feroli · 📋 [i programmet](../program.md#d2-1700) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/f0aeaff3-7ff5-4af4-b19e-f7efabd2546e)*

Feroli fortalte hvordan hun sa opp jobben som developer advocate innen data science og AI for å satse på «physical AI» – robotikk kombinert med moderne AI-modeller – og bygge et fellesskap rundt det. Prosjektet hennes var en robotarm bygget helt fra bunnen: første prototype var laget av papp og teip til 3 dollar, deretter plastdeler, og til slutt en 3D-printet arm med servomotorer til 1 dollar stykket og en mikrokontroller – først en Arduino programmert i C++, senere en Raspberry Pi Pico med MicroPython. Totalpris rundt 20 dollar, mot 100 dollar for det billigste ferdigkjøpte settet.

Neste steg var Hugging Faces åpne kildekode-robot Le Robot (ca. 150 dollar per arm), som hun demonstrerte live med teleoperasjon: en leder-arm styrer en følger-arm fordi servoene kan rapportere sin egen posisjon, og bevegelser kan tas opp og spilles av som funksjoner. Slike opptak blir treningsdata for modeller som etter hvert kan utføre oppgaver selvstendig – hun advarte samtidig om at mange imponerende robotdemoer i virkeligheten bare er teleoperasjon eller forhåndsprogrammerte bevegelser. Hun brukte også Claude til å generere servo-funksjoner («få den til å vinke») i stedet for å programmere hver vinkel manuelt, og pekte på at AI nå kan erstatte mye av den klassiske inverskinematikk-matematikken.

Lærdommene var like mye fysiske som digitale: feilsøking betyr å skille kodefeil fra løse kabler, kalibrering av servoer tar tid, lodding trengs når pinner løsner, og hun har brent både servoer, en NVIDIA-brikke og – midt under forberedelsene til foredraget – sikringen i foredragssalen. Veien videre går via ROS, datasyn, simulering og dyrere edge-maskinvare, med klesbretting som det store målet. Hovedbudskapet: med programvarebakgrunn kan man komme i gang med fysisk AI hjemme på en dag og få tilbake litt av lekelysten.

**Tags:** `AI` · `Robotikk` · `Live demo`

**📹** [How I built my own intelligent Robot Arm from Scratch – Iulia Feroli](https://vimeo.com/1223742105)

*[← JavaZone 2026](../README.md)*
