## Skal skrive et program som
# 1: tar a, b og c koeffisientene som data attributter i __init__
class Quadratic(object):        # unødvendig med object,
                                # for den er der automatisk, men
    def __init__(self, a,b,c):      # greit for å huske at den er der.
        self.a = a
        self.b = b
        self.c = c

# 2: Beregner en verdi for funksjonen ax**2 + b*x + c

    def value(self, x):
        a, b, c = self.a, self.b,self.c
        return a*x**2 + b*x + c

# 3: Lager en tabell for f over intervallet [L,R]
    def tabell(self,L,R):
        a,b,c = self.a,self.b,self.c
        print('-----------------')
        print(' x       f(x)')
        print('-----------------')
        for x in range(L,R+1):
            f1 = Quadratic(a,b,c)
            print('{:>5} {:>10.2f}'.format(x,f1.value(x)))
        print('-----------------')
    # Har jeg denne noe sted?
# 4: Beregner røttene til f

    def roots(self):
        a,b,c = self.a,self.b,self.c
        from numpy.lib.scimath import sqrt # Kan få komplekse røtter
        x1 = (- b + sqrt((b**2) - 4*a*c))/(2*a)
        x2 = (- b - sqrt((b**2) - 4*a*c))/(2*a)
        return x1, x2

def test_value():
    a = 2
    b = -5
    c = -3
    x = 2

    q1 = Quadratic(a,b,c)
    expected = a*x**2 + b*x + c
    computed = q1.value(x)

    tol = 1e-14
    success = abs(expected -computed)< tol
    msg = """program values:{:.2f} != expected: {:.2f}""".format(expected,computed)
    assert success, msg

test_value()

def test_roots_float():
    """Test if roots are correct float objects"""
    a = 2
    b = -5
    c = -3
    exact_x1 = 3              # Håndregnet verdi
    exact_x2 = -(1/2)         # Håndregnet verdi

    q1 = Quadratic(a,b,c)
    computed = q1.roots()
    x1 = computed[0]
    x2 = computed[1]
    success = (exact_x1 - x1) + (exact_x2 - x2) < 1e-14
    msg = """program values: x1=%g, x2=%g,
    exact values: x1=%g x2 =%g""" %(x1,x2,exact_x1,exact_x2)
    assert success, msg

test_roots_float()

def test_roots_complex():
    """Test if roots are correct complex objects"""
    from numpy.lib.scimath import sqrt
    a = 1
    b = 2
    c = 3
    exact_x1 = - 1 + sqrt(-2)        # Håndregnet verdi
    exact_x2 = -1 - sqrt(-2)         # Håndregnet verdi

    q1 = Quadratic(a,b,c)
    computed = q1.roots()
    x1 = computed[0]
    x2 = computed[1]
    success = (exact_x1 - x1) + (exact_x2 - x2) < 1e-14
    msg ="""program values: x1={:.2f}, x2={:.2f},
    exact values: x1={:.2f} x2={:.2f}""".format((x1),(x2),(exact_x1),(exact_x2))
    assert success, msg

test_roots_complex()

### for å ha noe kjøreeksempel, så
if __name__== '__main__':   # Gjør at man kan bruke
                            #  programmet som modul uten å få print
    print('\nTest av Quadratic:\n')
    q1 = Quadratic(2,-5,3)
    value =  q1.value(2)

    print('Utskrift av verdien:\n')
    print('{:.2f} \n'.format(value))
    print('Utskrift av tabellen: \n')
    tabell = q1.tabell(2,5)
    print('\n')
    print('Utskrift av røttene:\n')
    røtter = q1.roots()
    print("""For a={:g}, b={:g}, c={:g} har annengradslikningen
    røttene x1={:g} og x2={:g}""".format(2,-5,3, røtter[0],røtter[1]))

## Kjøreeksempel ##
"""
>> python Quadratic.py

Test av Quadratic:

Utskrift av verdien:

1.00

Utskrift av tabellen:

-----------------
 x       f(x)
-----------------
    2       1.00
    3       6.00
    4      15.00
    5      28.00
-----------------


Utskrift av røttene:

For a=2, b=-5, c=3 har annengradslikningen
    røttene x1=1.5 og x2=1

"""
