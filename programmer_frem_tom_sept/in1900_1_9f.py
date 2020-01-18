#### Forelesning 1.9

### last ned kildekoden til boka
###     Download tarfile
###     PS: Py 2.

### Skal gå gjennom en del oppgaver

"""2.1 f2c_table_while"""
### Skrive om fra farenheit til grader c
"""print("--------------------")
#C = -20
#dC = 5
F = 0
dF = 10

while F <= 100:
    C = (F-32)*5/9.0
#    F = (9.0/5)*C + 32
    print("%5d %5.2f" %(F,C))
    F = F + dF
#   C = C + dC
print("--------------------")"""

# ny oppgave
"""2.4 odd.py"""
# oddetall, fra 1 til n.
# oddetall kan beskrives som 2n-1

"""n = 11
odd = 1
print (odd)
a = n-1
while  odd < a:
    odd = odd + 2
    print (odd)"""

## ny oppgave
"""2.8 Make a table of values from a formula"""
# bruk n+1 uniformt spredt t verdier, t e [0,2v0/g]
n = 5
v0 = 5.0
g = 9.81

t_stop = 2*v0/g
dt = t_stop/n              #### n er antall steg før vi når t_stop

print("-------------------------")
print("for loop")  ## hjelpeprint
for i in range(n+1):      #### range tar bare heltall
    t = i*dt      # der i er tallet med index [i]. Fint når dt ikke er heltall
    y = v0*t - (1/2)*g*t**2
    print(t,y)
# a: for loop (se over)

# b: while loop (se under)
print("--------------------------")# kunne skrevet noe som ligner mer på forløkke
print("while loop")
t = 0 ## initialiser t verdi
eps = 1e-10
while t < t_stop + eps:      ### tryggere slik enn t <= t
    y = v0*t - (1/2)*g*t**2
    print(t,y)
    t = t + dt       ## steps må alltid være med i while løkken


### Videre på Forelesning

""""printe en liste"""
##  I) starte med tom liste
### II) for løkke
### III) namelist.append(intobjekt)

"""summen av en rekke"""

"""Legge til et tall til hver objekt i indeks til liste"""

"""list comprehension"""
###omvendt for løkke

"""zip"""

"""Nøstede lister"""
## nested lists er en type liste bestående av to eller flere lister
### listene kan da indekseres (ps husk at indeks begynner på 0, dvs
# 0 er første element)

## rekursjon: funksjoner kaller på seg selv

###Hente elementer i liste
###     Liste[i1:i2]

"""Tupler"""
# lister som ikke kan endres t = ()
