
### Forelesning 4 .oktober informatikk ###

# Øvelse A.4:

## N: Number of months
## L: Initial size of loan (x0)
## p: annual interest rate (in percent)# Må ha med prosenten som man skal betale tilbake hvert år
# deler på 12 for å få verdien hver måned


def loan(N,L,p)
    x = [0]*N # np.zeros(_like (alt.))
    y = [0]*n # x.copy() om man regner med array
    #(da skjer det samme som om man hadde arbeidet med lister x = x[:])
    L = float(L)
    p = float(p)
    x[0] = L ## Har fylt opp denne først

    for n in range(1,N):
        y[n] = (p/(12*100))*x[n-1] + L/N
        x[n] = x[n-1] + p/(12*100)*x[n-1] + y[n]
    return x,y
