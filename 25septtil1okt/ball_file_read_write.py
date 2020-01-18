### 4.14: Evaluer formelen for data i en fil ###

### a) Skal skrive funksjon som leser inputfile
# og returnerer v0 og en liste med t verdiene

"""Under:Test"""
    #rad = []
    #for raden in data:
    #    nesterad = raden
    #    rad = rad + raden


def ekstraher(filnavn):
    """Ekstraherer fil og omgjør den til en liste"""
    inndata = open(filnavn,'r')
    v0 = inndata.readline()
    # v0  =  float(inndata.readline().split()[1])
    v0 = float(v0[4:8])      ### Har prøvd med split og float
    inndata.readline()      ## Hopper over en linje     ## Tips: Ikke bruk list comprehension over hvert element , det blir feil!!
    data = [line.split() for line in inndata]
    minliste_ = []
    for rad in data:
        for indeks in rad:
            minliste_.append(indeks)
    inndata.close()
    flyt_liste = [float(i) for i in minliste_]
    return v0,flyt_liste

print("Deloppgave a")
print(ekstraher('ball.dat'))


## b) Skal lage en testfunksjon som
# i) lager inputfil
# inputfil kan lages med
# ii) kaller funksjon i a for å lese filen
# iii) Sjekker at retunerte data objekter er riktig

def test_ekstraher():
    "Tester om en tillaget inputfil tolkes riktig"
    testdata =  [[0.10,  0.20,   0.30],
            [0.15,  0.25,    0.35],
            [0.34,  0.22]]
    testfil = open('test_balls.txt','w')                #Lager først en inputfil
    testfil.write("v0:2.00")
    testfil.write("\n")
    testfil.write("t:")
    testfil.write("\n")
    for rad in testdata:
        for indeks in rad:
            testfil.write("%14.8f" % indeks)  # Ev. Konvertere enkeltvis til strenger
        testfil.write("\n")                              # Hva gjør denne?
    testfil.close()

    lest_tekst = ekstraher("test_balls.txt")
    dysleksi = float(2.00), [0.10,  0.20,   0.30,
        0.15,  0.25,    0.35,
        0.34,  0.22]

    import numpy as np
    lest_arrayv =  np.array(lest_tekst[0])
    dysleksi_arrayv = np.array(dysleksi[0])
    lest_arrayt = np.array(lest_tekst[1:])
    dysleksi_arrayt = np.array(dysleksi[1:])
                                                        # Gjør om til array for å teste alle verdiene samtidig
    test_arrayt  = lest_arrayt - dysleksi_arrayt
    test_arrayv = lest_arrayv - dysleksi_arrayv

    leseløve = "Programmet kjører riktig"
    if np.all(test_arrayt < 1e-14) & np.all(test_arrayv < 1e-14):      #with tol > 1e-14
        leseløve is True
    else:
        leseløve is False
    msg = "Dette programmet har dysleksi"
    assert leseløve,msg


### PS: toleranse kan være best. Legg derfor til med all() > tol. Skrive om til array
print("Deloppgave b")
test_ekstraher()

### c) Skriv en funksjon med som lager en fil med
## i) to formaterte kolonner
### ii) t i stigende rekkefølge, y på høyre side
### iii) Ps: inputfil har ikke nødvendigvis t verdiene sortert

# Algoritme:
## Begynner med en funksjon som lager t og y
## bruker numpy, ellers måtte y beregnet med en for løkke: Sparer plass
## Inne i funksjonen må det lages en ny fil

import numpy as np

def lagkol_t_y(inputfil):
    def hoyde(t):
        v0 = float(ekstraher(inputfil)[0])
        g = 9.81
        y_t = v0*t - 0.5*g*t**2
        return y_t
    t_list = (ekstraher(inputfil))[1]
    t_list = sorted(t_list)    # Bruker sorted funksjonen
    #t_array = np.array(ekstraher(inputfil)[1])
    #y_func = hoyde(t_array)
    y_list = []
    for t in range(len(t_list)):
        t_value = t_list[t]
        y = hoyde(t_value)
        y_list.append(y)

    nyfil = open('nyfil.txt','w')
    nyfil.write('-------------------\n')
    nyfil.write('  t(s)      y(m) \n')
    nyfil.write('-------------------\n')
    sammen_ = [[t,y] for t,y in zip(t_list,y_list)]
    for t,y in sammen_:
        nyfil.write('%5.4f  %10.4f \n'%(t,y))
#for t in range(0,len(t_list),1):
#    print('%5.4f %10.4f'%(t_list[t], y_list[t]))
    nyfil.write('-------------------')
    nyfil.close()
    return nyfil

print("Deloppgave c")
lagkol_t_y('ball.dat')

"""
# TEST


t_list = (ekstraher('ball.dat'))[1]
"""

# print(t_list.index(0.28075))
"""
def hoyde(t):
    v0 = float(ekstraher('ball.dat')[0])
    g = 9.81
    y_t = v0*t - 0.5*g*t**2
    return y_t


y_list = []
for t in range(len(t_list)):
    t_value = t_list[t]
    y = hoyde(t_value)
    y_list.append(y)

print(len(t_list))
print(len(y_list))


#for t in range(0,len(t_list),1):
#    print('%5.4f %10.4f'%(t_list[t], y_list[t]))

sammen_ = [[t,y] for t,y in zip(t_list,y_list)]
for t,y in sammen_:
    print('%5.4f  %10.4f'%(t,y))

"""
# print(y_list)
# print(hoyde(t_list[0]))

### Kan ikke bruke for løkke på samme måte med array

# t_array = np.array(ekstraher('ball.dat')[1])
# print(t_array)
#    y_func = hoyde(t_array)

### Kjøreeksempel
"""
>> python ball_file_read_write.py
Deloppgave a
(3.0, [0.15592, 0.28075, 0.36807889, 0.35, 0.57681501876, 0.21342619, 0.0519085, 0.042, 0.27, 0.50620017, 0.528, 0.2094294, 0.1117, 0.53012, 0.372985, 0.39325246, 0.21385894, 0.3464815, 0.57982969, 0.10262264, 0.29584013, 0.17383923])
Deloppgave b
(Ingen utskrift)
Deloppgave c
(Se nyfil)
-------------------
  t(s)      y(m)
-------------------
0.0420      0.1173
0.0519      0.1425
0.1026      0.2562
......      ......
0.5301      0.2119
0.5768      0.0985
0.5798      0.0904
-------------------
"""
