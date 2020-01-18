#### Forelesning 27.sept

""" Midtsemester: digital eksamen i 'Inspera'"""
## bruk matplotlib alltid,
##  scitools oppdateres ikke lenger

########### animasjon i matplotlib (kap5)###############
# Forventer at man kan plotte og veit om en generell måte å gjøre dette på
# liker best å benytte vektorisert array når man lager kurve
#   plot(), show()

#### Lage en animasjon, som med tegnefilm
# lager mange plot, og setter de etter hverandre
## Gir illusjonen av et plot som beveger seg

# Eks. plotte en gausskurve for ulike s
from matplotlib.pyplot import *
from numpy import *

def f(x,m,s):
    1/sqrt(2*pi)*(1/s)*exp(-0.5((x-m)/s))
"""
### Generell kode. Alt 1
"""
# lag array med s-verdier ved å bruke linspace
# lag array med x-verdier
# sett aksene, beregn f(x) (min) og maks
# lag en liste av line objekter

# for løkke!
### sett y=
## lines[0].set_ydata(y) # oppdaterer plotter og tegner igjen
# draw()
# pause(0.1)

"""
###  Generell kode. Alt 2
"""
# Samme for loop, ganske lik kode
# printf format for å lagre filer med ulike navn
#### Bruker framecounter, som setter til 0 før loopen og legges til 1
## bruker ikke pause. Må sette dem sammen vha Image Magick

"""
### Generell kode. Alt 3 : Moderne måte å lage animasjon i matplotlib
"""
### Lik kode frem til  man har satt f maks
### def init
#    lines.setdata
##   return lines
# def update
# return lines
### Opdaterer y data
"""
FuncAnimation(gcf(), update, frames=s_values,
               init_func=init, blit=True)
ani.save('test.gif')
"""
# gcf get current figure

########### lage egne moduler (kap 4) ##################
## Samling av nyttige funksjoner og data

## Eks. Skal lage funksjon med fire moduler
## I) Skriver funksjoner
## ii) Lagre som egen fil <- bruk som modul med import

######################### del 2 #########################
## Adding a test block in a module file



######## Interaktiv del
"""
5.13
"""
# plot trajectory of ball
## PS: Skal plotte ballbanen for y >= 0.Veit ikke for
# hvilke verdier av x  der y >=0.
# import sys
#import numpy as np
#from matplotlib.pyplot import *
#from math import tan, cos, sqrt
#import matplotlib.pyplot as plt
"""
g = 9.81

# skriv funksjonen
def f(x,y0, theta, v0, g):
    y = x*(tan(theta))-(1/(v0**2))*(g*x**2)/(cos(theta)**2) + y0
    return y

# Les argument fra kommandolinjen (Burde hatt en try except block)
y0 = float(sys.argv[1])
theta = float(sys.argv[2])
v0 = float(sys.argv[3])


# Løs likningen for en x med ABC formelen
a = -(1/(v0**2))*(g)/(cos(theta)**2)
b = tan(theta)
c = y0

x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)

print(x1,x2)

x_max =(x1,x2)

x = linspace(0,x_max, 100) # lager array av x
y = f(x,y0,theta, v0, g)   # y blir også array

plot(x,y)
show()
"""

"""
5.14: Judgeplot
"""
"""
x = np.linspace(0,2,1000) # endrer 20 til 1000
y = np.cos(18*(np.pi)*x)
plt.plot(x,y)
plt.show()
""""

"""
5.39 Animer evolusjonen av taylor approksimasjonen
"""
# approksimasjonen blir bedre for hvert ledd
# Skal lage en animasjon der man ser dette

#k = 0 f_k = 1
#k = 1 f_k = x
#k = 2 f_k = x**2/2

# n er antall x verdier , exact er den faktiske funksjonen
"""animate_series(fk, M, N, xmin, xmax, ymin, ymax,n,exact)"""

from numpy import *
from math import factorial ## fins ikke i numpy
import matplotlib.pyplot as plt

def animate_series(fk, M, N, xmin, xmax, ymin, ymax,n,exact):
    # Beregn x verdier og referanseløsning

    # Initialiser plot med akser, kall plottet

    # oppdater data og gjentegne i en for loop

# Kall funkjonen med korrekte argumenter
