#### Oppgave E.47 ###
## Har laget kode som kan ta varierende paramatere
## Skal simulere de tre stadiene
## Lage kode for hver

from SIZR import ProblemSIZR, SolveSIZR

# parameterne kan skriver som funksjoner

S0,I0,Z0,R0 = [60,0,1,0]; T = 4+24+5; dt = 1

def beta(t):
    if t <= 4:
        beta = 0.03
    elif t <= 28:
        beta = 0.0012
    else:
        beta = 0
    return beta

def alfa(t):
    if t <= 4:
        alfa = 0
    elif t <= 28:
        alfa = 0.0016
    else:
        alfa = 0.006
    return alfa

def di(t):
    if t <= 4:
        di = 0
    elif t <= 28:
        di = 0.0014
    else:
        di = 0.000
    return di

def ds(t):
    if t <= 4:
        ds = 0
    elif t <= 28:
        ds = 0.0
    else:
        ds = 0.0067
    return ds

def sigma(t):
    if t <= 4:
        sigma = 20
    elif t <= 28:
        sigma = 2
    else:
        sigma = 0.0
    return sigma

def rho(t):
    if t <= 4:
        rho = 0
    elif t <= 28:
        rho = 1
    else:
        rho = 1
    return rho

## Lagrer først problemet med gitt variabler vha egen klasse
problem = ProblemSIZR(sigma, beta,ds, di,rho, alfa,S0,I0,Z0,R0,T)

## Bruker så egen klasse til å løse problemet
solver = SolveSIZR(problem,dt) # Lager en instanse
u,t = solver.solve()        # Løser for instansen
solver.plot()
