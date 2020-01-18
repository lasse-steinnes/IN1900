##### Oppgave 5.2. Fyll tomme matriser(arrays) med en for løkke

## Tolker oppgaven som at en tom matrise,
## er en matrise bestående av nuller

## Eventuelt kunne jeg laget en tom liste
## og gjort om denne til matrise

## Først lager jeg tomme matriser

from numpy import zeros # numpy for matriseoperasjoner
from math import sqrt, exp, pi

n = 9 ## lengde på array

x = zeros(9, int) # zeros med type spesifisering
#print(x) Test
y = zeros(9, float)
# print(y) Test
## Deretter definerer jeg h(x)

def h(x):
    y_value = (1/sqrt(2*pi))*exp((-0.5)*x**2)
    return y_value


## Så fyller jeg inn i de tomme matrisene i en for løkke
## Kommentar: Slik skalarkode er treig fordi man må gå gjennom hvert element og disse er lagret i en list
x0 = int(-4)
print("""
Tabell 1: Liste over x og y verdier
""")
print("---------------")
print(" x     y")
print("---------------")

for i in range(n):     ## kunne brukt x._len_() men får den ikke til å fungere
    x[i] =+ x0
    x0 += 1
    y[i] = h(x[i])
    print("{: d} {:>11.3e}".format(x[i],y[i]))

print("---------------")

## Bruker nye formatet til å fjerne problemet
## med negative og positive tall som ikke er på linje

## Kjøreeksempel
"""
>> python fill_arrays_loop.py

Tabell 1: Liste over x og y verdier

---------------
 x     y
---------------
-4   1.338e-04
-3   4.432e-03
-2   5.399e-02
-1   2.420e-01
 0   3.989e-01
 1   2.420e-01
 2   5.399e-02
 3   4.432e-03
 4   1.338e-04
---------------
"""
