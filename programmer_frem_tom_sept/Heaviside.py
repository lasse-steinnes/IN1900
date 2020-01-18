### Oppgave 3.29: Heaviside funksjon

## a) lage en funksjon med H(x)
print("a)")

def H(x):
    if x < 0:
        return 0
    else:
        return 1

print("For x=3 har vi H(3)=%g" % (H(3)))  ## Test

## b) Lager test_H() for å teste
print("b)")

from math import e

def test_H():
    """Test value for Heavyside"""
    H_computed = [H(-10), H((-10)**-15), H(0),H(10**-15), H(10)]  # programverdier
    H_expected = [0,0,1,1,1]                                  # faktiske verdier
    tol = 1e-12
    for i,j in zip(H_computed, H_expected):                  # SPM!! SE under
        success = abs(H_computed[i] - H_expected[j]) < tol
        msg = "Beregnet heaviside=%g != %g (forventet)" % \
        (H_computed[i], H_expected[j])
        assert success, msg

print(test_H())

"""
SPM: Kunne jeg skrevet for i in zip(H_computed, H_expected)
og istedet benyttet meg av success = abs(H_computed[i][0] - H_expected[i][1])
"""

### Kjøreeksempel
"""
>> python Heaviside.py
a)
For x=3 har vi H(3)=1
b)
None
"""
