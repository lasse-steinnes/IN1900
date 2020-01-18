### Revidert oppgave 4.11
###  Skal skrive om oppgave 4.10 med hensyn til unntak(exception handling)

## Kommentar: Kunne brukt asparg eller if length() elif for
# å ha input for kun en verdi som mangler, men oppgaven ber
# om ikke om det, så gjør ikke det denne gangen.

## Kommentar: Denne oppgaven kunne også blitt løst med en if-else statement


import sys

try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
    print("Du har ikke oppgitt noen verdi for v0 eller t")
    v0 = float(input("v0="))
    t = float(input("t="))
except ValueError:
    print("Verdien du har oppgitt for v0 eller t0 er ikke på riktig form")
    v0 = float(input("v0="))
    t = float(input("t="))

g = 9.81

y = (v0*t) - 0.5*g*(t**2)

print("""Ballens posisjon over bakken er %.2f m evaluert
når v0=%.2f og t=%.2f."""%(y,v0, t))

### Kjøreeksempel
"""
>> python ball_cml_qa2.py 5
Du har ikke oppgitt noen verdi for v0 eller t

v0=5
t=0.6

Ballens posisjon over bakken er 1.23 m evaluert
når v0=5.00 og t=0.60.
"""
