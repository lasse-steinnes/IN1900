### Forelesning informatikk 8. sept

"""Finne elementer i en liste"""
# liste[indeks1][indeks innenfor liste 2 i indeks1]

##      Husk list[i1:i2] dvs a[i] for range(i1,i2)
##      dvs. tar ikke med det siste elementet
""" PS: py prøver å være sparsom
##          Om a_list=b_list
#           vil endringen i b_list falle tilbake på
##          a_list. Løsning: Indeksering!!!!"""

""" Dagens øvelser
### 3.20. hw_functions"""

## Første funksjon
def hw1():
    return "Hello World"

print(hw1())
## Andre funksjon
def hw2():
    print ("Hello World")

## Tredje funksjon
def hw3(A,B):
    return A + B

print(hw3("Hello","Python"))

"""Oppgave 3.23 Skriv en formel inn i en funksjon"""
## egg_func.py
# rett frem

""" Oppgave 3.28, maxmin_list"""
def findMin(a):
    min_elem = a[0]
    for e in a[1:]
        if e < min_elem:
            min_elem = e
    return min_elem

    #####    else: if trenger ikke bli etterfulgt av else
# Vil teste om a har noen elementer. Om ikke kunne man returnert en feilmelding

## tilsvarende
 def findMax(a):
     max_elem = a[0]
     for e in a[1:]
         if e > max_elem:
             max_elim= e
     return max_elem

#####################################################
"""Mer om funksjoner"""

## Med defaultverdier: Vi kan endre de, eller la dem stå)
            ## Kalles keyword arguments; nøkkelargumenter

## Variable uten defaultverdier kalles posisjonsargument.

""" Funksjoner innad i funksjoner"""
### Definerer først f
## Bruker f i funksjon for deriverte f.eks. (se def)
        ## PS: For keyword arguments i dette tilfellet
        ## Rounding errors: Man må velge h=1e-6 for å komme nær deriverte
                ### spesielt pass på dette i numeriske beregninger
                ## (1) Avrundingsfeil (2) Amplifiserer ved å dele på h^2

    ## dess flere desimaltall dess mindre feil : 25 tall, 10^-23 desimalfeil

#   Rekursive funksjoner
#       nødvendig med (if) begrensning

### Doc string: dokumentere funksjoner, forklarer hva funksjonen gjør
""" def f(x):"""
#        """forklarer funksjonen"""

## Burde ha bare en return i funksjonen
## lagre (value) i et eget objekt
## else  .... return objekt

## elif : Flere if setninger
