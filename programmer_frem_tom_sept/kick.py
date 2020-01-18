""" Oppgave 1.11 om luftmotstand"""

from math import pi

### Definerer variabler

q = 1.2 ## lufttetthet [kg/m**3]
Vsoft = (30*1000)/3600## Hastighet, velocity [m/s]
Vhard = (120*1000)/3600 ## Hastighet, velocity [m/s]
a = float(11)/100 ## radius to ball [m]
m = 0.43 ## masse til ballen [kg]
A = pi*(a**2)  ## normal til hastighetsretningen
Cd = 0.4 ## dragningskoeffisienten (variarer m. hastighet)
g = 9.81 ## gravitasjonskonstant [m/s**2]
## Newton (N) = kg m/s**2 ##

"""Dragningskraft"""

Fd1 = (1/2)*Cd*q*A*(Vsoft**2)
print("Dragningskraften er %.1e N for V=%.2g" %(Fd1, Vsoft))

### Utskrift ###
""" Dragningskraften er 6.3e-03 N for V=0.83 """

Fd2 = (1/2)*Cd*q*A*(Vhard**2)
print("Dragningskraften er %.1g N for V=%.2g" %(Fd2, Vhard))

""" gravitasjonskraft"""

Fg = m*g
print("Gravitasjonskraften er %.1f N for m=%g" %(Fg,m))

""" ratio """
ratio1 = Fd1/Fg
ratio2 = Fd2/Fg
print("""Forholdet mellom dragningskraften og gravitasjonskraften
er %.2e for V=%.2e, og %.2e for V=%2.e."""%(ratio1, Vsoft ,ratio2, Vhard))


### Utskrift ####
"""python kick.py
>> Dragningskraften er 6.3e-01 N for V=8.3
>> Dragningskraften er 1e+01 N for V=33
>> Gravitasjonskraften er 4.2 N for m=0.43
>> Forholdet mellom dragningskraften og gravitasjonskraften
er 1.50e-01 for V=8.33e+00, og 2.40e+00 for V=3e+01."""

"""Fra utskriften ser man at dragningskraften
er større enn gravitasjonskraften" for V=33, og omvendt for V=8.3.
Man kan konkludere med at luftmotstanden får med å si med høy
hastighet"""
