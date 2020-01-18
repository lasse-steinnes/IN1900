###  6.4, 6.2 (FY)

## 6.3 Skal forbedre density.py fra seksjon 6.1.5 i boka.
## Skal bruke string(streng) operasjoner, for å gjøre
# koden kortere, gjøre den mer elegant og generell.

#  a) Lag en python funksjon som lar substansen inneholde
#  alle ordene i split utenom den siste.

def read_densities_vol2(filnavn):
    innfil = open(filnavn,'r')
    th_dict = {} # tom dictionary (ordbok)
    for line in innfil:
        ord_ = line.split()
        th_v = float(ord_[-1])

# Bruk join metoden for å i strengobjekter til å komibinerer
# ordene til navnet på substansen(forbindelsen)
        materie = ' '.join(ord_[:-1]) # legger sammen ordene i linja frem til th-verdien.
        th_dict[materie] = th_v # legger til nøkkel-verdi-par til oppslagsverket.
    innfil.close()
    return th_dict

tetthet = read_densities_vol2('densities.txt') # Dataene blir lagret i en ordbok.

print('Deloppgave a')
print(tetthet)

# b) Observere at alle tetthetsverdiene i densitites.dat starter i samme kolonne
# Lag alternativ kode som bruker substring indexing til å dele en linje inn i to deler
# substans og tetthet.

# skal bruke .strip og substring indexing. (Kan ev bruke .find)

def read_densities_vol3(filnavn):
    innfil = open(filnavn,'r')
    th_dict = {}
    for line in innfil:
        materie = line[0:16].rstrip()  # Indeksering begynner alltid på 0. En enkel felle å gå i.
        th_v = float(line[16:])
        th_dict[materie] = th_v
    innfil.close()
    return th_dict

tetthet_2 = read_densities_vol3('densities.txt')

print('Deloppgave b')
print(tetthet_2)

### Kjøreeksempel
"""
>> python density_improved.py

Deloppgave a
{'air': 0.0012, [...] 'proton': 230000000000000.0}
Deloppgave b
{'air': 0.0012, [...] 'proton': 230000000000000.0}
"""
