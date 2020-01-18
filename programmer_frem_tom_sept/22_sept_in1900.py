###### Forelesning

# Oppgave 4.7
"""
import sys

print(sys.argv[1], type(sys.argv[1]))
x = eval(sys.argv[1])
# x = "this is a string"

print(x,type(x))
# tolker som python uttrykk om må fikse det.
"""
"""
# oppgave 5.7
from numpy import *

w = linspace(0,3.0,31)

print(w[:])   # skriver ut alt

print(w[:-2]) # henter frem til nest siste)

print(x[::5]) # hente ut med step 5 (hvert femte)
"""
####################### Plotting
# Oppgave 5.9:
"""Trekkes rette linjer mellom punktene"""
"""
from numpy import *
from matplotlib.pyplot import *

v0 = 10
g = 9.81

t = linspace(0,2*v0/g,100)
y = v0*t-0.5*g*t**2     # t er array, derfor blir y array


plot(t,y)
title("Height of the ball")
xlabel("Time(s)")
ylabel("Height(m)")
#xaxis(0,)
show()
"""
### Oppgave 5.10. Plot en formel for flere variable
"""
from numpy import *
from matplotlib.pyplot import *   ## gui bibliotek kommunikasjon
import sys
# v0 = 10
g = 9.81

v_list = sys.argv[1:]

for v0 in v_list:
    v0 = float(v0)
    t = linspace(0,2*v0/g,100)
    y = v0*t-0.5*g*t**2     # t er array, derfor blir y array
    plot(t,y, label= "v0 = %g"%(v0))

title("Height of the ball")
xlabel("Time(s)")
ylabel("Height(m)")
legend()
show()
"""
# Kjøreeksempel
"""
Terminal > python filnavn
(output is a plot)
"""

# 5.11 Spesifiser størrelse på aksene.
# Poeng; må regne ut største og minste y verdi

"""
from numpy import *
from matplotlib.pyplot import *   ## gui bibliotek kommunikasjon
import sys
# v0 = 10
g = 9.81

v_list = sys.argv[1:]

t_max = 0       # sett variabler
y_max = 0

for v0 in v_list:
    v0 = float(v0)
    t_stop = 2*v0/g
    t = linspace(0,t_stop,100)
    y = v0*t-0.5*g*t**2     # t er array, derfor blir y array
    plot(t,y, label= "v0 = "%(v0)) # skal være %   g der
    if t_stop > t_max:
        t_max = t_stop
    if max(y) > y_max:
        y_maks = max(y)

title("Height of the ball")
xlabel("Time(s)")
ylabel("Height(m)")
legend()
axis([0,t_max,0,y_max])
show()
"""
## Heaviside med if
def H(x):
    if x < 0:
        return 0
    else:
        return 1
## Når numpy skal brukes må man benytte for el while løkke
## En enklere måte er å bruke funksjonen vectorize
