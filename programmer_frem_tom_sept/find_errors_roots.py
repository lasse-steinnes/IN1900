a = 2; b = 1; c = 2
from cmath import sqrt
q = b*b - 4*a*c
q_sr = sqrt(q)
x1 = (-b + q_sr)/2*a
x2 = (-b - q_sr)/2*a

print (x1,x2)

## For å løse denne må man bruke komplekse tall ###
## Kvadratroten er negativ, og dette gjelder ikke
## på tallinjen av reelle tall

## I python skrives det imaginære tallet i,
## som j.

## Beregning med komplekse tall kan importeres slik:
## from scipy import *
## from cmat import sqrt eller *
## from scitools.std import *
## from numpy.lib.scimath import *
