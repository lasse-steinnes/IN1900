### Oppgave 5.3: Gjør det samme som i 5.2 med med vektoriserte funksjoner###

### I oppgave 5.2 brukte jeg math for å importere funksjoner
### Istedet kan jeg importere alle med bruk av numpy
### Da kan jeg beregne h(x) direkte siden funksjonen tar vektorisert x

from numpy import array, linspace, sqrt, exp, pi

### Først lager jeg matrise for x

x = linspace((-4),4,9, dtype=int) # PS: List comprehension gir liste,
                #   unngår dette med linspace, typespesifisering: bruk av heltall
# print(x) Test
## funksjon for h
def h(x):
    y_value = (1/sqrt(2*pi))*exp((-0.5)*x**2)
    return y_value

## Gjør skriver inn for y

y = h(x)

# Skriver ut ved å bruke to list
# comprehension som omgjøres til array

x_y_array = array([[i,n]for i,n in zip(x,y)])# når man gjør om til array blir alt float

# print(x_y_array) Test

print("""
#Tabell 2: Samme liste over x og y verdier
""")
print("---------------")
print(" x     y")
print("---------------")
[print("{: g} {:>11.3e}".format(j[0],j[1])) for j in x_y_array]
print("---------------")

"""SPM: 1) Går det an å gjøre om i til type int idet man gjør om til array?
2) Er det en måte å skrive ut uten å gå via en for løkke eller list comprehension?
3) Burde man kunne map funksjonen?"""
### Kjøreeksempel
"""
python fill_arrays_vectorized.py

#Tabell 2: Samme liste over x og y verdier

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
