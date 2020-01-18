### Forelesning in1900, 25 okt. ###
""" TEMA ### Klasser ####"""
"""
s = "This is a string"
print(type(s))
"""
# <class 'str'>

#l = s.split()
#print(type(l))
#"""<class 'list'> # innebygget klasse, trenger ikke kalle kstruktøren
"""

# Poeng: Når man bruker split går string over til en
# liste av strings

#Poeng2: Man har brukt klasser hele veien i in1900.
# Funksjoner lagret inni klasser.
"""
class Y:
    def __init__(self,v0):  # Konstruktør: Lager alle variable vi
                            # ønsker skal være tilgjengelige i klassen
        self.v0 = v0        # Globale variabler i klassen
        self.g = 9.81

    def value(self,t):
        return self.v0*t - 0.5*self.g*t**2

y1 = Y(3)  # Gjør om self til tilfellet(instance) y1 når v0=3)
           # Lager objekt av klassen Y
           # Må kalle konstruksjonen først på en måte

v = y1.value(0.1) # Kaller value for tilfellet y1 med t = 1
# v = Y.value(y1,t=0.1) Eventuelt. y1 tilsvarer self (klasse.metode)
            # Se at syntaksen er som med moduler, f.eks. math.sqrt

print(v)       # Skaffer verdien for funksjonen
# 0.25095
print(y1.v0)  #Skaffer variabler i tilfellet y1
print(y1.g)
# print() # Hvordan printe t-variabelen?
# 3
# 9.81
