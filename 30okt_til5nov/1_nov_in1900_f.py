#### Forelesning in1900 1.november ####
"""Spesielle metoder"""

###
# __call__  # Gjør at man kan kalle instansen som en funksjon
# __init__  # Nødvendig for å initere instansen
#__add__    #
#__str__    # Gjør at denne kalles hver gang man printer instansen.
                # f.eks. om man ønsker å skrive ut funksjonsuttrykket
                # med de gitte dataattributtene.

## For å være sikker med str kan man benytte print(str(instanse))
## Ellers holder det langt med print(instanse)


##### EKS: Ønsker å ha en klasse for å evaluere polynomer

## Kan bruke enumerate,
## eller index(coeff), men skriver
## __init__(self, coeff)
## __call__()
        # for i in range !

## Bruker polynomials2(object)   object = polynomials2,1...
## For å anvende en klasse i en klasse


## __str__
 ### Med string operasjoner!

### __add__

#### Aritmetiske operasjoner

## PS: truediv! vs div


#### __repr__ ###
# The default implementation is useless (it’s hard to think of one which wouldn’t be, but yeah)
## __repr__ goal is to be unambiguous
## __str__ goal is to be readable # Brukes for de tilfellene der du vil vise hvordan den brukes
## Container’s __str__ uses contained objects’ __repr__


# Brukes for å se hvordan klassen er bygd opp (For de ønsker å skrive koden eller kopiere den)
#   Lager en "klone"/kopi av klassen

# Kan benytte eval i kallet
"""
def __repr__(self): # Person er en klasse
    return 'Person(%r)' %self.name # %r kaller repr for name?
"""
# print(repr(p1_instanse))# Man får utskrift over hvordan dataattributtene
## ser ut i klassen Person

# kan bruke eval(repr(car)) og printe denne <-- repr(car) er et nytt objekt/klone


######### Eksempel: Klasse for imaginære tall

## __radd__ : Den reverserte addisjonen

"""
U = kompekst tall
w = 4.5 + u
skriver 4.5__add_(u) -> funker ikke. (raise ValueError)
For komplekse:
u.__radd__(4.5)
Rekkefølge har jo ikke noe å si for sum av pos tall
"""


## __rsub__: Den reverserte substraksjonen
"""
Spesialtilfelle med substraksjon. Rekkefølge spiller en rolle.
"""


##### Plenumsoppgaver #####
""" Spesiell Hello world"""
# bruker __str__, __call__
"""
__str__(self):
ret 'hallo world'

__call__(self,s):
str_ = 'hello {}!'.format(s) # eventuel ved å plusse sammen strings
ret str_                     # 'Hello,' + str(s)+'!'
"""
### Tips:
### Husk å bruke return inni metodene i klassen
### Ellers blir jo return NONE!

""" Sum.py"""
## S.term(k,x) # Kaller term argumentet for en k og en
