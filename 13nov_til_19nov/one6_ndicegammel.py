###  Oppgave 8.6 ###
# Skal beregne sannsynligheten for å få minst en terning
# med seks, når man kaster n terninger.
# Bruker komplementær hendelser
# Sannsynlighet for ingen seksere er (5/6)^n
# A u B; A, B eller begge tilfellen samtidig
# A n B; A og B (multipliserin fordi uavhengige hendelser)
# Dermed blir sannsynligheten for minst en

import sys
# les av antall kast: n
# og antall simuleringer: S
# fra kommandolinja
try:
    n = int(sys.argv[1])
    S = int(sys.argv[2])
except IndexError:
    print("Manglende verdier. Oppgi:\n n: antall kast, S: Antall simuleringer")

# (Monte Carlo simulering)
"""
def terning(n,S):
    import numpy as np
    sum_ = 0
    for s in np.arange(S):
        utfall = np.random.random_integers(1,6,size=n)
        suksess = utfall == 6
        M = np.sum(suksess)
        p = M/n
        sum_ = sum_ + p
    mean = sum_/S
    print(mean)
    return mean
"""
#1 - (5/6)**n
def terning(n,S):
    import numpy as np
    utfall = np.random.random_integers(1,6,size=(S,n))
    suksess = utfall == 6
    M = np.sum(suksess)
    p = M/n
    mean = p/S
    print(mean)
    return mean
terning(n,S)

## For å delvis verifisere
## 11/36 for n=2
## Observere at tilnærmet sannsynlighet nærmer seg eksakte
## med økt antall simuleringer
