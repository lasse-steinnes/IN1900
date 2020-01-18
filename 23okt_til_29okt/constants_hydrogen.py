### oppgave 6.2 Fysikkheftet. ###
## Skal lese physics.dat og lagre konstantene i en dictionary
## Skal kunne bruke symbolene som nøkler, som gir tilgang til
## konstantene når de tas i bruk.

#### Deloppgave a ####
innfil = open('physics_constants.dat','r')

navn = []
konstanter = []
for linje in innfil:
    ny_l = (linje[linje.find(':')+1:linje.find('[')])
    ny_l1 = ny_l.strip()
    ny_l2 = ny_l1.replace(' ',':') # litt unødvendig, men fint å repetere
    kons_ = float(ny_l2[ny_l2.find(':')+1:])
    ny_l3 = ny_l2[:ny_l2.find(':')]

    navn.append(ny_l3)
    konstanter.append(kons_)


c_dict = {navn[k]:konstanter[k] for k in range(len(navn))} # dictionary comprehension

print('Deloppgave a\n')
print(c_dict)
print('\n')

#### Deloppgave b ####
k_e = c_dict['ke']                 #columbos konstanter
m_e = c_dict['me']                 #elektronets masse
e = c_dict['e']                   #elektronladning
h = c_dict['hbar']                   #plancks reduserte konstant

en_coeff = k_e**2*m_e*e**4/(2*h**2)

print('Deloppgave b \n')
print("""Koeffisienten i utledningen av energinivået
til et hydrogenatom er {:4.2e} V.""".format(en_coeff))

"""
>> python constants_hydrogen.py
Deloppgave a

{'c': 299792458.0, 'g': 9.80665, 'G': 6.67428e-11, 'h': 6.62606896e-34, 'hbar': 1.054571628e-34, 'e': 1.602176487e-19, 'a0': 5.2917720859e-11, 'ke': 8987551787.0, 'me': 9.10938356e-31}


Deloppgave b

Koeffisienten i utledningen av energinivået
til et hydrogenatom er 2.18e-18 V.
"""
