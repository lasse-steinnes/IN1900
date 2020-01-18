### Oppgave E.44 ###
### Skal introdusere en vaksinasjonskampanje i SIR modellen ###
## Har allerede skrevet en utvidelse i koden til å takle en varierende p

# Skal ha p = 0.1 if 6 <= t <= 15, else 0

# Plot
from SIRV import ProblemSIRV, SolverSIRV
import matplotlib.pyplot as plt

beta = 0.0005
S0,I0,R0,V0 = [1500, 1, 0,0]
nu = 0.1
T = 60
p = lambda t: 0.1 if 6 <=t <=15 else 0
dt = 0.5

# Lager først problem med den første klassen
problem = ProblemSIRV(nu, beta,p, S0, I0, R0,V0, T)

# Lager så løsning med andre klassen
solver = SolverSIRV(problem, dt)
u,t = solver.solve()
solver.plot()

print(max(u[:,1]))

## Dette funka bra.
