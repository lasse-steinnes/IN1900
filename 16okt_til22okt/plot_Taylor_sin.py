###### 5.32 Plot Taylor polynom approksimasjonen til sin x ###

##### Oppgave a #####
# Skal beregne S(x;n) rett frem for
# hvert ledd som det står i formelen

import math as math
import numpy as np

def sin_aprox(x,n):
    sum_ledd = 0
    for j in range(n+1):
        ledd_j = ((-1)**j)*(x**(2*j+1))/np.math.factorial(2*j+1)
        sum_ledd = sum_ledd + ledd_j
    return sum_ledd


##### Oppgave b #####
# Skal plotte sin x på [0,4*pi], sammen med approx
# S(x:1), S(x;2); S(x;3, S(x;6), S(x;12)

# Lager først approksimasjonen for x mellom 0 og 4*pi.
x_arr = np.linspace(0,4*np.pi,1000)
# print(x_arr)

# Kan deretter kalle funksjonen,
#siden np er benyttet i funksjonen trengs ikke å vektorisere
import matplotlib.pyplot as plt

plt.plot(x_arr, np.sin(x_arr), label = "f(x) = sin(x)")
plt.plot(x_arr, sin_aprox(x_arr,1), label = r'$S_{1}$')
plt.plot(x_arr, sin_aprox(x_arr,2), label = r"$S_{2}$")
plt.plot(x_arr, sin_aprox(x_arr,3), label = r"$S_{3}$")
plt.plot(x_arr, sin_aprox(x_arr,6), label = r"$S_{6}$")
plt.plot(x_arr, sin_aprox(x_arr,12), label = r"$S_{12}$")
plt.axis([0,4*np.pi,-2,2])
plt.legend()
plt.show()

## Kommentar: Man ser at desto større n er, jo mer tilnærmet er
## f_aprox til f=sinx

#### Kjøreeksempel
"""
>> python plot_Taylor_sin.py
(plot)
"""
