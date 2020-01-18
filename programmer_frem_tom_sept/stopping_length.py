#### 4:16 Beregne avstanden det tar å stoppe en bil ###

## Skal beregne bremselengden d, som kan
# utledes fra Newtons andre lov.
# Algoritme: Importere nødvendig pakke, skrive program med sys.argv

import sys

try:
    v0 = float(sys.argv[1])*(1.0/3.6)   #fart[m/s]
    my_ = float(sys.argv[2])           # my[-], skal være 0,3

except IndexError:
    print("Verdi for v0 eller my_ er ikke oppgitt")
    print("Oppgi: v0 my_, type:float")
    v0=float(input("v0="))*(1.0/3.6)
    my_=float(input("my_="))
except ValueError:
    print("Verdien for v0 eller my_ er ugyldig")
    print("Oppgi: v0 my_, type:float")
    v0=float(input("v0="))*(1.0/3.6)
    my_=float(input("my_="))

g = 9.81                          # gravitasjonskonstanten
d_ = (1/2)*(v0**2)/(my_*g)

print("Bremselengden er %.2f meter når farten er %.2f m/s og my er lik %.2f." %
    (d_, v0,my_))

### Kjøreeksempel
"""
>> python stopping_length.py
Verdi for v0 eller my_ er ikke oppgitt
Oppgi: v0 my_, type:float

v0=120
my_=0.3
Bremselengden er 188.77 meter når farten er 33.33 m/s og my er lik 0.30.
"""

"""
>> python stopping_length.py 50 0.3
Bremselengden er 32.77 meter når farten er 13.89 m/s og my er lik 0.30.
"""

## Hvorfor fungerer det ikke med def....?
