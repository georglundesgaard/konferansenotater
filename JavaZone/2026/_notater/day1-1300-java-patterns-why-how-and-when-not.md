# Notater: Java Patterns: Why, How, and When Not

Rånotater fra salen, flyttet ut av [talk-siden](../talks/day1-1300-java-patterns-why-how-and-when-not.md) 4. september 2026. Punktene er verifisert mot opptaket og flettet inn i sammendraget; korreksjoner står som kursiverte merknader under det aktuelle punktet.

- Hovedtema: OOP vs DOP
- Bok: «Data-Oriented Programming in Java», Chris Kiehl
  *(I foredraget omtalt bare som «Data-Oriented Programming»; full tittel er likevel riktig.)*
- «Algebraic» data: sum og product
- «Exhaustive» switch
- «Enhanced» switch
- JEP 540
- JEP 532 – mulige pitfalls: `double x` => `int x`
  *(Verifisert: fella er at et `int`-mønster mot en `double`-komponent stille bare matcher verdier som passer i int – rådet er å alltid bruke `var`. Transkripsjonen sier «Java SE 532», trolig feiltranskribering av JEP 532.)*
- Data classes: immutable, no hidden state
- Records: «comb» hierarchy
- Helt grei talk – kanskje litt smalere tema enn hva jeg antok i forkant
