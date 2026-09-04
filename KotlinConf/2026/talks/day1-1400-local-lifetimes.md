# Local Lifetimes for Kotlin

*Dag 1, 21. mai 2026 · kl 14:00 · Ross Tate · 📋 [i programmet](../program.md#d1-1400) · 🌐 [offisiell beskrivelse](https://kotlinconf.com/talks/1077477/)*

Ross Tate presenterte et forslag om «local lifetimes» i Kotlin — et typesystem-tillegg der et nytt `local`-nøkkelord på parametere (og `local class`-deklarasjoner) begrenser hvor lenge en referanse får leve, supplert av en subskript-notasjon som `Iterator<B>_{this&transform}` som binder returtypens levetid til inn-parameterne. Målet er å forhindre at ressurser og tilbakekall lekker ut av kallets leksikalske ramme, slik at man trygt kan bygge effektlignende mønstre som `Raise<E>`, non-local return i `fold`, samt lekkasjefrie byggere som `buildMap` og `lazy`.

Forslaget ligger tettere på scope-funksjoner (`let`, `apply`, `run` blir typesikre uten å endre bruksmønsteret) og gir grunnlag for «leksikalsk suspend» ved siden av dagens coroutines, mens det utfyller context parameters som en ortogonal mekanisme. Ross viste eksempler som `MappingIterator`-implementasjon, lokalisering av standardbiblioteket og et casestudium med pods4k-biblioteket der bare rundt tjue annoteringer trengtes – og forklarte at kompilatoren kan behandle levetider som en form for generisk parameter og utlede dem på samme måte som typeargumenter. Levetidene åpner også for ytelsesgevinster: objekter med lokal levetid kan stakkallokeres i stedet for å havne på heapen – mindre press på GC, billigere varargs og færre store inline-funksjoner i standardbiblioteket. En bærende del av argumentasjonen var dessuten at både exceptions og dagens coroutines bygger på dynamisk scoping, som beviselig ikke komponerer – illustrert med en sequence-builder der yield inne i launch fanges av feil handler og programmet henger evig – mens leksikalsk scopede primitiver, typet med local lifetimes, løser dette.

Han la vekt på at forslaget er bakoverkompatibelt: eksisterende kode fortsetter å virke, `Any` kan gjøres `local` uten å bryte arv, og biblioteker kan gradvis annotere signaturer uten å tvinge klienter til endringer. Typesjekkingen bygger videre på inferensalgoritmen fra fjorårets foredrag og forblir avgjørbar, men alt foreligger foreløpig bare på papir – spørsmålet er ikke om det kan implementeres, men om og hvordan det bør designes. Arbeidet er publisert som design notes i KEEP #485 og er fremdeles forskning under utvikling, delt tidlig for å samle tilbakemeldinger før et formelt KEEP-forslag. Min vurdering fra salen: en interessant og nyttig ny Kotlin-feature – verdt å følge videre.

**Tags:** `Språkdesign` · `Type system` · `Forslag` · `Escape analysis` · `Effects` · `Compiler`

**📹** [Local Lifetimes for Kotlin – Ross Tate](https://www.youtube.com/watch?v=6ALhoqxYrV0)

*[← 1300 Google Search-coroutines](day1-1300-google-search-coroutines.md) · [1515 Why Most AI Agents Never Scale? →](day1-1515-why-ai-agents-never-scale-koog.md)*
