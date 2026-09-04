# 50 tips på 60 min – bli bedre med AI-agenter

*Dag 1, 2. september 2026 · kl 09:00 · Kjetil Jørgensen-Dahl · 📋 [i programmet](../program.md#d1-0900) · 🌐 [offisiell beskrivelse](https://2026.javazone.no/program/bf1d8198-ae19-4558-a259-3e6910565a3f)*

Jørgensen-Dahl leverer 50 tips om AI-kodeagenter (Claude Code, GitHub Copilot CLI, OpenCode) bygget på en tipsserie han har delt internt på Slack siden nyttår. Han starter med et fundament om hvordan språkmodellene faktisk virker: de er tilstandsløse, ikke-deterministiske token-maskiner med frossen kunnskap, der hele samtalen sendes inn på nytt hver tur – derav prefix-caching, og derav at oppmerksomheten forvitrer når kontekstvinduet fylles. Praktiske konsekvenser blir konkrete tips: velg modell og reasoning effort etter oppgaven, hold én oppgave per sesjon, start en ny sesjon i stedet for å krangle når agenten drifter, og formuler spørsmål nøytralt eller be om kritikk for å omgå modellenes smisketendens.

Neste bolk handler om å rigge agenten for suksess: en kort, håndkuratert instruksjonsfil (agents.md/CLAUDE.md) som prosjektets stående onboarding, skript for alt som skal være deterministisk, hooks som håndhever regler agenten ellers glemmer (f.eks. lint etter filendring), og forhåndsgodkjente kommandolister. Han advarer om prompt injection – illustrert med Klein-hendelsen og Hugging Face-hackingen der over 1000 agenter samarbeidet om å jukse – og anbefaler minimumsprivilegier og sandboxing. For å holde konteksten slank: subagenter som gjør grovarbeidet i egen kontekst (inkludert advisor-mønsteret med billig hovedmodell og dyr rådgiver), skills med progressive disclosure, og spek-dokumenter som overlever på tvers av sesjoner.

Arbeidsflyt-tipsene omfatter billige engangs-spikes man kaster før man bygger ordentlig, code review fra flere perspektiver med parallelle subagenter, Git Worktree ved flere samtidige agenter, og «loop engineering» der tester og kjørbare sjekker lar agenten lukke sløyfen selv. Han avslutter reflekterende: vibe-koding bygger forståelsesgjeld (med henvisning til et Anthropic-eksperiment der AI-brukere forsto koden sin signifikant dårligere), refaktoriseringstrykket må holdes oppe, harness-oppsettet bør eies av teamene selv, og det å skrive ned egne erfaringer lærer deg mer enn å lese andres tips.

**Tags:** `AI` · `AI-agenter` · `Produktivitet` · `Tooling` · `LLM`

**📹** [50 tips på 60 min – bli bedre med AI-agenter – Kjetil Jørgensen-Dahl](https://vimeo.com/1223281331)

*[← JavaZone 2026](../README.md)*
