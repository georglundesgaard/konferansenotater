# SwiftPM support for Kotlin Multiplatform

*Dag 1, 21. mai 2026 · kl 13:30 · Timofey Solonin*

Timofey Solonin viste i denne lyntalen hvordan Kotlin Multiplatform nå kan konsumere SwiftPM-avhengigheter direkte fra Gradle via en ny `swiftPMDependencies {}`-blokk, demonstrert med populære pakker som FirebaseFirestore, Sentry og Google Maps SDK. Xcode-integrasjonen fungerer ved at Gradle-tasken `integrateLinkagePackage` genererer en syntetisk SwiftPM-pakke som legges inn i `.xcodeproj` og deretter oppdateres automatisk når avhengigheter endres, med en `Package.resolved`-låsfil sjekket inn i repoet.

Under panseret oppdager Kotlin Gradle-pluginen Clang-modulene i Swift-pakkene og eksponerer dem for Kotlin/Native under navnerommet `swiftPMImport.<group>.<project>.<Module>`, slik at Objective-C- og Swift-API-er (via genererte Obj-C-headere) kan importeres direkte i `iosMain`. Transitiv maskinkode kobles inn automatisk ved testing og framework-linking, mens publisering av KMP-biblioteker som selv bruker SwiftPM-importer foreløpig ikke er støttet (sporet i KT-84420) – funksjonen er i alfa, og statiske rammeverk anbefales for å unngå duplikatsymboler.

**Tags:** `Lyntale` · `KMP` · `iOS` · `SwiftPM` · `Kotlin/Native` · `Tooling`

**📹** [SwiftPM support for Kotlin Multiplatform – Timofey Solonin](https://www.youtube.com/watch?v=GrO-bTnn_Ng)
