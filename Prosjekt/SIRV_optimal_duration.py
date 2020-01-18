### Oppgave E.45 ###
## Finne en optimal vaksinasjon periode ###
# Plot maksimum antall infiserte mot antall vaksinasjonsdager, Vt

import numpy as np
from SIRV import ProblemSIRV, SolverSIRV
import matplotlib.pyplot as plt
## Vi har
## Lagrer verdiene til Imax i en array
beta = 0.0005
S0,I0,R0,V0 = [1500, 1, 0,0]
nu = 0.1
T = 60
dt = 0.5

I_maks = np.zeros(32)
V_tid = np.zeros(32)

for i in range(32):
    p = lambda t,v_tid=i: 0.1 if 6 <= t <= 6 + v_tid else 0
# Lager først problem med den første klassen
    problem = ProblemSIRV(nu, beta,p, S0, I0, R0,V0, T)

# Lager så løsning med andre klassen
    solver = SolverSIRV(problem, dt)
    u,t = solver.solve()
    i_max = np.max(u[:,1])
    I_maks[i] = i_max
    V_tid[i] = i


plt.plot(V_tid,I_maks)
plt.title(r"""Maksimum antall infiserte i perioden T $\epsilon[0,60]$
som funksjon av vaksinasjonstid""")
plt.xlabel('Antall vaksinasjonsdager')
plt.ylabel('Antall infiserte i perioden')
plt.show()

## skal finne optimal vaksinasjonperiode: Dvs når økning i en
# med vaksinering har liten effekt på maks antall infiserte
i_arr = np.zeros(32)
for i in range(1,32):
    j = I_maks[i-1] - I_maks[i]
    i_arr[i] = i
    tol = 20
    if j < tol:
        break

# Dvs at optimalt antall vaksinasjonsdager er:
print('Optimalt antall vaksinasjonsdager er {:}'.format(V_tid[int(np.max(i_arr))]))
