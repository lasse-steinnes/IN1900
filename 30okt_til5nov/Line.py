### Skal lage en klasse line ###
# Kan løse denne med input eller sys.argv
import sys

class Linje(object):

    def __init__(self):
        """
        p1 og p2 skal være lister,
        slik at inputen ikke kan forandres.
        På formen (x0,y0)
        """
        """#if p1 and p2 != None:""" # Prøvde å fikse testfunksjonen(se komm.)
        import sys
        self.p1 = eval(sys.argv[1]) # kunne bestemt til x0, y0, men vil ha kun p1 og p2 som input
        self.p2 = eval(sys.argv[2]) # husk float/eval på input:blir string

        """#else:
        #    self.p1 = p1
        #    self.p2 = p2"""

    def sekant(self):
        p1,p2 = self.p1, self.p2
        a = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p1[1]-a*p1[0]
        return a, b

    def __call__(self,x):   # trenger jeg egentlig self her? # call erstatter value-metoden
        p1,p2 = self.p1,self.p2
        l1 = Linje()
        s = l1.sekant()
        return s[0]*x + s[1]

    def __str__(self):                                       # erstatter formula (formatert print)
        p1,p2 = self.p1,self.p2
        l1 = Linje()
        s = l1.sekant()
        return 'a*x + b; a ={}, b={} når p1={} og p2={}'\
                .format(s[0],s[1],p1,p2)    #

def test_Linje():
    ## Lager et spesialtilfelle
    """
    PS: Denne testfunksjonen kan bare kalles gitt dette
    spesialtilfellet i kommandovinduet: det er en svakhet!
    """
    p1 = [1.0,0]
    p2 = [2.0,3.0]
    a = (3.0-0.0)/(2.0-1.0)
    b = 0.0-a*1.0
    x = 1.8

    expected = a*x + b
    l1 = Linje()
    computed = l1(x)

    tol = 1e-14
    success = abs(expected-computed) < tol
    msg = 'Den beregnede y-verdien stemmer ikke overens med forventet verdi'
    assert success, msg

print("""Når test_Linje kjøres kommer ingen output.
Funksjonen fungerer som den skal""")
test_Linje()

print("""\nNår man kaller funksjonen for insidens skrevet i kommandovinduet får man med print:""")
l1 = Linje()
print(l1) # kaller __str__ fordi ekvivalent med print(l1__str__())
value = l1(1.8) # kan skrive som vanlig funksjon pga call.
print('\nPrint av y-verdien')
print('{:.2f}'.format(value))

### Kjøreeksempel
"""
>> python Line.py [1.0,0] [2.0,3.0]
Når test_Linje kjøres kommer ingen output.
Funksjonen fungerer som den skal

Når man kaller funksjonen for insidens skrevet i kommandovinduet får man med print:
a*x + b; a =3.0, b=-3.0 når p1=[1.0, 0] og p2=[2.0, 3.0]

Print av y-verdien
2.40
"""
## Komm: Forbedre testfunksjonen hvordan?
