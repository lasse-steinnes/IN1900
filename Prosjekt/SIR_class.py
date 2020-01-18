### Oppgave E.42 ###

## Skal lage en egen klasse for problemet, som kan ta
## beta og v(nu) som variabler, og lagre kvalitative
# parametere for problemet
import numpy as np
import ODESolver as ODESolver
import matplotlib.pyplot as plt

class ProblemSIR:
    def __init__(self, nu, beta,S0,I0,RO,T):
        """
        nu, beta: parametere i ODE-systemet
        S0,I0,R0 = init verdier
        T: Simulering for t i [0,T]
        """
        if isinstance(nu,(float,int)): # nu tall
            self.nu = lambda t: nu
        elif callable(nu):             # nu funksjon
            self.nu = nu

        if isinstance(beta,(float,int)): # beta tall
            self.beta = lambda t: beta
        elif callable(beta):             # beta funksjon
            self.beta = beta

        self.S0,self.I0, self.R0, self.T = S0,I0,RO,T

    def __call__(self,u,t):
        """ Høyresiden(e) i ODE-systemet"""
        S,I,R = u
        return [-self.beta(t)*S*I, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I]
"""
        if callable(beta) and callable(nu):
            f = [-beta(t)*S*I, beta(t)*S*I - nu(t)*I, nu(t)*I]
        elif callable(nu):
            f = [-beta*S*I, beta*S*I - nu(t)*I, nu(t)*I]
        elif callable(beta):
            f = [-beta(t)*S*I, beta(t)*S*I - nu*I, nu*I]
        else:
            f = [-beta*S*I, beta*S*I - nu*I, nu*I]
        return f
Om jeg hadde brukt self, så hadde jeg sluppet dette. Se over.
"""

## Skal lage en klasse for å løse problemet.
class SolverSIR:
    def __init__(self,problem,dt):
        self.problem,self.dt = problem, dt

    def initb(self):
        return [self.problem.S0,self.problem.I0,self.problem.R0]

    def solve(self,method = ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        # initialbetingelser:
        ic = self.initb()
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0,self.problem.T,n+1)
        self.u,self.t = self.solver.solve(t)
        return self.u, self.t

    def set_values(self):
        self.S,self.I,self.R = self.u[:,0], self.u[:,1], self.u[:,2]

    def plot(self):
        self.set_values()
        S0,I0,RO,beta,nu, t = self.problem.S0,self.problem.I0, self.problem.R0,\
                            self.problem.beta,self.problem.nu,self.t
        plt.title("""
        SIR-modell;
        $S_{0}=%.0d$,$I_{0}=%.0d$, $R_{0}=%.0d$
        """%(S0,I0,R0))
        plt.plot(t,self.S, label = 'S(t), susceptibles')
        plt.plot(t,self.I, label = 'I(t), Infected')
        plt.plot(t,self.R, label = ' R(t), Resistent')
        plt.ylabel('Individer')
        plt.xlabel('Tid(t)')
        plt.legend(loc = 'center right')
        plt.show()

if __name__ == '__main__':
# beta skal være varierende
    #beta = 0.0005
    beta = lambda t: 0.0005 if t <= 12 else 0.0001
    S0,I0,R0 = [1500, 1, 0]
    nu = 0.1
    T = 60
    dt = 0.5

# Lager først problem med den første klassen
    problem = ProblemSIR(nu, beta, S0, I0, R0, T)

# Lager så løsning med andre klassen
    solver = SolverSIR(problem, dt)
    u,t = solver.solve()
    solver.plot()

    i_max = np.max(u[:,1])


# Lager først problem med den første klassen
    beta = 0.0005
    problem = ProblemSIR(nu, beta, S0, I0, R0, T)

# Lager så løsning med andre klassen
    solver = SolverSIR(problem, dt)
    u,t = solver.solve()
    solver.plot()
    i2_max = np.max(u[:,1])

    print("""Maksimum infiserte for beta = beta(t) er I(t)={:d}
Maksimum infiserte for beta = 0.0005 er I(t)={:d}
    """.format(int(i_max),int(i2_max)))
