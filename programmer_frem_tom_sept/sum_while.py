### Oppgave 2.11: Trening i å rette opp en kode

s = 0; k = 1; M = 100

while k <= M:       # Feil 1: Begrensning
    s += float(1)/k # Feil 2: (Ikke problem i py_3)
    k += 1          # Feil 3: Må ha en teller for k

print ("Summen av a_n:1/k er lik %.3f for 0<k<=100" %(s))

## to måter å finne feil på:
#       1. Se gjennom algoritme (logikk)
#       2. Regne gjennom for hånd.
#               Prøver for M=3. Får det samme

## Kommentar: Har fjerde feil noe å gjøre med desimalfeil?
## (dvs. tredje feil i py3)

# Kjøreeksempel
""" python sum_while.py
>> Summen av a_n:1/k er lik 5.187 for 0<k<=100 """
