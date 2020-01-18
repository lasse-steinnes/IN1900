#### Oppgave 5.31. bølgehastigheten til bølger på vannoverflaten

### Setter først opp konstantene i ligningen vår
g = 9.81 # tyngdeakselerasjonen [m/s**2]
s = 7.9e-2 #luft-vannspenning (trykk?) [N/m]
rho = 1000 #Vannets tetthet [kg/m**3]
#h = 50 # Vannets dybde[m] Skriver denne i funksjonen siden den skal fikseres
# Har da mulighet til å endre etterpå

## Bølgehastigheten c [m/s] kan uttrykkes som
# en funksjon av bølgelengden lambda.
from numpy import sqrt, tanh, pi, linspace

bølge_hast = lambda lambda_, h=50:sqrt(g*lambda_/(2*pi)*\
            (1+(s*4*pi**2/(rho*g*lambda_**2)))*tanh(2*pi*h/lambda_))

# lag et plot av c(lambda) for lambda i to intervaller

# første intervall
lambda_1 = linspace(1e-3,1e-1,1000)

# andre intervall
lambda_2 = linspace(1,2e3,1000)

# Deretter lagrer jeg bølgehastigheten som to matrisevariabler

hast_1 = bølge_hast(lambda_1)

hast_2 = bølge_hast(lambda_2)

# Så kan jeg lage de to figurene
import matplotlib.pyplot as plt

f, xarr = plt.subplots(2, figsize=(8,7.2))
xarr[0].plot(lambda_1,hast_1, label = "Bølgehastighet grafA")
xarr[0].set_title('Hastighet for små bølgelengder(λ)')


xarr[1].plot(lambda_2,hast_2, label = "Bølgehastighet grafB" )
xarr[1].set_title('Hastighet for store bølgelengder(λ)')

plt.xlabel('λ [m]')
plt.ylabel('c(λ) [m/s]')
plt.show()

"""
SPM: Har fått subplots,
men hvordan spesifiserer jeg legends for subplots?
"""
### Kjøreeksempel
"""
>>  python water_wave_velocity.py
(plot)
"""
