### Oppgave 5.41
### Plot sum av sinus approksimasjonen til en funksjon f

# Først definerer jeg en funksjon for sinussummer
## dvs. approksimasjonen

## eventuelt bruke sorted. Kan sortere elementene
# inn etter logiske argument (?)

from numpy import pi, sin, linspace, array, append

## sinus sum approksimasjonen
def S(t,n,T=2*pi):
    sum_ = 0
    for i in range(1,n+1,1):
        ledd_i = (4/pi)*1/(2*i-1)*sin(2*(2*i-1)*pi*t/T)
        sum_ += ledd_i
    return sum_
## Skriver så en funksjon for f eksakt


def f(t,T=2*pi):
    n = len(t)
    f_t = [0]*n
    for i in range(n):
        if 0 < t[i] < T/2:   # any. #np.logical_array?() #
            f_t[i] = 1
        elif t[i] == T/2:   # tol = 1e-14
            f_t[i] = 0
        elif T/2 < t[i] < T:
            f_t[i] = -1
    return f_t

    # Kommentar: Programmet kjører, men det tar lang tid.
    # Er det en bedre måte å gjøre dette på?

# Lager array for t.
t_arr = linspace(0.1,1.9*pi,1000) # bruker linspace. Ønsker 0 < t < T


# Dermed kan vi plotte ved å kalle på funksjonene
import matplotlib.pyplot as plt
sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

plt.plot(t_arr, S(t_arr,1), label ='S{}(t,n=1)'.format('1'.translate(sub)))
plt.plot(t_arr, S(t_arr,3), label = 'S{}(t,n=3)'.format('3'.translate(sub)))
plt.plot(t_arr, S(t_arr,20), label = 'S{}(t,n=20)'.format('20'.translate(sub)))
plt.plot(t_arr, S(t_arr,200), label = 'S{}(t,n=200)'.format('200'.translate(sub)))
plt.plot(t_arr, f(t_arr), label = 'f(t)')
plt.xlabel('t-akse')
plt.ylabel('y-akse: f(t)')
plt.legend()
plt.show()

## Kjøreeksempel
""" >> python sinesum1_plot.py
(plot)
"""
""" Kommentar: Ser at for større n er S(t,n) bedre tilnærmet f(t)
