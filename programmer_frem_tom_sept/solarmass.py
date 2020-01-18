# Solar mass. Oppgave 1.2

from math import e, pi

pi_ = 4*(pi**2)
Aum = (1.58*(10**-5))
lys = 9.5*10**12
aums = (Aum*lys*1000)# lysår i meter per år
G = 6.674*(10**-11)  # gravitasjonskonstant

### Konverterer år til sekunder
days = 365.25
hours = days*24
minutes = hours*60
seconds = minutes*60

Solarmass = ((pi_)*(aums**3))/((G)*(seconds**2))

print("""Solarmassen er %.3g kg.
Denne oppgaven brukte jeg unødvendig lang tid på.""" %Solarmass)
