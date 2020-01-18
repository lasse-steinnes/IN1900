### Oppgave 9.11 ###

### Implementer formelene
### Seksjon 9.2
#### Skal være en underklasse av diff fra seksjon 9.2
#f_approx = (f(x-2h) - 4*f(x-h)+3f(x) + 3*f(x))/2*h ## Utledet med bruk av Newton polynomet, med tre punkter

def g(t):
    from numpy import exp
    return exp(-t)

def dg(t):
    from numpy import exp
    return -exp(-t)

# t = 0
# h = 2**(-k)
# k = 0,14. # Skriv ut feilen for g'(t). # Greit å bruke linspace og array

# Sammenlign med backward1 for g(t) og de ovenfor

## Bruker definisjonen av den deriverte, samt ulike varianter av den deriverte
## til numerisk approksimasjon i klassen Diff og ulike underklasser
import numpy as np

class Diff(object):
    def __init__(self,f,h):
        self.f = f
        self.h = h

class Backward1(Diff):
    def __call__(self,x):
        f,h = self.f, self.h
        return (f(x) - f(x-h))/h
"""
    def format(self):
        f,h = self.f, self.h
        print('Backward1, (f(x) - f(x-h))/h)')
        for i in range(len(h)):
            print(, h:{:.3e}'.format()
"""

class Backward2(Diff):
    def __call__(self,x):
        f,h = self.f,self.h
        f_diff = (f(x-2*h) - 4*f(x-h)+3*f(x))/(2*h)
        return f_diff


t = np.zeros(15)
k = np.linspace(0,14,15)
h = 2**(-k)   # vektorisert beregning
# print(h)

b2 = Backward2(g,h)
b2t = b2(t)

b1 = Backward1(g,h)
b1t = b1(t)

error1 = abs(dg(t)-b1t)
error2 = abs(dg(t)-b2t)
print('--------------------------------------------------------------------')
print('{:>5s}{:>15s}{:>15s}{:>15s}{:>15s}'.format('h','Bw1','Bw2','err1','err2'))
print('--------------------------------------------------------------------')
for i in range(len(h)):
    print('{:>5.2e}{:>15.4e}{:>15.4e}{:>15.4e}{:>15.4e}'.format(h[i],b1t[i],b2t[i],error1[i],error2[i]))
print('---------------------------------------------------------------------')

## Kjøreeksempel
"""
>> python Backward2.py
--------------------------------------------------------------------
    h            Bw1            Bw2           err1           err2
--------------------------------------------------------------------
1.00e+00    -1.7183e+00    -2.4204e-01     7.1828e-01     7.5796e-01
5.00e-01    -1.2974e+00    -8.7660e-01     2.9744e-01     1.2340e-01
2.50e-01    -1.1361e+00    -9.7476e-01     1.3610e-01     2.5239e-02
1.25e-01    -1.0652e+00    -9.9427e-01     6.5188e-02     5.7264e-03
6.25e-02    -1.0319e+00    -9.9864e-01     3.1911e-02     1.3649e-03
3.12e-02    -1.0158e+00    -9.9967e-01     1.5789e-02     3.3326e-04
1.56e-02    -1.0079e+00    -9.9992e-01     7.8533e-03     8.2341e-05
7.81e-03    -1.0039e+00    -9.9998e-01     3.9164e-03     2.0465e-05
3.91e-03    -1.0020e+00    -9.9999e-01     1.9557e-03     5.1012e-06
1.95e-03    -1.0010e+00    -1.0000e+00     9.7720e-04     1.2734e-06
9.77e-04    -1.0005e+00    -1.0000e+00     4.8844e-04     3.1812e-07
4.88e-04    -1.0002e+00    -1.0000e+00     2.4418e-04     7.9502e-08
2.44e-04    -1.0001e+00    -1.0000e+00     1.2208e-04     1.9872e-08
1.22e-04    -1.0001e+00    -1.0000e+00     6.1038e-05     4.9695e-09
6.10e-05    -1.0000e+00    -1.0000e+00     3.0518e-05     1.2369e-09
---------------------------------------------------------------------
"""
## Kommentar: Ser at feilen blir mindre desto mindre h er.
#           Feilen er minst for bw2.
