### Oppgave 6.4 ###

# Lagrer først output til programmet lnsum.py i en fil

# Skriver i kommandovinduet:
""" python lnsum_utfil.py > lnsum_utskrift.txt"""

# Skriver et program som leser fila og ekstraherer
# tallene som hører til epsilon, exact feil, og n.
# lagrer tallene i tre array, bruker strengoperasjoner
import numpy as np

innfil = open('lnsum_utskrift.txt','r')
## num_l = sum(1 for linje in innfil)

linjer = []
for linje in innfil:
    ord_ = linje.split()
    linjer.append(ord_)

lin_len = len(linjer)

eps = np.zeros(lin_len)
error_ = np.zeros(lin_len)
n = np.zeros(lin_len)

for i in range(len(linjer)):
    eps[i] = float(linjer[i][1][:-1])
    error_[i] = float(linjer[i][4][:-1])
    n[i]= int(linjer[i][5][2:])

# plotter epsilon og eksakt feil versus n, i samme figur
# logaritmisk skal på y-aksen. --> semilogy fra matplotlib pyplot
import matplotlib.pyplot as plt

plt.semilogy(n,eps, '.r-',label = 'Estimert feil')
# Har med så få punkter at jeg velger å ta dem med i plot
plt.semilogy(n,error_,'.c-',label = 'Eksakt feil')
plt.title('Estimert feil vs. eksakt feil i beregningen av en sum')
plt.legend()
plt.xlabel('n´te ledd i summen')
plt.ylabel(r'$log_{10}$') # semilogy bruker base 10, log i python bruker base e
plt.show()

## Kjøreeksempel
"""
>> python read_error.py
(plot) 
"""
