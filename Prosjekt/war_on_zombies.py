### Oppgave E.48 ###
### Skal ha motangrep ved ulike tidspunkter
# Øker alfa med w(t)
### Angrep ved m+1 tidspunkter, m tidssteg

## Omega stor rundt disse t verdiene
## Liten ellers
import numpy as np
from SIZR import ProblemSIZR as PSIZR, SolveSIZR as SSIZR
import matplotlib.pyplot as plt

def war(t):
    sum_o = 0
    for T in T_arr:
        o = np.exp(-1/2*((t-T)/delta)**2)
        sum_o = sum_o + o
    omega = a*sum_o
    war = alfa + omega    ## alfa pluss omega eller bare omega
    return war

di = 0.0; ds = 0; sigma = 0; rho = 1; beta = 0.03; alfa = 0.2*beta;
a = 50*alfa; T_arr = np.array([5,10,18]); delta = 0.5; S0,I0,Z0,R0 = [50,0,3,0];
T = 20; dt = 1; war = war

t = np.linspace(0,20,40)
plt.plot(t,war(t))
plt.title('Oversikt over alfa')
plt.show()

problem = PSIZR(sigma, beta,ds, di,rho, war,S0,I0,Z0,R0,T)

## Bruker så egen klasse til å løse problemet
solver = SSIZR(problem,dt) # Lager en instanse
u,t = solver.solve()        # Løser for instansen
solver.plot()

### Dette er en simulering, derfor går zombiene i minus,
## selv om dette ikke kan skje i virkeligheten.
## Menneskene vinner så vidt.
