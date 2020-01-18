### Prøveeksamen test
from math import factorial

import sys

def taylor_term(x,n):
     return x**n/factorial(n)

# Skal skrive et programm som beregner summen og printer resultatet

#x = float(sys.argv[1])
#N = int(sys.argv[2])
sum_ = 0

try:
    x = float(sys.argv[1])
    N = int(sys.argv[2])

except IndexError:
    print("For få argumenter er oppgitt")
    exit(1)
except ValueError:
    print("Kommandolinjeargument er av feil type")
    exit(1)



for n in range(N+1):
    taylor = taylor_term(x,n)
    sum_ += taylor

print(sum_)
