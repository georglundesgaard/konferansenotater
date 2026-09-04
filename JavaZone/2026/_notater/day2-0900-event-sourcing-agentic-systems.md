# Notater: Event Sourcing: The Only Sane Way to Run Agentic Systems

Rånotater fra salen, flyttet ut av [talk-siden](../talks/day2-0900-event-sourcing-agentic-systems.md) 4. september 2026. Punktene er verifisert mot opptaket og flettet inn i sammendraget; korreksjoner står som kursiverte merknader under det aktuelle punktet.

- Fra skaperen av [cratis.io](https://cratis.io)
- Intro om event sourcing for å fange alt som skjer i et system
- Events er domain events (fra DDD)
- Eventene lagres i en event store – den holder sannheten
- Observers, read models, outbox, inbox og «source box»
  *(Korreksjon fra opptaket: «source box» brukes ikke – mishøring av «an inbox per source outbox» (13:35). Navnet cratis.io sies heller ikke eksplisitt, men innholdet stemmer med Cratis.)*
- Interessant foredrag om event sourcing og hvorfor det er viktig for å holde styr på hva agentene gjør og hvorfor i agentiske systemer
