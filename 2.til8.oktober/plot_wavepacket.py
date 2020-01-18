###

## Definerer funksjonen
from numpy import exp, sin, pi, linspace

bølge = lambda x,t=0: exp(-(x-3*t)**2)*sin(3*pi*(x-t))

## Lager intervallet for x
x_matrise = linspace(-4,4,1500)

# Slik at
bølge_t0 = bølge(x_matrise)

### Plotter funksjonen
import matplotlib.pyplot as plt
plt.plot(x_matrise, bølge_t0, label = 'bølgepakke for t=0')
plt.legend()
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.show()

## Kjøreeksempel
"""
>> python plot_wavepacket.py
(plot)
"""
