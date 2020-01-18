### Oppgave A.5 Løs et system av differensligninger.###

## Om man har en formue i banken, og ønsker å ta ut
## en mengde c_n hvert år skal tas ut. Siden det er inflasjon, må
## denne verdien justeres.

#Vi får da ligningssett som kan løses for en gitt
## initialverdi(formue), renteverdi og inflasjon.

import numpy as np

i_end = 101
n = np.arange(0,101,1)    # Anta at personen lever i 100 år,
                              #  og arver hele formuen i en alder av 0 (lucky bastard)
r = 0.05                      # rente
q = 1500                      # prosentuttak av formueveksten det første året.
I = 0.02                      # Inflasjon

x = np.zeros(i_end)
x[0] = 15                  # millioner formue.

c = np.zeros(i_end)

c[0] = x[0]*r*q/1e4           # Første uttak

def formue(x,c):
    "Beregner xn og cn for en situasjon med x formue og c uttak"
    "Nødvendig med x0 og c0 for at denne skal fungere"
    for i in range(1,i_end):
        x[i] = x[i-1] + r/100*x[i-1] - c[i-1]
        c[i] = c[i-1] + I/100*c[i-1]
    return x, c

formue_ = formue(x,c)
## Plotter X_n sekvensen, (og c_n siden jeg har lyst)
import matplotlib.pyplot as plt
from matplotlib import gridspec

# Initierer figur
plt.figure(figsize=(7,5)) # bredde,høyde

# Lager subplot
gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])
#rad,kolonner, bredderatio på subplot

# for x_n
plt.subplot(gs[0])  # bruker gridspec spesifisering på subplot
plt.plot(n,formue_[0],'b-')
plt.title('Formue som en funksjon av år')
plt.xlabel('År')
plt.ylabel('Formue[millioner]')

# for c_n
plt.subplot(gs[1])
plt.plot(n, formue_[1],'g-')
plt.title('Uttak som en funksjon av år')
plt.xlabel('År')
plt.ylabel('Uttak[millioner]')

plt.subplots_adjust(left=0.10, right=0.9,\
                wspace=1.0)

plt.tight_layout() # Overkjører default for fig instillingene.

plt.show()

## Kjøreeksempel
"""
>>  python fortune_and_inflation1.py
(plot)
"""
