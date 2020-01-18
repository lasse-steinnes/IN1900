### Skal lage en klasse line ###
# Kan løse denne med input eller sys.argv
import sys

class Linje(object):

    def __init__(self,p1,p2):
        """
        p1 og p2 skal være lister,
        slik at inputen ikke kan forandres.
        På formen (x0,y0)
        """
        import sys
        self.p1 = p1 # kunne bestemt til x0, y0, men vil ha kun p1 og p2 som input
        self.p2 = p2 # husk float/eval på input:blir string


    def sekant(self):
        p1,p2 = self.p1, self.p2
        a = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p1[1]-a*p1[0]
        return a, b

    def value(self,x):   # trenger jeg egentlig self her? # call erstatter value-metoden
        p1,p2 = self.p1,self.p2
        l1 = Linje(p1,p2)
        s = l1.sekant()
        return s[0]*x + s[1]

    def __str__(self):                                       # erstatter formula (formatert print)
        p1,p2 = self.p1,self.p2
        l1 = Linje(p1,p2)
        s = l1.sekant()
        return 'a*x + b; a ={}, b={} når p1={} og p2={}'\
                .format(s[0],s[1],p1,p2)    #

def test_Linje():
    ## Lager et spesialtilfelle
    p1 = [1.0,0]
    p2 = [2.0,3.0]
    a = (3.0-0.0)/(2.0-1.0)
    b = 0.0-a*1.0
    x = 1.8

    expected = a*x + b
    l1 = Linje(p1,p2)
    computed = l1.value(x)

    tol = 1e-14
    success = abs(expected-computed) < tol
    msg = 'Den beregnede y-verdien stemmer ikke overens med forventet verdi'
    assert success, msg

"""
print("""Når test_Linje kjøres kommer ingen output.
Funksjonen fungerer som den skal""")
test_Linje()
"""
#print("""\nNår man kaller funksjonen for insidens skrevet i kommandovinduet får man med print:""")
#p1 = [1.0,0]
#p2 = [2.0,3.0]
#l1 = Linje(p1,p2)
#print(l1) # kaller __str__ fordi ekvivalent med print(l1__str__())
#value = l1.value(1.8) # kan skrive som vanlig funksjon pga call.
#print('\nPrint av y-verdien')
#print('{:.2f}'.format(value))

### Kjøreeksempel
"""
>> python
(Python 3.6.1 |Anaconda 4.4.0 [...])

from Line_revidert import Linje, test_Linje
>>> line = Linje((0,-1),(2,4))
>>> print(line.value(0.5),line.value(0),line.value(1)
... )
0.25 -1.0 1.5
>>> test_Linje()
"""

"""
Kommentar: Se gjerne linje.py, der jeg har arbeidet med user input
Er det en måte å få test_funksjonen til å virke i alle tilfellene?
(Jeg leste oppgaven litt feil først)
"""
