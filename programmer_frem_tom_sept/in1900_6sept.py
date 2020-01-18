### Forelesning 6.september

# Notater
""" Lister"""

#  listenivå
#    Ofte feilkilde.
#    Liste av en liste
#    Smart å bruke ipython eller visual simulator

#   En-nivålister: primtall
#   tonivå: sjakkbrett (tabell, matrise 2D)
#   Blandet nivå: Dersom man har en undersøkelse
#   med flere replikater(ulike antall måleverdier)

### Oppgave  2.7: coor.py
## Vil lage n+1 oppdelte x koordinater i [a,b],
## definere startparametre
a = 0.0
b = 1.0
n = 20

 # a)

x = []   # begynner med tom  liste
h = float(b-a)/n

for i in range(n+1):
    x.append(a + i*h)

## b) Med list comprehension: KORTERE!!

x = [a + i*h for i in range(n+1)]

#### Oppgave 2.14 inverseSine
## Google

## 2.15: Indeksering av nøstede lister
# a) Trekke ut elementer med Indeksering
# q[indeks til liste][indeks til element i liste]

# ## b) Nøstede for løkker.




################# Del 2 ###############
""" Funksjoner og forgreininger """

# Matematiske funksjoner
# Ikke-matematiske funksjoner
# Metoder (dvs non-callable kommandoer)

# F.eks. sin x : bruker den geometriske rekken, og andre "omveier" for å
# oppnå den eksakte sin verdien

## Funksjoner er "callable"
##  Kan angi en verdi til en variabel, få et svar
##  Kjører programkode indirekte

#### En funksjon kan ha ingen variabler (
#              dvs. variabelen er satt på forhånd og oppdateres automatisk
#               fordi den avhenger av funksjoner i funksjonen)

# med variabler

### Globale og lokale variabler
#        De lokale variablene eksisterer kun inne i funksjonen
#           De globale variablene eksisterer kun utenfor funksjonen
#        gitt at den er definert på nytt inne i funksjonen.
#         Om en variabel er gitt globalt kan den brukes inne i funksjonen.
#          Praktisk å ha konstanter globale



### funksjonsuttrykk kan brukes til å definere sin og cos osv
## ved å benytte geometrisk rekke, (for eller while løkke i funksjonen)
##  feilestimat og faktisk feil
