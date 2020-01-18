#### Forelesning 13 september.

## repetisjon kap 3.

""" testfunksjon"""
# unit testing: Tester for spesialtilfeller, dvs ingen argumenter
# som skal inn.
##  standardisert oppsett
##  assert setning
##      assert setningen kan være inne i en for løkke
##      spesifikt dersom flere verdier skal testes!!!!!
## Blir bare fortalt om den ikke fungerer: Silent run

# test framework

"""Kap 4: Avrundingsfeil og retting"""
### Program 1
from math import sqrt

for n in range(1,60):
        r = 2.0
        for i in range(n):
            r = sqrt(r)
        for i in range(n):
            r = r**2
        print("%d times sqrt and **2: %.16f" % (n,r))
"""
### Kommentar: Oscillerer litt, men etter mange n blir feilen større.
## Alle verdiene burde i utgangspunktet bli lik 2,
## men pga avrunding blir det ikke slik
## Program 2 bygger videre på denne: Fikserer n og r og printer ut
## over to for løkker. For n = 52: Datamaskiner tolker dette til slutt som 1
###  fordi oppløsningen ikke er stor nok(tar ikke vare på nok desimaler)

##       Kan løses med diverse programpakker

### Nytt program (2.20)
### Epsilon halveres, viser hvilke desimalnøyaktighet man har..
## Beregner maskinfeilen.
"""
### 2.21
a = 1/947.0*947
b = 1
if a != b:
    print("Wrong Result")

# Poeng: Ikke sammenlign flyt objekter.
# bruker heller
"""abs(a-b) < tol # hvor tol er akseptabel feilmargin"""


########## Nytt tema #############
"""Hente input data"""
# 1) program
# 2) Kommandolinje
# 3) Mens programmet kjører: Brukerinteraksjon (user input)

### Eksempel: print all primes up to n


#Nytt tema
""" Fillesning"""

### Eksempel: lese filer
### Skriv ned strategi basert på observasjon
##      Tittel leses for seg(annet format)(read not save)
##      Bestemmer seg for en linje om gangen.
##      split
##      de to ordene kan lagres separat
##      Spesielle rader burde leses separat!!!!
##      Kan bruke for løkker etter for å splitte opp
##          og gjøre noe med linejene.
## '    Lagre variable i lister f.eks.(begynn med tomme). Lukk fil
##      print resultatet

##      Del opp i overkommelige delkoder

##      Tester vurderingsevne!!!! Tenk sjøl.

"""Få brukeren til å lage egne uttrykk som kan
evalueres i programmet"""






##
