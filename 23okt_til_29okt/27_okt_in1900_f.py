### Forelesning in1900

### MER OM KLASSER ###

# Klasser er ikke nødvendigvis viktig i forhold til mye annet "pensum."
# Imidlertid er de nyttige om man lager store programsystemer.
# For senere bruk er de derfor svært nyttige.

### Object orientert programmering (OOP)
# Utviklet i Oslo (simula)

### Python har lister og dictionaries innebygget
## #Dermed er det mindre viktig å lage sine egne Klasser
# i dette tilfellet.

# Fordelen med klasser er at de pakker data og funksjoner
# som naturlig hører sammen.

## Alternativ til å lage en global funksjon.

#Klasser: Dermed fungerer funksjonen
# for visse type data, og er spesiallaget for denne typen data.


########## Bruk av klasser ##########
## Skiller seg fra vanlig funksjon ved at man setter
## et tilfelle med fastsatte argumenter(fra funksjonen init - konstruktør),
# som sendes med som
## parametere i neste funksjon i klassen, slik at denne kun avhenger av en variabel.
## Dermed kan man benytte funksjoner i klasser til generelle funksjoner laget av andre,
## som kun kan operere på funksjoner av en variabel.


### Self

# lager et tilfelle med self.
# objektet selv.

############ Eksempler ###########
############## Bankkonto ##########
### Kunne lett laget dette som en dictionary
## Ved å først definere en funksjon som lager en dictionary
## Videre, lager kode for deposit, withdraw, print.
## MEN: ikke like bra spesifisitet som en klasse!
## Funker, men passer til mindre programsystemer.

# UML: Unified modified language

# Korrekt bruk:
# SKal ikke endre attributter i ett tilfelle direkte, utenfor klassen.
# skal kun forandres gjenneom funksjonene.
# Bruk underscore slik at det blir tydelig når konvensjonen brytes.
# self._name = name
# Riktig: a1.get_balance
# feil: a1.balance # for tilfelle a1 # Men, ok i testfunksjon

# Grunner til dette:
# Om man vil endre funksjoner i klassen, eller intern datastruktur.
# Om man forandrer inni klassen --> Trenger kun å endre en gang slik at
# dette gjelder for alle funksjonene i klassen.

# Slipper å endre for alle funksjonene.

########### Linear/Quadratic ################
# Fra koeffisienter som en attributt hver til
# en liste som atrributt (må bruke indeksering videre)

# underscore konvensjon: F.eks. get_balance () som funksjon for å skaffe balanseverdi
# Kan da kalle på denne for å finne attributter til et tilfelle.


# KLASSER tilbyr ekstra organisering: I store programmer kan dette være forskjellen
# som gjør om programmet fungerer eller ikke.

# ####### Legge til data attributt til en klasse ########

# utvidelse av klassen med antall uttak.
 ### Setter i konstruktøren:
 # self.transactions = 1
 # oppdaterer med += 1 for deposit og withdraw


 # ########## Testfunksjon: ############
 # Lage en egen testfunksjon for å teste klassen

## == Husk at du må ha to likhetstegn dersom du skal ha den matematiske betydningen av
# =

# = Tester om to objekter er like. ikke matematisk likhet

############## Legg til funksjonalitet til en klasse #########
# Introdusere en liste, transactions, der hvert element er en dictionary;
# med tid: ctime() og transactionsantall: initial amount (nøkler:tid, transactions).
## Trenger ikke balance, kan heller beregne dette fra listen "transactions."
## Bruker da en lokal variabel balance(istedenfor self.balance) i metoden get_balance(Bruker)
# for løkke.

# I dump. Skriver self.get_balance()

# datetime, time (from time import ctime)

# I deposit, withdraw. Oppdater verdiene som tilhører nøklene i lista .

# Append til den gamle lista.

# print transactions
# Gjøres med en for løkke.

# Når man kaller print transactions ; ingen argumenter (men self i metoden i klassen)

# PS: Husk å benytte self.transactions. transactions alene er ikke et objekt.


### Poeng: Kan forandre intern datastruktur uten å forandrer
# hvordan klassen fungerer.
