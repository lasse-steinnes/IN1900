### Oppgave 5.5 Oscillerende fjær; fysikkheftet
### En stein henger fra ei fjær, steinen dras ned.
#Skal finne posisjonen ved tid t

from numpy import zeros
from math import sqrt, exp, cos

#  Skal lage to tomme arrays t_array og y_array av lengde 101.

n=101                       # lengde

t_array = zeros(n)#, int)
y_array = zeros(n)


#Skal bruke en for løkke til å fylle dem med tidsverdier i intervallet
# [0 s, 25 s],

dt = (25)/(n-1)#*100 # Lager en delta t med n-1 steg

#Konstanter i y
#A = 0.3     # Utrekningslengde på fjæra[m]
#γ = 0.15    # En konstant, gamma[s**(-1)]
#k = 4       #en konstant[kg/s**2]
#m = 9       #steinens masse[kg]

def position(t, A = 0.3, gamma_ = 0.15, k = 4, m = 9):  # Gjør så man kan endre når man kaller på den
    y_t = A*exp(-gamma_*t)*cos(sqrt(k/m)*t)
    return y_t

for t in range(n):
    t_array[t] = dt*t
    # y_array[t] = A*exp(-γ*t)*cos(sqrt(k/m)*t)
    y_array[t] = position(t_array[t]) # Glemte å skrive t_array, skrev t

t_array = t_array#/100
y_array = y_array#/100

print("a) Utskrift: t etterfulgt av y")
print(t_array)
print(y_array)

# PS: husk at for t in t_array, da ville t vært en verdi fra t_arrayet
#print(t_array) Test

## b) Skal gjøre det samme, men i vektorisert form.
# Dette gjør programmet raskere og mer fleksibelt

#import numpy as np # Prøvd dette også, men neida...
from numpy import linspace, exp, cos, sqrt

# Lager array
t_array2 = linspace(0,25,n)# dtype=int) #100

# definerer funksjon
def position2(t, A = 0.3, gamma_ = 0.15, k = 4, m = 9):  # Gjør så man kan endre når man kaller på den
    y_t = A*exp(-gamma_*t)*cos(sqrt(k/m)*t)
    return y_t

y_array2 = position2(t_array2)

t_array2 = t_array2#/100
y_array2 = y_array2#/100

print("b) t etterfulgt av y")
print(t_array2) #test
print(y_array2) # test

# c)
# Skal plotte de mot hverandre

import matplotlib.pyplot as plt # plt for visualiseringspakke, standard navn
plt.plot(t_array,y_array,t_array2,y_array2)
plt.title("Posisjon til kulen fra utgangsposisjonen")
plt.xlabel("Tid[s]")
plt.ylabel("Posisjon[m]")
plt.text(13,0.3,"Grafene er like!!! :D")
plt.show()

### Kjøreeksempel
"""
>> python oscilating_spring.py
Utskrift: t etterfulgt av y
a) Utskrift: t etterfulgt av y
[  0.     0.25   0.5    0.75   1.     1.25   1.5    1.75   2.     2.25
  ..............
  23.75  24.    24.25  24.5   24.75  25.  ]
[  3.00000000e-01   2.84954297e-01   2.63003296e-01   2.35261635e-01
   2.02925830e-01   1.67234799e-01   1.29432046e-01   9.07304561e-02

  ...........
  -7.85004655e-03  -7.07924703e-03  -6.16558284e-03  -5.14500350e-03
  -4.05385970e-03]

b) t etterfulgt av y
[  0.     0.25   0.5    0.75   1.     1.25   1.5    1.75   2.     2.25
  .....
  21.25  21.5   21.75  22.    22.25  22.5   22.75  23.    23.25  23.5
  23.75  24.    24.25  24.5   24.75  25.  ]
[  3.00000000e-01   2.84954297e-01   2.63003296e-01   2.35261635e-01
   2.02925830e-01   1.67234799e-01   1.29432046e-01   9.07304561e-02
  ......
  -7.85004655e-03  -7.07924703e-03  -6.16558284e-03  -5.14500350e-03
  -4.05385970e-03]

(plot)
"""
"""
Kommentar: Jeg ser at verdiene for y blir feil på en av dem,
men funksjonen ser da helt lik ut. Har prøvd å leke med heltall
istedet for flyttall, men uten hell. Eneste jeg kommer på er å omskrive
eller at numpy funksjonene kjører annerledes enn math. IDK! Det er lørdag
I give up. :P

Edit: Jeg tok en pause, og kom tilbake med enn ganske simpel løsning :3

"Most coders think debugging software is about fixing a mistake,
but that’s bull****. Debugging’s actually all about finding the
bug, about understanding why the bug was there to begin with,
about knowing that its existence was no accident. It came to
you to deliver a message, like an unconscious bubble floating
to the surface, popping with a revelation you’ve secretly
known all along" (Mr Robot, S1.Ep3: eps1.2_d3bug.mkv)
"""
