### Oppgave 3.8 Skriv en funksjon for å løse ax^2 + b*x + c = 0

# a) Algoritmen for å løse dette problemet:
# 1: Skrive ned ABC-formelen som funksjon med a,b og c som variabler
# 2: Bruk if, og elif til å skille mellom flytobjekter (reelle røtter)
# og komplekse objekter. Unngår dette ved å benytte numpy.lib.scimath
print("a)")

from numpy.lib.scimath import sqrt
from math import e

def roots(a,b,c):
    x1 = (- b + sqrt((b**2) - 4*a*c))/(2*a)
    x2 = (- b - sqrt((b**2) - 4*a*c))/(2*a)
    return x1, x2

print("""For a={:g}, b={:g}, c={:g} har annengradslikningen
røttene x1={:g} og x2={:g}""".format(1,2,3,roots(1,2,3)[0],roots(1,2,3)[1]))

# b) Tolker oppgaven som at man skal lage to funksjoner som tester om
# røttene er komplekse, eller reelle. Dette kan imidlertidig testes i en og
# samme funksjon
"""
def complex_or_real(a,b,c):
    if (b**2) - 4*a*c < 0:
        return "complex = True"  # Dette er en måte å gjøre det på,
    elif (b**2) - 4*a*c >= 0:    # men oppfyller ikke kravene
        return "real = True"     # til en testfunskjon.
print(complex_or_real(1,2,1))
"""

## print(roots(1,2,1))     Test
## print(roots(1,2,1)[0])

print("b)")

def test_roots_float():
    """Test if roots are correct float objects"""
    a = 2
    b = -5
    c = -3
    exact_x1 = 3              # Håndregnet verdi
    exact_x2 = -(1/2)         # Håndregnet verdi
    x1 = roots(a,b,c)[0]
    x2 = roots(a,b,c)[1]
    success = (exact_x1 - x1) + (exact_x2 - x2) < 1e-14
    msg = """program values: x1=%g, x2=%g,
    exact values: x1=%g x2 =%g""" %(x1,x2,exact_x1,exact_x2)
    assert success, msg

test_roots_float()
print(test_roots_float())

def test_roots_complex():
    """Test if roots are correct complex objects"""
    a = 1
    b = 2
    c = 3
    exact_x1 = - 1 + sqrt(-2)        # Håndregnet verdi
    exact_x2 = -1 - sqrt(-2)         # Håndregnet verdi
    x1 = roots(a,b,c)[0]
    x2 = roots(a,b,c)[1]
    success = (exact_x1 - x1) + (exact_x2 - x2) < 1e-14
    msg ="""program values: x1={:.2f}, x2={:.2f},
    exact values: x1={:.2f} x2={:.2f}""".format((x1),(x2),(exact_x1),(exact_x2))
    assert success, msg

test_roots_complex()
print(test_roots_complex())

### Kjøreeksempel:
"""
>> python roots_quadratic.py
a)
For a=1, b=2, c=3 har annengradslikningen
røttene x1=-1+1.41421j og x2=-1-1.41421j
b)
None
None
"""
# Kommentar: At testene ikke skriver noe ut vil si at programmet kjører riktig.
## SPM: Er det en måte å få den imaginære delen med færre desimaler?
