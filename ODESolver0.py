### En generell klasse for å løse
### differensialligninger
import numpy as np

class ODESolver:
    def __init__(self,f):
        self.f = lambda u,t: np.asarray(f(u,t), float)

    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError

    def set_initial_condition(self,U0):
        if isinstance(U0, (float,int)): #skalar ODE
            self.neq = 1
            U0 = float(U0)
        else:                           # system av ODEr
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0

    def solve(self,time_points, terminate=None):
        if terminate is None:
            terminate = lambda u,t,step_no: False

        self.t = np.asarray(time_points)
        n = self.t.size
        if self.neq == 1: # Skalar ODE
            self.u = np.zeros
        else:            # system av ODEr
            self.u = np.zeros((n,self.neq))

        # Anta at self.t[0] tilhører self.U0
        self.u[0] = self.U0

        # tidsløkke
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u,self.t,self.k+1):
                break # Terminer løkke over k
        return self.u[:k+2], self.t[:k+2]

class ForwardEuler(ODESolver):
    # Arver alt fra odesolver, utenom advance, som settes selv
    def advance(self):
        u,f,k,t = self.u, self.f, self.k, self.t
        # dt spesifisert i oppgaven
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k],t[k])
        return u_new

class RungeKutta4(ODESolver):
    def advance(self):
        u,f,k,t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(u[k],t[k])
        K2 = dt*f(u[k]+0.5*K1,t[k]+dt2)
        K3 = dt*f(u[k]+0.5*K2,t[k]+dt2)
        K4 = dt*f(u[k]+K3,t[k]+dt)
        u_new =u[k] + 1/6*(K1+2*K2 + 2*K3 + K4)
        return u_new
