### Oppgave E.46 ###
## Skal simulere menneske-zombie interaksjon ###
# S: Susceptibles
# I: Infected
# Z: Zombies
# R: Removed individuals


import numpy as np
import ODESolver as ODESolver
import matplotlib.pyplot as plt

class ProblemSIZR:
    def __init__(self, sigma, beta,ds, di,rho, alfa,S0,I0,Z0,R0,T):
        """
        nu, beta: parametere i ODE-systemet
        S0,I0,R0 = init verdier
        T: Simulering for t i [0,T]
        """
        if isinstance(sigma,(float,int)): # nu tall
            self.sigma = lambda t: sigma
        elif callable(sigma):             # nu funksjon
            self.sigma = sigma

        if isinstance(beta,(float,int)): # beta tall
            self.beta = lambda t: beta
        elif callable(beta):             # beta funksjon
            self.beta = beta

        if isinstance(ds,(float,int)): # beta tall
            self.ds = lambda t: ds
        elif callable(ds):             # beta funksjon
            self.ds = ds

        if isinstance(di,(float,int)): # beta tall
            self.di = lambda t: di
        elif callable(di):             # beta funksjon
            self.di = di

        if isinstance(rho,(float,int)): # beta tall
            self.rho = lambda t: rho
        elif callable(rho):             # beta funksjon
            self.rho = rho

        if isinstance(alfa,(float,int)): # beta tall
            self.alfa = lambda t: alfa
        elif callable(alfa):             # beta funksjon
            self.alfa = alfa

        self.S0,self.I0, self.Z0, self.R0, self.T = S0,I0,Z0,R0,T

    def __call__(self,u,t):
        """ Høyresiden(e) i ODE-systemet"""
        S,I,Z,R = u
        u0 = self.sigma(t) - self.beta(t)*S*Z - self.ds(t)*S
        u1 = self.beta(t)*S*Z - self.rho(t)*I -self.di(t)*I
        u2 = self.rho(t)*I - self.alfa(t)*S*Z
        u3 = self.ds(t)*S + self.di(t)*I + self.alfa(t)*S*Z
        return [u0,u1,u2,u3]

## Skal lage en klasse for å løse problemet.
class SolveSIZR:
    def __init__(self,problem,dt):
        self.problem,self.dt = problem, dt

    def initb(self):
        return [self.problem.S0,self.problem.I0,self.problem.Z0,self.problem.R0]

    def solve(self,method = ODESolver.RungeKutta4):
        # send problemet til Rungekutta4
        self.solver = method(self.problem)

        # initialbetingelser:
        ic = self.initb()
        # Setter initialbetingelser for instansen
        self.solver.set_initial_condition(ic)
        # antall steg
        n = int(round(self.problem.T/float(self.dt)))
        # tidspunkter som en array
        t = np.linspace(0,self.problem.T,n+1)
        # Løser for valgte initialbetingelser
        self.u,self.t = self.solver.solve(t)
        return self.u, self.t

    def set_values(self):
        self.S,self.I,self.Z,self.R = \
            self.u[:,0], self.u[:,1], self.u[:,2], self.u[:,3]

    def plot(self):
        self.set_values()
        S0,I0,Z0, R0, t = self.problem.S0,self.problem.I0, self.problem.Z0,\
                            self.problem.R0,self.t
        plt.title("""
        SIZR-modell;
        $S_{0}=%.0d$,$I_{0}=%.0d$, $Z_{0}=%.0d$, $R_{0}=%.0d$
        """%(S0,I0,Z0,R0))
        plt.plot(t,self.S, label = 'S(t), Susceptibles')
        plt.plot(t,self.I, label = 'I(t), Infected')
        plt.plot(t,self.Z, label = 'Z(t), Zombies')
        plt.plot(t,self.R, label = ' R(t), Removed(Dead)')
        plt.ylabel('Individer')
        plt.xlabel('Tid(t)')
        plt.legend(loc = 'center right')
        plt.show()

if __name__ == '__main__':

    ## Lagrer først problemet med gitt variabler vha egen klasse
    beta = 0.012; alfa = 0.0016; di = 0.014; ds = 0; sigma = 2;
    rho = 1; S0,I0,Z0,R0 = [10,0,100,0]; T = 24; dt = 1

    problem = ProblemSIZR(sigma, beta,ds, di,rho, alfa,S0,I0,Z0,R0,T)

## Bruker så egen klasse til å løse problemet
    solver = SolveSIZR(problem,dt) # Lager en instanse
    u,t = solver.solve()        # Løser for instansen
    solver.plot()
