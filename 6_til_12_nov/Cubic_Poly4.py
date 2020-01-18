#### Oppgave 9.2 ###
## Lag en klasse for kubiske funksjoner

# c3*x**3 + c2*x**2 + c1*x + c0

## call operator og table metode som i Line og Parabola
## programmene


## Implementer klassen Cubic slik at den arver fra Parabola

## Kall opp funksjonalitet som vist i kap 9.1

## Lag en tilsvarende for 4.grads polynomer ved å arve fra Cubic
# c4*x**4 + 3*x**3 + c2*x**2 + c1*x + c0
##  Sett inn print i alle call metodene (alle klasser)

## Evaluer Cubic og 4.gradspolynom i ett punkt.
## Observer utskrift fra alle superklasser.

class Line(object):
    def __init__(self,c0,c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self,x):
        print(r'P_{1}'+'={:}, x:{}'.format(self.c0 + self.c1*x, x))
        return self.c0 + self.c1*x

    def table(self, L,R,n):
        """n punkter for L <= x <= R"""
        s = ''
        import numpy as np
        for x in np.linspace(L,R,n): # Lower, upper R, n points
            y = self(x)
            s += '%12g %12g\n' % (x,y)
        return s

class Parabola(Line):
    def __init__(self,c0, c1,c2):
        Line.__init__(self,c0,c1) # Line lagrer c0 og c1
        self.c2 = c2

    def __call__(self,x):
        y1 = Line.__call__(self,x) + self.c2*x**2
        print(r'P_{2}'+'={:}, x:{}'.format(y1, x))
        return y1

class Cubic(Parabola):
    def __init__(self,c0,c1,c2,c3):
        Parabola.__init__(self,c0,c1,c2) # Parabola lagrer c0, c1,c2
        self.c3 = c3

    def __call__(self,x):
        y2 = Parabola.__call__(self,x) + self.c3*x**3
        print(r'P_{3}'+'={:}, x:{:}'.format(y2, x))
        return y2

class Poly4(Cubic):
    def __init__(self,c0,c1,c2,c3,c4):
        Cubic.__init__(self,c0,c1,c2,c3) # Cubic lagrer c0, c1,c2
        self.c4 = c4

    def __call__(self,x):
        y3 = Cubic.__call__(self,x) + self.c3*x**3
        print(r'P_{4}'+'={:}, x:{}'.format(y3, x))
        return y3

print('\nUtskrift fra kall på klassen Cubic')
c1 = Cubic(1,2,1,1)
c1(2)

print('\nUtskrift fra kall på klassen Poly4')
p1 = Poly4(1,2,1,1,3)
p1(2)

### Kjøreeksempel
"""
>> python Cubic_Poly4.py

Utskrift fra kall på klassen Cubic
P_{1}=5, x:2
P_{2}=9, x:2
P_{3}=17, x:2

Utskrift fra kall på klassen Poly4
P_{1}=5, x:2
P_{2}=9, x:2
P_{3}=17, x:2
P_{4}=25, x:2
"""
### Kommentar: Superklassene får lik utskrift for poly4 og Cubic.
### Superklassene er i begge tilfeller Line, Parabola
###, i tillegg til Cubic, som er en superklasse for underklassen Poly4.
