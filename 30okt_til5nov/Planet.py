## Oppgave. 7.1 FY-heftet

class Planet():

    def __init__(self,navn,radius,masse):
        self.navn = navn
        self.radius = radius
        self.masse = masse


    def tetthet(self):
        r, m = self.radius,self.masse
        from math import pi
        return m/(4/3*pi*r**3)  # kg/m**3

    def print_info(self):
        n, r, m = self.navn, self.radius,self.masse
        print('--------------------')
        print('Informasjon om {:s}:'.format(n))
        print('--------------------')
        print('radius:{} m '.format(r))
        print('masse:{} kg'.format(m))
        #print('populasjon:{:.2e} individer'.format(p)) Tenkte først man skulle ha populasjon i klassen
        p1 = Planet(n,r,m)
        t1 = p1.tetthet()
        print(r'tetthet:{:.2e} kg/m^3'.format(t1))
        print('--------------------')


## Oppgave b
n = 'Jorda'       # navn (string)
r = 6371*1000 # radius [m]
m = 5.972e24    #masse [kg]

planet1 = Planet(n,r,m)
planet1.populasjon = 7497486172   # Men dette er jo ikke standard måte å gjøre det på
print('Deloppgave a: \nKjører tetthet:')
print(planet1.tetthet())
print('\nKjører print_info')
planet1.print_info()
print('\nDeloppgave b, \nUtskrift:')
print(planet1.navn,'har en populasjon på',planet1.populasjon)

## Kjøreeksempel
"""
>> python Planet.py
Deloppgave a:
Kjører tetthet:
5513.258738589093

Kjører print_info
--------------------
Informasjon om Jorda:
--------------------
radius:6371000 m
masse:5.972e+24 kg
tetthet:5.51e+03 kg/m^3
--------------------

Deloppgave b,
Utskrift:
Jorda har en populasjon på 7497486172
"""
