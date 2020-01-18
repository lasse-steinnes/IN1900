# Forelesning, dictorionaries and string


"""##### Oppslagsverk(?) og strenger ####"""

"""PS: OBJEKTORIENTERING!!!!"""

###### Plenumsoppgaver #########
"""5.16: Read_density_data"""

## Alltid sjekke tekstfilen for å se format før man bruker read og write

# plan: Tenke før man begynner å programmere. (LOLs)
# skaff tekstfilene
# bruker sysargv
# Bruker split, deler inn i ord, skal hente temperatur og tetthet
# Skill ut linjer som er kommentarer og blanke
            # Kan bruke split(), eller fremskaffe ord i liste ved indeksering

#(PS: Usyblige kontrolltegn, som f.eks. \n)

#### Svar: Leser fila. Lager en variabel:
"""
    for line in infile:
        words = line.split()
        if len(words) >= 2 and words[0] != '#':
            temp.append(float(words[0]))
            den.append(float(words[1]))
"""
#############
""" 5.18 Fit a polynomial to data points """
## Bruke numpy til å tilnærme en funksjon til grafen av dataene sine
###  Man skal plotte rådataene, sammen men en tilpasset funksjon
### Det beste er å tegne de ulike kurvene med ulike punkter og farger


"""
Oppgave a)
    def fit(x,y,deg):
        plot data
        x_array   # bruker linspace(xmin,xmax,n), vil ha jevne punkter
        for d in deg:
            coef med polyfit
            polynom med poly1d
            y_array
            plot polynom med x_array, y_array
        show
"""

# Skal kjøre samme operasjon på samme type filer
"""
Oppgave b)
fnavn = ['filnavn1', 'filnavn2']

for i in range(len(fnavn));
subplot(1,2,i+1)

# Plotter tetthet luft, og tetthet vann, som
funksjon av temperatur, med lineær og kvadratisk tilpasning

Tilpasning -> mønstre -> testbare hypoteser.
Kan overføres til nye tilfeller.
"""

### Del 2 se notater
