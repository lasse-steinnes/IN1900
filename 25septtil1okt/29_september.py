#################  29_september, informatikk forelesning  ####################
###  Oppgave 5.39: En av forelesers favorittoppgaver

### s(x;M,N) = taylor series
## a: Skal sammenligne med a = 100. Taylor blir mer lik når antall ledd øker.


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

"""
from numpy import *
from math import factorial ## fins ikke i numpy
import matplotlib.pyplot as plt

# Oppgave a
def animate_series(fk, M, N, xmin, xmax, ymin, ymax,n,exact):
    # Beregn x verdier og referanseløsning, samt lage en tom array for y verdier som fylles inn senere
    x = linspace(xmin,xmax,n) # Se på funksjonsvariablene og bruk disse om dem skal anvendes
    y_exact = exact(x)     ## for en funksjon exact (kan evaluere array)
    s = zeros_like(x)  ### Denne lager en array med nuller lik x i lengde og type
                        ## Brukes for y

    # Initialiser plot med akser, kall plottet
    plt.plot(x,y_exact)
    lines = plt.plot(x,s)              # Lyst til å endre denne senere og lagrer det derfor som et objekt
    plt.axes([xmin,xmax,ymin,ymax])

    # oppdater data og gjentegne i en for loop
    for k in range(M, N+1):
        s += fk(x,k)      ### bruker funksjonen fk = (x^k)/factorial(x) Hvert ledd for y legges til array
        lines[0].set_ydata(s)
        plt.draw()
        plt.pause(0.25)

# Oppgave b

# Kall funkjonen med korrekte argumenter
def f_sin(x,k):
    fk = ((-1)**k)*x**(2*k+1)/(factorial(2*k+1))   ### Hvert ledd
    return fk

##c
def exp_inv(x):
    return exp(-x)

def f_exp(x,k):
    return (-x)**k/factorial(k)


##  bsin er det samme som exact funksjonen

animate_series(f_sin,0,40,0,13*pi,-2,2,100,sin)
"""
###  c
# animate_series() ## Se oppgaveteksten

"""
### Oppgave A.1
"""
## Løser denne for alle naturlige tall, ikke kun partall
from numpy import *

# oppgave a
def sequence_a(N):
    index_set = range(N+1)  # av type range(stop)
    a = zeros(len(index_set))   # lag a som array av nuller som kan fylles på etterpå med en for løkke

    for n in index_set:
        a[n] = (7+1.0/(n+1))/(3-1.0/(n+1)**2) ## gjør om array til a for hver index

    return a

print(sequence_a(100))
print(7.0/3.0)
# print(sequence_a(100)[100])

# Oppgave b
def sequence_b(N):
    index_set = range(N+1)
    D = zeros(len(index_set))
    for n in index_set:
        D[n] = sin(2**(-n))/2**(-n)
    return D

print(sequence_b(10)[-1])

# Oppgave c
## omdefinering av leddet
# følger definisjonen av den deriverte i punktet
# følgene konvergerer mot f i punktet x

def D(f,x,n):
        index_set = range(n+1)   # laget et index set
        D = zeros(len(index_set))
        for n in index_set:
            h = 2**(-n)
            D[n] = (f(x+h)-f(x))/h    # For en funksjon x
        return D

import matplotlib.pyplot as plt
D1 = D(sin,pi,80)     ### endret fra 0 til pi
plt.plot(range(80+1), D1, 'o') ### Hvert punkt blir en sirkel
plt.show()

### Ser at den ikke konvergerer for n=51 eller n=52
### poeng: Avrundingsfeil når n blir stor, fordi h blir veldig liten.
## dvs pi + h ≈ pi, og vi har pi - pi = 0, teller, mens i nevner avrundes den til noe over 0.
### Ser at h er 1.10**-16 something når feilen skjer.
