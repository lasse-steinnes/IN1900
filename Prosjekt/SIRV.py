#### Oppgave E.43 ###
## Skal introdusere vaksinasjon til SIR-modellen.

## Skal helst benytte subklasse, og ikke kopiere kode
## Objektorientert programmering.

## Skal modifisere slik at
# S´= -beta*S*I-pS
# S´= pS
# v0 = 0
# p = 0.1
from SIR_class import ProblemSIR as PSIR
from SIR_class import SolverSIR as SSIR
import matplotlib.pyplot as plt
import numpy as np
# Lager en klasse for problemet
                                   ##!!! Se kap 9.2.4: utvidelser
class ProblemSIRV(PSIR):     ## Has-a relationship, ikke is-a
    def __init__(self, nu, beta,p, S0,I0,RO,V0,T):    ## -> Skriver som attributter
        PSIR.__init__(self,nu, beta,S0,I0,RO,T)
        self.V0 = V0

        if isinstance(p,(float,int)): # p tall
            self.p = lambda t: p
        elif callable(p):             # p funksjon
            self.p = p

    def __call__(self,u,t):
            """ Høyresiden(e) i ODE-systemet"""
            S,I,R,V = u
            f = [-self.beta(t)*S*I-self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I, self.p(t)*S]
            return f

class SolverSIRV(SSIR):
        def initb(self):
            return [self.problem.S0,self.problem.I0,self.problem.R0, self.problem.V0]

        def set_values(self):
            self.S,self.I,self.R, self.V = self.u[:,0], self.u[:,1], self.u[:,2], self.u[:,3]

        def plot(self):
            self.set_values()
            S0,I0,R0, V0, beta,nu, t = self.problem.S0,self.problem.I0, self.problem.R0\
                        ,self.problem.V0, self.problem.beta,self.problem.nu,self.t
            plt.title("""SIR-modell;
             $S_{0}=%d$,$I_{0}=%d$, $R_{0}=%d$,$V_{0}=%d$ """%(S0,I0,R0,V0))
            plt.plot(t,self.S, label = 'S(t), susceptibles')
            plt.plot(t,self.I, label = 'I(t), Infected')
            plt.plot(t,self.R, label = ' R(t), Resistent')
            plt.plot(t,self.V, label = 'V(t), Vaccinated')
            plt.ylabel('Individer')
            plt.xlabel('Tid(t)')
            plt.legend(loc = 'center right')
            plt.show()


if __name__ == '__main__':
    beta = 0.0005
    S0,I0,R0,V0 = [1500, 1, 0,0]
    nu = 0.1
    T = 60
    p = 0.1
    dt = 0.5

# Lager først problem med den første klassen
    problem = ProblemSIRV(nu, beta,p, S0, I0, R0,V0, T)

# Lager så løsning med andre klassen
    solver = SolverSIRV(problem, dt)
    u,t = solver.solve()
    solver.plot()

    i3_max = np.max(u[:,1])
    print("""Maksimum infiserte for beta = beta(t) er I(t)={:d}
Maksimum infiserte for beta = 0.0005 er I(t)={:d}
Maksimum infiserte med vaksine, p = 0.1 er I(t)={:d}
""".format(745,897,int(i3_max)))
