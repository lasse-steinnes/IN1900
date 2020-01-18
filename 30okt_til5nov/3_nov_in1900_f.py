### Forelesning in 1900###

## Går først gjennom et eksempel

## Skal bruke klassen polynomial
## Inneholder
## __call__ : evaluerer polynomet for en x
## __add__(self,other) : Returnerer self + other som polynom objekt
## self.coeff[] og other.coeff[] er to ulike lister til to ulike polyn.
## __sub__(self,other): Bruker koeffisientene i other.
##   bruker koeffisientene i klassen polynomials
## Fungerer selv om lengdene i de to polynomene
## P1 og other  er forskjellige, fordi man kun bruker den
## ene lista som er mindre enn den andre i range(len(shortest list))
        ## men denne koden fungerer kun i det ene tilfellet
        ## Vil ha en generell kode som fungere uavhenig av lengdene
        ## Bruker if test: 1 for løkke, else: 2 for løkker
        ## siste for løkke for i in range(len(self.coeff, len(other.coeff))
        ## append(-other.coeff)??


## Andre løsningsmåte: __sub__: self + neg_p
# neg_p = polynomial(neg_coeff) # bruker other.coeff og list comprehension for å endre fortegn

## Fortsetter på eksempelet:
    ## Gjør om til å gjelde dictionary.
    ## mer hendig
    ## Begynner med tom dictionary, potens - coeff par
    ## Da får vi et nytt problem å håndtere: Når den ene dictionary har
    ## en høyere grad enn den andre.

    ## Kan håndtere dette med for løkke og boolsk statement
    ## if i not in result_coeff.(result_coeff fra other)
    ## dermed else: result_coeff[i] -= other.coeff[i]


## Kan implementere klassen på akkurat samme måte, men
## endre på selve koden til å håndtere dictionary.

"""## Objekt orientert programmering (OO)"""
##
##
