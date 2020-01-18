### 4.10: Les parametere i en formel fra commnadolinjen"""

## Skal gjøre om ligningen fra oppgave 4.9 til å ta
## verdier fra terminalen

import sys

v0 = float(sys.argv[1])    # fart [m]
g = 9.81                  # gravitasjonskonstanten[]
t = float(sys.argv[2])     # tid [sek]
y = (v0*t) - 0.5*g*(t**2)

print("""Ballens posisjon over bakken er %.2f m evaluert
når v0=%.2f og t=%.2f."""%(y,v0, t))

##### Kjøreeksempel
"""
>> python ball_cml.py 5 0.6
Ballens posisjon over bakken er 1.23 m evaluert
når v0=5.00 og t=0.60.
"""
