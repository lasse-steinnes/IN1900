### Oppgave 7:11 ###


#Skriv om funksjonen til å inneholde class og str

class F(object):
    def __init__(self,a,w):
        self.a = a
        self.w = w

    def __call__(self,x):
        a, w = self.a, self.w
        from math import sin,exp
        return exp(-a*x)*sin(w*x)

    def __str__(self):
        a,w = self.a,self.w
        return 'exp(-a*x)*sin(w*x), med a={},w={}'.format(a,w)

## Kjøreeksempel: Fra python shell
"""
>> python
(Python 3.6.1 |Anaconda 4.4.0 [...])
>>> from F2 import F
>>> f = F(a=1.0,w=0.1)
>>> from math import pi
>>> print(f(x=pi))
0.01335383513703555
>>> f.a = 2 # Kommentar: Endrer a attributten for tilfellet(insidens) f
>>> print(f(pi))
0.0005770715401197441
>>> print(f)
exp(-a*x)*sin(w*x), med a=2,w=0.1
"""
