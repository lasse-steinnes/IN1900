#### Oppgave A.15: Finn en differens likning for å beregne cos x ####

### En tilnærming til cosinus x kan skrives slik
## for x rundt 0

# sum((-1)^k*x**2*k/(2*k!)

#### Dermed får man uttrykket ###

## S(x;j-1), dvs at n = at det skal skrives
# som sum, som er avhengig av forrige leddet

## Løsningen blir:
# k = -1*(x**(2)/(2*j*(2*j-1))

### Dvs:
# s = 1  # s0
# a_p = -x**2/2

#######  Deloppgave a og b ######

from math import pi, factorial

def cos_Taylor(x,n):
    sum_ = 1  # s0
    a_p = (-x**2/2)  # Det første leddet, a0
                    # Siden vi har med s = 1

    for n in range(1,n+1):
        sum_ = sum_ + a_p
        #print(a_p)
        k = -(x**2)/((2*(n+1))*(2*(n+1)-1))
        a_p = a_p*k

    return sum_, a_p

# a blir da a+1 og være et estimat av feilen

########  Deloppgave c #####
print( 'Deloppgave c; Utskrift og test av cos_Taylor\n')
print('cos_Taylor(2*pi, 2):')
print(cos_Taylor(2*pi, 2))
print('Får et svar som stemmer med 1 - 2pi^2/2 + 2pi^4/3:')
print(1-(2*pi)**2/2 + 2*pi**4/3)
print('Feilen skal da være omtrent -(2pi)^6/6!:')
print(-(2*pi)**6/factorial(6))
print('Ser at dette er en dårlig tilnærming langt fra punktet a = 0\n')

# print(cos_Taylor(0, 2))
### Automatisere testen i en testfunksjon:

def test_cos_Taylor():
    x = 2*pi
    n = 2

    ## Taylor og feileddet slik det burde være
    korr = 1-(x)**2/2 + x**4/24
    korr_feil = -(x**6)/factorial(6)

    # Slik det er programmert
    est = cos_Taylor(x,n)[0]
    est_feil = cos_Taylor(x,n)[1]

    tol = 1e-13
    suksess_1 = abs(korr - est) < tol
    suksess_2 = abs(korr_feil - est_feil) < tol
    msg_1 = "Den estimerte verdien stemmer ikke overens med Taylorpolynomet"
    msg_2 = "Den omtrentlige feilverdien stemmer ikke overens med neste ledd i Taylorpolynomet"

    assert suksess_1, msg_1
    assert suksess_2, msg_2

test_cos_Taylor()

## d) Nøyaktigheten øker når n øker og x minker
import numpy as np
np.vectorize(cos_Taylor)
x_arr = np.linspace(-2*pi,2*pi,200)

# plot cos_Taylor for ulike verdier av x og n
import matplotlib.pyplot as plt
print('Deloppgave d\n (plot)')

plt.plot(x_arr,np.cos(x_arr), label ='cos x')
plt.plot(x_arr,cos_Taylor(x_arr,1)[0], label=r'taylor_{1}')
plt.plot(x_arr,cos_Taylor(x_arr,2)[0],label=r'taylor_{2}')
plt.plot(x_arr,cos_Taylor(x_arr,3)[0],label=r'taylor_{3}')
plt.plot(x_arr,cos_Taylor(x_arr,4)[0],label=r'taylor_{4}')
plt.plot(x_arr,cos_Taylor(x_arr,5)[0],label=r'taylor_{5}')
plt.legend(loc ='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('cos_taylor approksimasjonen')
plt.axis([-2*pi,2*pi,-2.0,2.0])
plt.show()

#### Kjøreeksempel ###
"""
>> python cos_Taylor_series_diffeq.py
Deloppgave c; Utskrift og test av cos_Taylor

cos_Taylor(2*pi, 2):
(46.200185220489566, -85.4568172066937)
Får et svar som stemmer med 1 - 2pi^2/2 + 2pi^4/3:
46.200185220489566
Feilen skal da være omtrent -(2pi)^6/6!:
-85.45681720669371
Ser at dette er en dårlig tilnærming langt fra punktet a = 0

Deloppgave d
 (plot)
"""
