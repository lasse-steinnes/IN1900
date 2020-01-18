### Oppgave E.30 ###

# bruker Rungekutta slik den er oppgitt i formel
# E.38
## dt = t[k+1]-t[k] dersom datapunkter

# x' = x(1-x)
# x(0) = 1/10

# Bruk en enkel funksjon slik som for Forward Eulers metode

def Rungekutta_2(f,U0,T,n):
    """Løs u' = f(u,t), u(0)=u0, med n steg til t=T"""
    import numpy as np
    t = np.zeros(n+1) # n+1 punkter
    u = np.zeros(n+1)  # u[k] er løsningen ved t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)

    for k in range(n):
        k1 = dt*f(u[k],t[k])
        k2 = dt*f(u[k]+(1/2)*k1,t[k]+1/2*dt)
        u[k+1] = u[k] + k2
        t[k+1] = t[k] + dt
    return u, t

# Konstruere testproblem der man kjenner den analytiske løsnigen
# x' = x(1-x)
# x(0) = 1/10
def g(t):  # eksaktløsning
    from numpy import exp
    return exp(t)/(9 + exp(t))

def f(u,t):  # differensialproblem
    return u*(1-u)

rung1 = Rungekutta_2(f,1/10,10,5)
rung2 = Rungekutta_2(f,1/10,10,10)
rung3 = Rungekutta_2(f,1/10,10,15)
rung4 = Rungekutta_2(f,1/10,10,20)
import numpy as np
t1 = np.linspace(0,10,1000)
eksakt = g(t1)
# Plot differansen mellom den numeriske og analytiske løsningen.
import matplotlib.pyplot as plt
plt.figure(figsize=[10,7])
plt.plot(t1,eksakt,'m-', label = r'F = $\frac{e^(t)}{9 + e^t}$')
plt.plot(rung1[1], rung1[0],'g.-', label = r'$Rungekutta2_{n=3}$')
plt.plot(rung2[1], rung2[0],'c.-', label = r'$Rungekutta2_{n=6}$')
plt.plot(rung3[1], rung3[0], '.-',label = r'$Rungekutta2_{n=8}$')
plt.plot(rung3[1], rung3[0], '.-',label = r'$Rungekutta2_{n=10}$')
plt.legend()
plt.title(r'2-ordens RungeKutta for $x\prime = x(1-x)$, F = $\frac{e^(t)}{9 + e^t}$')
plt.show()
# Demonstere at den numeriske løsningen nærmer seg den eksakte løsningen

# når tidssteget (delta t) reduseres.

### Kjøreeksempel
"""
>> python RungeKutta2_func.py
(Figur)
"""
