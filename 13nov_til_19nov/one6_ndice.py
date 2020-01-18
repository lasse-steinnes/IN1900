###  Oppgave 8.6 ###
# Skal beregne sannsynligheten for å få minst en terning
# med seks, når man kaster n terninger.


import sys
# les av antall kast: n
# og antall simuleringer: S
# fra kommandolinja
try:
    n = int(sys.argv[1])
    S = int(sys.argv[2])
except IndexError:
    print("Manglende verdier. Oppgi:\n n: antall kast, S: Antall simuleringer")

def terning(n,S):
    import numpy as np
    ## S antall rader(eksperiment) ## n antall søyler (kast i ett eksperiment)
    utfall = np.random.random_integers(1,6,size=(S,n))

    M = 0
    for i in range(S):
        if 6 in utfall[i,:]:
            M = M + 1
    p = M/S

# Legg merke til at man her kun teller
# med de eksperimentene man får minst en
# sekser og deler på antall eksperimenter S,
# og ikke på antall kast N.

    print('P(tilnærmet)= {:.5e}'.format(p))
    eksakt = 1 - (5/6)**n
    print('P(eksakt)={:.5e}'.format(eksakt))
    return p

terning(n,S)

"""
PS: Indeksering av matriser:
matrisearray[rad,rekke(søyle)] ev. matrisearray[rad]
"""

### Kjøreeksempel
"""
>> python one6_ndice.py 2 10
P(tilnærmet)= 4.00000e-01
P(eksakt)=3.05556e-01

>> python one6_ndice.py 2 100
P(tilnærmet)= 3.50000e-01
P(eksakt)=3.05556e-01

>> python one6_ndice.py 2 10000
P(tilnærmet)= 3.00000e-01
P(eksakt)=3.05556e-01

>> python one6_ndice.py 2 1000000
P(tilnærmet)= 3.05498e-01
P(eksakt)=3.05556e-01

"""
