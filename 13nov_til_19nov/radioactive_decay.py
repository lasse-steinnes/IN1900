## Oppgave E.16 ##
# Skal beregne en ODE av første orden
# u' = -a*u
# u(0) = 1
# Kan bruke ODESolver

#####  Deloppgave a ####
class Decay:
    def __init__(self,a):
        self.a = a

    def __call__(self, u,t): # f(u,t)
        a = self.a
        return -a*u

##### Deloppgave b; initialiserer instansen
from math import log
a = log(2)/5600 # 1/y
d1 = Decay(a)

#### Del oppgave c. Skal løse differensialligningen numerisk ###
T = 20000 # år total
n = 500   # år tidssteg

# Bruker ForwardEuler som funksjon, et annet alterativ ville vært
# å bruke ODEsolver med ForwardEuler som subklasse.
def Forward_Euler(f,U0,T,n):
    """Løs u' = f(u,t), u(0)=u0, med n steg til t=T"""
    import numpy as np
    t = np.zeros(n+1) # n+1 punkter
    u = np.zeros(n+1)  # u[k] er løsningen ved t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        u[k+1] = u[k] + dt*f(u[k],t[k])
        t[k+1] = t[k] + dt
    return u, t

# Vi har d1, som er problemet spesifikt for C-14
# og u(0)=1
u0 = 1
u,t = Forward_Euler(d1,u0,T,n)

## Skal så plotte løsningen, gjør det sammen med eksaktløsningen
def g(a,t):
    import numpy as np
    return np.exp(-a*t)

import numpy as np
t1 = np.linspace(0,T,n)
eksakt = g(a,t1)

import matplotlib.pyplot as plt
plt.plot(t1, eksakt, label =  r'Eksakt')
plt.plot(t,u, label = r'Forward_Euler_{n=500}')
plt.title(r'Forward euler for $u\prime = -au$')
plt.xlabel('t')
plt.ylabel('Mengde c-14')
plt.legend()
plt.show()

## utskrift, approks og eksakt
print('\nFor tilfellet u´ = -au, u(0)=1, T = 20000, så...')
print('Euler forward:{:6e}'.format(u[-1]))
eksakt2 = g(a,T)
print('Eksakt løsning:{:6e}'.format(eksakt2))
print('Feilverdi:{:.3e}'.format(abs(eksakt2-u[-1])))

### Kjøreeksempel
"""
>> python radioactive_decay.py
(Figur)

For tilfellet u´ = -au, u(0)=1, T = 20000, så...
Euler forward:8.360314e-02
Eksakt løsning:8.411876e-02
Feilverdi:5.156e-04
"""
