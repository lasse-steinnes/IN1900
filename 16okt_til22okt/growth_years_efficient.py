#### Oppgave A.3: Reduser minnebruken til en differenslikning. ###

## Siden Xn kun avhenger av Xn-1 trengs ikke alle n+1 xn verdier å bli lagret
## Trenger kun å lagre xn og den forrige verdien Xn-1

### Programmet skal ha følgende kriterier

#x_p0 = 100 # initialverdi
p = 5    # renten
N = 0    # Begynner på år 0

# 1) Modifisert kode skal kun inneholde to verdier, ikke array.
# 2) Unngå index_set
# 3) Bruk heltallsskritteller for n
# 4) while løkke
## Skriver sekvensen til fil slik at den kan bli visualisert

utfil = open('kontovekst.txt','w')
utfil.write('Tabell 1: Veksten av pengene i banken\
 over fire år,\n med initialverdi = 100 og rente = 0.05.\n')

utfil.write('-------------------\n')
utfil.write('{:>5} {:>7}\n'.format('N','x_n'))
utfil.write('-------------------\n')

x_p = 100
while N <= 4:
    x_n = (1 + p/100)*x_p
    utfil.write('{:>5d} {:>10.2f}\n'.format(N,x_p))
    x_p = x_n
    N += 1
utfil.write('------------------\n')
utfil.close()

## Kjøreeksempel

"""
>> python growth_years_efficient.py

Tabell 1: Veksten av pengene i banken over fire år,
 med initialverdi = 100 og rente = 0.05.
-------------------
    N     x_n
-------------------
    0     100.00
    1     105.00
    2     110.25
    3     115.76
    4     121.55
------------------
"""
