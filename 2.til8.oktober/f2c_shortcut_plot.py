### Oppgave 5.12

### Skal plotte eksakt og tilnærming til celsius i et og samme plotte

def c_eksakt(f):
    c = (float(5)/9)*(f - 32)
    return c

def c_tilnarmet(f):
    c = (f - 30)/2
    return c

## Skal jobbe med array, det er enklest
## Lager en ny med linspace.

from numpy import linspace

F_deg = linspace(-20,120,140)

c_eksakt = c_eksakt(F_deg)
c_tilnarmet = c_tilnarmet(F_deg)

# Deretter kan man plotte disse mot hverandre

import matplotlib.pyplot as plt  # Regnes som bra praksis

plt.plot(F_deg, c_eksakt, label = 'Eksakt')
plt.plot(F_deg, c_tilnarmet, label = 'Tilnærmet')
plt.xlabel("Grader[F]")
plt.ylabel("Grader[C]")
plt.legend()
plt.show()

## Kjøreeksempel
"""
>> python f2c_shortcut_plot.py
(plot)
"""
