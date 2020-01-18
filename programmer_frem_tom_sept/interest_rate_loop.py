### Oppgave 2.13
initial_amount = 100
p = 5.5 # initial rate
amount = initial_amount
years = 0

while amount <= 1.5*initial_amount:
    amount += p/100*amount
    years += 1
    print (years, amount)

### a) regne ut for hånd. meh
## b) for p=5 ville pyt2 brukt integer divisjon
## c) +=
## d) Det matematiske problemet i denne oppgaven
## er å lage en liste over hvor mange år som
## det tar for initial amount å fordoble seg.
## Den siste verdien er det året mengden er >= amount
