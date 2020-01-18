# Halveringstid er den tiden det tar for
# et radioaktivt stoff å få halvert sin masse

# Halveringstiden til C-11 kan beskrives slik:
# a)

from math import exp, log

N0 = 4.5        # masse [kg]
tau_ = 1760     #tidskonstanten til C-11,
#                gjennomsnittstid for et atoms nedbrytning
t = 10*60          # tid [sek]

N_t = N0*exp(-t/tau_)

print("a)")
print ("N_t kan utledes fra en enkel funksjon. For \
N0=%.2f og t=%.2f, er restmassen %.2f kg." %(N0,t,N_t))

# b) Forholdet mellom halveringstid og tidskonstanten kan beskrives slik:

def halflifeC_11(t_half,N_0, t):
    tau_2 = float(t_half)/log(2) # utregning av tidskonstanten
    N_t2 = N_0*exp(-t/tau_2)
    return(N_t2)

t_half = 1220      # sek
N_0 = 4.5
t2 = 10*60
remains = halflifeC_11(t_half, N_0, t2)

print ("b)")
print("N_t kan utledes indirekte, ved å uttrykke tidskonstanten \
som funksjon av Halveringstiden. For N0=%.2f kg og t=%.2f sek, \
er den gjenværende massen lik %.2f kg." %(N_0,t2,remains))


## Kjøreeksempel
"""
>> python half_life.py
a)
N_t kan utledes fra en enkel funksjon. For N0=4.50 og t=600.00,
er restmassen 3.20 kg.
b)
N_t kan utledes indirekte, ved å uttrykke tidskonstanten som
funksjon av Halveringstiden. For N0=4.50 kg og t=600.00 sek,
 er den gjenværende massen lik 3.20 kg.
"""
