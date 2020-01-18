### Forelesning

"""
oppgave 4.4: Les og skriv flere tall fra og til fil
"""
"""
### f2c_file_farenhet.py
### Skal hente ut tallet som grader celsius
infile = open("Fdeg.dat","r")  # lagrer filobjekt, r = read

infile.readline() # hopper over de tre første
infile.readline()
infile.readline()

F.degrees = []  # tom liste
C.degrees = []  # tom liste

for line in infile:    # behandler fila som en liste
    words = line.split()
    F = float(words[-1])    # må konvertere tekststreng til flytobjekt
    F.degrees.append(F)
    C = (F-32)*(5.0/9)
    Cdegrees.append(C)

infile.close()

    ## Skal skrive dette ut som en fil med to kolonner
print(F.degrees,C.degrees)  # test


outfile = open("FCdeg.dat","w")     #w = write

## Lage for løkke med list comprehension
for F,C in zip(F.degrees, C.degrees):
    outfile.write("%5.1f %5.1f \n" %(F,C))

outfile.close()

#\n = newline. For å få tabell og ikke lang liste
"""

""" Oppgave 4.2 f2c_cml.py"""
"""
import sys

try:
    F = float(sys.argv[1])
except:
    print("Command line argument missing")
    exit()

C = 5.0/9*(F-32)
print("Temperature(Celsius): %g" %C)

"""
""" Ny oppgave : objects"""
"""
var = input("Give some input:")
print(type(var),var)

x = eval(var)
print(type(x), x)
"""

### Visualisere grafene ######################################

# Skal plotte funksjoner som er ukjente og kjente

### først for kjente
## Lag først en nøstet liste med en funksjons for f, og list comprehension
## etterfulgt av zip()

""" import numpy as np. """
""" np.array(listx, listy)""" # <- indirekte array

"""lage array direkte"""
"""
n = 5
x = linspace(0,1,n) # n punkter i intervallet
y = np.zeros(n)
for i in range(n):
    y[i] = f(x[i])
"""
