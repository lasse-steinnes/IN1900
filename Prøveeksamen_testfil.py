w##
"""
a = [0, 1, 2, 3, 4]; b=a
b[0] = 50 ; print(a[0], b[0])
"""

### Gjennomgang av eksamen 2016
## Tydeligvis uten alternativer: SKRIVEOPPGAVER
""" Best å være på den sikre siden"""
# 1
"""
Output blir
Letter 2 is c
Letter 7 is h
Må huske at string indeks også har indeks som begynner på 0
"""
# 2
"""
# Når klassen har spesialmetoden:string, skrives det som står i return
# ut når man printer instansen.
# v0*t - 0.5*g*t**2,v0 = 5
"""

# 3
"""
Kaller funksjonen: python poly_list.py 1.0 3.5 2 (float,float,int)
Siden potenser beregnes før multiplikasjon, blir det 3.5 + 2
Dermed blir utskrift: The value of the polynomial is 5.5
"""

# 4
"""
Tekst og filbehandling: Utskrift: The total rainfall from
June to August was 58.00
"""

# 5
"""
(Ingen output, når man kaller en testfunksjon som går riktig)
"""

# 6 Seksjon 2: Programmering
"""
Skal implementer funksjon, kalle for x=2, og printe resultat

def x(x):
    if x < 0:
        f = 0
    elif 0 <= x < 2:
        f = x**2
    else:
        f = 4
    return f

print("When x is {:}, x is evaluated to {:}".format(2,x(2))
"""

# 7 En klasse for Paraboler.
"""
Skal lage en underklasse : Line, som skal arve fra parabola

## Riktig: Men husk å importere fra parabola da
from Parabola import *
class Line(Parabola):
    def __init__(self,c0,c1,c2=0):
        Parabola.__init__(self,c0,c1,c2)

# Tom print --> var en skrivefeil på eksamen: Kunne ha bytta ut call med tom streng
# Merk spesialmetoden call: Trenger ikke skrive instanse.solve(0.5)
# Holder å skrive instanse(0.5) # Kan kalle instansen som funksjon.
"""

# 8 File read and write
"""
# Skal lese en fil, og skrive en fil inni en funksjon
def sum_file(inputname,outputname):
    inn = str(inputname)
    ut = str(outputname)
    inndata = open(inn,'r')
    # Må gjøre string operasjon; vil ha ut tallene som liste
    s = []
    for line in inndata:
        s.append(line.split('')) # splitter ved whiteline, gir en liste
    inndata.close()

    for rad in range(len(s)):
        for index in range(len(s[rad])):
            s[rad][index] = float(s[rad][index])
    sum_list = [sum(rad) for rad in s]

## Har da to lister som begge nå inneholder floats
## Skal skrive den nye fila, må ha string operasjon:
    utdata = open(ut,'w')
    for rad in s:
        for verdi in rad:
            utdata.write('{:>10.2f}'.format(verdi))
            for sum in sum_list:
                utdata.write('{:>10.2f} \n'.format(sum))
    utdata.close()

# kaller
sum_file(innfil.txt,utfil.txt)
"""

# 9 Tilfeldige tall
"""
Sannsynligheten for å  trekke to eller flere hjerter når du
trekker frem kort fra et kortbord (uten tilbaketrekning)
52 kort, 13 hjerter.

Lager en liste med hjerter, andre kort
def hearts():
    from random import shuffle  # husk å importere!!!
    kortstokk = ['h','k','s','r']*13
    S = 1000 # antall eksperimenter
    trekk = 5
    M = 0
    for i in range(eks):   # merk den doble for løkka: 1 for eksperimentet
        hearts = 0
        shuffle(kortstokk)
        for trekk in range(trekk):  # en for de fem trekkene
            if a.pop() == 'h':
                hearts += 1
        if hearts >= 2:
            M += 1
    p = M/S
    return p
"""
# Oppgave 10 Random numbers
"""
Kommentar til meg sjøl: Oppgavene skal ligge nært opp til det du har gjort fra før,
bare at du må kunne kombinere de nødvendige metodene. Gjør standard
ting du er vant med, så går det raskere å kode. Har tross alt begrenset tid.

Tar heltall som input:
Simulerer å flippe en mynt N ganger
returnere antall hoder. Vektorisert kode.

def heads(N):
    N = int(N)
    import numpy as np
    flip = np.random.random_integers(0,1,size=(1,N)) # 1 rad, N kolonner
    sum = np.sum(flip)
    return sum

Riktig: PS - det virker som at hintene ofte er mangelfulle.
Dersom du husker metoden fra øvingen, så bruk heller denne om du er sikker på
metoden.
"""

# Oppgave 11: Taylor Series
"""
# Tester om vi kan summere og bruke riktig range!!
# Effektivisering av kode
# Differenslikninger: Skal løse system av
# Viktig å oppdatere i riktig rekkefølge:
# Funksjonen under skal kun gi summen; trenger ikke benytte lister


def taylor_exp_diffeq(x,N):
    e_p = 0
    a_p = 1
    sum_ = 0
    x = float(x) # Vær obs på å få riktig type
    for n in range(1,N+2):
        # PS: Her har range endret seg pga. diffeq avhenger av n-1 s.a nlower =1,, upper = n+1
        e_new = e_p + a_p
        a_new = x/n*a_p
        e_p = e_new
        a_p = a_new
    return e_new
"""

