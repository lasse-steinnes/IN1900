### Oppgave 8.2 ###
## Hva er sannsynligheten for å få et nummer mellom 0.5-0.6?
## Uniform distribusjon, intervall [0,1)

## Spesifikk løsningsmetode:
## Bruke standard random
## Trekke N tall
## Tell opp antall M i intervallet

def rand_0506(N):
    import random
    M = 0
    for i in range(N):
        utfall = random.uniform(0,1)
        if 0.5 <= utfall <= 0.6:
            M = M + 1
    return float(M)/N


## Beregn M/N
## N = 10^i, i:1,2,3,6.
N0 = 10**1
N1 = 10**2
N2 = 10**3
N3 = 10**6

print(rand_0506(N0))
print(rand_0506(N1))
print(rand_0506(N2))
print(rand_0506(N3))

### Kjøreeksempel ####
"""
>> python compute_prob.py
0.1
0.08
0.089
0.099658
"""
