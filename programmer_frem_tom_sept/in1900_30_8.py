#### Forelesning IN1900 30_8_2017

""" Først noe plenumsregning, deretter løkker og lister"""

""" Første oppgave length_conversions"""
### Litt bruk av variabler og repetisjon#
### Konvertere mellom lengdeenheter, skriver algoritme

#length in unit = length in meters/unit
# length in km = length in meters/1000
"""
inch = 2.54/100
foot = inch*12
yard = foot*3
miles = 1760*yard

length_in_meters = 640
length_in_inches = length_in_meters/inch
length_in_feet = length_in_meters/foot
length_in_yards = length_in_meters/yard
length_in_miles = length_in_meters/miles

print(length_in_inches, length_in_feet , length_in_yards, length_in_miles)

answer = '%g meters is %g inches, %g feet,\
%g yards and %g miles.' %(length_in_meters,length_in_inches, length_in_feet,
length_in_yards, length_in_miles)

print(answer)
"""
### Kjøreeksempel
"""
python in1900_30_8.py
 >> 640 meters is 25196.9 inches, 2099.74 feet,
699.913 yards and 0.397678 miles.
"""

######################################################################
""" NYTT PROBLEM: 1.12: How to cook perfect eggs """
### egg.py
from math import pi, log

### Begynner å skrive objekter
M = 67
c = 3.7
rho = 1.038
K = 5.4e-3
T0 = 4.0
Ty = 70
Tw = 100

time = (M**(2.0/3)*c*rho**(1.0/3))/(K*pi**2*(4*pi/3)) \
    *log (0.76*(T0-Tw)/(Ty-Tw))
# rho er standardnotasjon for tetthet i fysikk"""

"""print(" It takes %g minutes and %g seconds to reach %g degrees" \
    %(int(time/60),int(time%60), Ty))"""

## Kjøreeksempel
"""python in1900_30_8.py
 It takes 4 minutes and 6 seconds to reach 70 degrees"""

 #######################################################################
""" Introduksjon av løkker og lister """
### løkker brukes når man ønsker å gjenta operasjoner som ligner på hverandre.
                ### while løkke
                    ### while condition:
        #                    statement
        #                    statement               <- PS: Innrykk!

                ### for løkke
                    ### løper gjennom en liste for å gjøre noe med alle
                    ## elementer i listen
                    ## PS: Innrykk
                    ## for element in somelist:

                    ## kan alltids gjøres om til en while løkke
                    #(SE BOKA)
                    # PS: while løkker kan ikke alltid gjøres om til for!!!!



#### Boolske uttrykk : uttrykk som enten er sanne(True), eller falske(False)
    ### Bruker matematiske uttrykk
        # Eksempel for å bestemme om et utsagn er feil/riktig
        # =/ betyr falsk
    ### and (T = om begge er sanne)
    ### or (T = om en eller begge er sann)

### Lister
            # Ulikt fra tall og strenger (f.eks tekststrenger)
        # len(liste) <- ser på lengder av Lister
        # var1.append()  # legger til på slutten
            # kan også plusse sammen Lister
        # var1.insert(i,number eller objekt)
        # lete i lister: index()

""" lage tabell av celsius og farenhet"""
### Kan skrive ut tabell med copy paste, og sette inn for verdier
### Men! Enklere å bruke en liste for mange verdier

## Når programmering blir kjedelig gjøres det ofte feil!

C = -20
dC = 5

F = (9.0/5)*C + 32

while C <= 40:
    F = (9.0/5)*C + 32
    """print(C,F)"""
    print("%5d %5.1f" % (C,F))
    C = C + dC



"""Lister"""
L_= [1,2,3]
print(L_)

"""For løkke"""
"""degress = [0,10,20,40,100]
for C in degrees:
    print()"Celsius degrees", C)
    F
    print()"Faraneheit, F")
    print ("The degrees list has len(degrees)", "elements")"""
