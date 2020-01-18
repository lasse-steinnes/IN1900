### Oppgave E.41 ###
# S; susceptibles
# I; infected
# R; recovered(immune)

# N = S + I + R  # N; antall individer i populasjonen

# s´(t) = -betaSI (fra omskrivning og deler på delta t)
# I´(t) = betaSI - vI
# R´(t) = vI
# 1/v: reflekterer normal varigheten på sykdommen
# Dersom ingen blir immune når friske, så +vI til s´(t) istedet for r´(t)

## Funksjon for å løse difflikningene (valgbar numerisk metode)
import numpy as np
from ODESolver import ODESolver
import matplotlib.pyplot as plt

class Forward_Euler(ODESolver):
    # Arver alt fra odesolver, utenom advance, som settes selv
    def advance(self):
        u,f,k,t = self.u, self.f, self.k, self.t
        # dt spesifisert i oppgaven
        dt = t[k+1]-t[k]
        u_new = u[k] + dt*f(u[k],t[k])
        return u_new

def f(u,t):
    # u er en liste eller array med de ukjente funksjonene SIR
    # burde her ha benyttet  S,I,R = U <- Nærmere matematisk språk
    return [-beta*u[0]*u[1],beta*u[0]*u[1] - v*u[1],v*u[1]]

## Utfør en test for å sjekke s0 + i0 + r0 = S+I+R  (en konstant(N))
        # Foreslås benytte en brukeroppgitt terminate --> true om
        # S+I+R ikke konstant

def terminate(u, t, step_no):
    ## PS: Vær litt forsiktig med toleransen.
    ## Om terminate gir true så sluttes det å lages nye punkter!!!
    eps = 1.0e-12
    return abs(sum(u[step_no])-sum(U0)) > eps


## Visualisere S,I, R i samme plot vha. en funksjon
def plot_SIR(u,t):
    plt.title(r"""
    SIR-modell;
    $S_{0}=%d$,$I_{0}=%d$, $R_{0}=%d$,
    $beta=%.2e$, $v =%.2e$ """%(U0[0],U0[1],U0[2],beta, v))
    plt.plot(t,u[:,0], label = 'S(t), susceptibles')
    plt.plot(t,u[:,1], label = 'I(t), Infected')
    plt.plot(t,u[:,2], label = ' R(t), Resistent')
    plt.ylabel('Individer')
    plt.xlabel('Tid(t)')
    plt.legend(loc = 'center right')
    plt.show()

def SIR():
    problem = f
    solver = Forward_Euler(problem) # Setter instanse
    solver.set_initial_condition(U0)
    u,t = solver.solve(time_points, terminate)
    plot_SIR(u,t)
    return u,t

if __name__ == '__main__':
    betas = [5.0e-4,1.0e-4]
    U0 = [1500, 1, 0]
    v = 0.1
    time_points = np.linspace(0,60,60*2) # må stemme overens med vektor u

    for i in range(len(betas)):
            beta = betas[i]
            SIR()

### Kommenter hvordan en forandring i beta endrer S(t).
"""
Ser at for en mindre beta, så blir ikke folk raskt nok syke fordi
smittede og friske treffes i en for lav frekvens.
Sykdommen spres derfor ikke, og kun en person blir resistent; den personen
som var syk til å begynne med.
"""