# Oppgave 12: ODESolver
"""
Tester arv
from ODESolver import ODESolver

class Midpoint(ODESolver):
    def advance(self):
        u,f,k,t = self.u,self.f,self.k,self.t
        dt = t[k+1]-t[k]
        k1 = dt*f(u[k],t[k])
        k2 = dt*f(u[k]+0.5*k1,t[k]+0.5*dt)
        # PS: vær obs på rekkefølgen inni f(u,t) (ikke f(t,u))!!! Var det dette jeg gjorde feil i prosjektet??
        u_new = u[k] + k2                     ## Nei, det var det ikke.
        return u_new
"""


# Skal skrive en testfunksjon til Midpointklassen
"""
Tester anvendelse av klasser
# Dersom differensialligningen er lineær skal
# tilnærmingen være lik den eksakte ned til maskinpresisjon
# PGA: konstant stigning.

def test_midpoint():
    import numpy as np
    # Lager et tilfelle
    def f(u,t):  # høyresiden
        return 5
    Y0 = 1
    t = np.linspace(0,10,11) #(intervallet [0,10])

    # numerisk metode
    solver = Midpoint(f) # instansen
    solver.set_initial_condition(Y0)
    u,t = solver.solve(t)

    # eksakt
    linear = lambda t: 5*t + 1
    np.vectorize(linear)
    u_eksakt = linear(t)

    # test
    tol = 1e-14 # Med maskinpresisjon mener de tydeligvis bare et lite tall
    success = np.all(abs(u - u_eksakt) < tol)
    msg = 'Den numeriske metoden er ikke implementert riktig'
    assert success msg
"""

# Oppgave 14
"""
from ODESolver0 import *
import numpy as np
def SEID(S0,E0,p,q,r,T):
     def f(u,t):
        S,E,I,D = u
        return [-p(t)*S*I,p(t)*S*I - q*E,q*E - r*I, r*I]

     ## løsning
     solver = RungeKutta4(f) # PS: Selvfølgelig skal f være inni her
     u0 = [S0,E0, 0, 0]
     solver.set_initial_condition(u0)
     t = np.linspace(0,T,10*T + 1)
     u,t = solver.solve(t)
     S,E,I,D = u[:,0], u[:,1], u[:,2], u[:,3] # husk at du må hente ut kolonner i matrisa u så det blir korrekt
     return S,E,I,D,t

# For tilfellet
S0 = 4.93
E0 = 0.55
q = 0.1
r = 1/10.38
p = lambda t: 0.0233
T = 100

S,E,I,D,t = SEID(S0,E0,p,q,r,T)

# plot
import matplotlib.pyplot as plt
plt.plot(t,S,label =   'S')
plt.plot(t,E, label = 'E')
plt.plot(t,I, label = 'I')
plt.plot(t, D, label = 'D')
plt.xlabel('tid[dager]')
plt.ylabel('Individer')
plt.title('Modell for Ebolas sykdomsutvikling \n i Sierra Lione (2014)')
plt.legend(loc = 'center right')
plt.show()
"""

## Dictionaries
"""
d = {6:100}
e = {6:6, 7:8}
d.update(e)
print(d)
"""

"""
n = 10
xlist = [i for i in range(n)]
ylist = [2*i for i in xlist]
print(ylist)
for i in zip(xlist,ylist):
    print(i)
""" # Kommentar: zip slår sammen x,y til tuppelpar inni en liste
"""
import numpy as np
x = np.zeros(len(range(10)))
print(x)
""" # Komm: range gir iterator med index 0-9 --> lenge 10

"""
import random
import numpy as np
elem = [0,1,2,3]
random.shuffle(elem)
print(elem)
"""
"""
class Diff:
     def __init__(self, f, h=1E-5):
         self.f = f
         self.h = float(h)
class Forward1(Diff):
     def __call__(self, x):
         f, h = self.f, self.h
         return (f(x+h) - f(x))/h

dfdx = Forward1(lambda x: x**2)
print(dfdx(0.5))
""" # Eksempel på bruk av arv, og spesialmetoden __call__
"""

import sys
C = '20.0 degrees'
try:
    C = float(C) ## fordi ikke kun tall

except ValueError:
    print ('Cannot convert %s to float' %type(C))
    sys.exit(1)

F = 9.0*C/5 + 32
print ('%g C is %.1fF' % (C, F))
"""
##
def is_prime(k):
    if k == 1:
        prime = False
    elif k == 2:
        prime = True
    else:
        for j in range(2,k):
            if k%j == 0:
                prime =  False
                break
            else:
                prime =  True
    return prime

def primes(n):
    prim = []
    nprim = 0
    k = 2
    while nprim < n:
        if is_prime(k):
         prim.append(k)
         ### Må huske at når du bruker while-løkke, så må du ha counter
         nprim += 1
         k += 1
    return prim

print(primes(5))
