### Oppgave 5.5 Kjemiheftet  ###

"""Deloppgave a"""
import numpy as np

k_1 = 5.01*10**-7
k_2 = 4.79*10**-11

ph_arr = np.arange(4,13,1e-4)

# ph = -log(oksonium)
oks_arr = 1/(10**(ph_arr))

# Konsentrasjonene for de ulike pH:
co2_arr = oks_arr**2/(oks_arr**2 + k_1*oks_arr + k_1*k_2)


hco3_arr = k_1*oks_arr/(oks_arr**2 + k_1*oks_arr + k_1*k_2)

co3_2_arr = k_1*k_2/(oks_arr**2 + k_1*oks_arr + k_1*k_2)

## plotter
"""
import matplotlib.pyplot as plt

plt.plot(ph_arr,co2_arr,'r-', label = '{}'.format(r'$CO_{2}$'))
plt.plot(ph_arr,hco3_arr,'b-',label = '{}'.format(r'$HCO_{3}^{-}$'))
plt.plot(ph_arr,co3_2_arr, 'g-', label = '{}'.format(r'$CO_{3}^{2-}$'))
plt.title('Likevektene blir forskjøvet avhengig av pH')
plt.legend()
plt.xlabel('pH')
plt.ylabel('Konsentrasjon [mol/L]')
plt.show()
"""

"""Deloppgave b"""

def fortegn(arr1,arr2,arr3):
    tol = 1e-12
    diff1 = arr1 - arr2
    for i in range(len(co2_arr)):
        if diff1[i] < 0:
            diff1[i] = -1
        elif abs(diff1[i]) < tol:
            diff1[i] = 0           ### Litt vanskelig å forstå at jeg ikke får
                                    ## nuller, men det får jeg kanskje med høyere oppløsning. Altså flere punkter for ph.
        elif diff1[i] > 0:
            diff1[i] = 1

    diff2 = arr2-arr3
    for i in range(len(co2_arr)):
        if diff2[i] < 0:
            diff2[i] = -1
        elif  abs(diff1[i]) < tol:
            diff2[i] = 0
        elif diff2[i] > 0:
            diff2[i] = 1
    return diff1, diff2


def skjare(arr1,arr2,arr3):
    fortegnv_ = fortegn(arr1,arr2,arr3)
    d1 = fortegnv_[0]
    d2 = fortegnv_[1]

    krysspunkt1 = []
    kryss1 = []
    for i in range(1,len(d1)):
        if d1[i] == 1\
        and d1[i+1] == -1:
            krysspunkt1.append(i)
    for i in range(len(krysspunkt1)):
        kryss1.append(arr1[krysspunkt1[i]])

    krysspunkt2 = []
    kryss2 = []
    for i in range(1,len(d2)):
        if d2[i-1] == 1 \
        and d2[i] == -1:
            krysspunkt2.append(i)
    for i in range(len(krysspunkt2)):
        kryss2.append(arr2[krysspunkt2[i]])

    print(ph_arr[krysspunkt1], kryss1, ph_arr[krysspunkt2], kryss2)
    return ph_arr[krysspunkt1], kryss1, ph_arr[krysspunkt2], kryss2

kryss_ = skjare(co2_arr,hco3_arr,co3_2_arr)

import matplotlib.pyplot as plt

# plotter med krysspunktene
plt.figure(figsize=(9,6))

plt.plot(ph_arr,co2_arr,'r-', label = '{}'.format(r'$CO_{2}$'))
plt.plot(ph_arr,hco3_arr,'b-',label = '{}'.format(r'$HCO_{3}^{-}$'))
plt.plot(ph_arr,co3_2_arr, 'g-', label = '{}'.format(r'$CO_{3}^{2-}$'))
plt.plot(kryss_[0],kryss_[1], 'mo', label =\
                '{}{:.2f},{}{:.2f}'.format(r'$x_{0}=$',kryss_[0][0], r'$y_{0}=$',kryss_[1][0]))
plt.plot(kryss_[2],kryss_[3], 'co', label =\
                '{}{:.2f},{}{:.2f}'.format(r'$x_{0}=$',kryss_[2][0], r'$y_{0}=$',kryss_[3][0]))
plt.title('Likevektene blir forskjøvet avhengig av pH')
plt.legend(loc = 'center right')
plt.xlabel('pH')
plt.ylabel('Konsentrasjon [mol/L]')
plt.show()

#### Kjøreeksempel
"""
>> python bjerrum_plot.py
[ 6.3001] [0.50001195024927003] [ 10.3197] [0.49995565969919664]
(Kommentar:Skjæringspunktene)
(plot, med skjæringspunkter)
"""
