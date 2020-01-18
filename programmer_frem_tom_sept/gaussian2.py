### Oppgave 3.22: Implementer en gaussisk funksjon
## Algoritme:
#   Velger først å importere nødvendige funksjoner
#

from math import exp,pi, sqrt

def f(n, m=0, s=1):
    min_ = m - 5*s
    maks_ = m + 5*s
    steps = (maks_ - min_)/n

    for x in range(min_, maks_ + 1):
         f_x = (1/(sqrt(2*pi)*s))*exp((-1/2)*((x-m)/s)**2)
         print(" %.1e %.1e" %(x,f_x))
         x += steps

print("""Dette er tabellen til en gaussisk funksjon med x i intervallet
[m-5s,m+5s], der m=%g og s=%g, for n=%g."""%(0,1,5))
print("""-------------------
   x      f(x)
-------------------""")
x2n5 = f(n=5)
print("-------------------")

### Kjøreeksempel
"""
>> python gaussian2.py
Dette er tabellen til en gaussisk funksjon med x i intervallet
[m-5s,m+5s], der m=0 og s=1, for n=5.
-------------------
   x      f(x)
-------------------
 -5.0e+00 1.5e-06
 -4.0e+00 1.3e-04
 -3.0e+00 4.4e-03
 -2.0e+00 5.4e-02
 -1.0e+00 2.4e-01
 0.0e+00 4.0e-01
 1.0e+00 2.4e-01
 2.0e+00 5.4e-02
 3.0e+00 4.4e-03
 4.0e+00 1.3e-04
 5.0e+00 1.5e-06
-------------------
"""
