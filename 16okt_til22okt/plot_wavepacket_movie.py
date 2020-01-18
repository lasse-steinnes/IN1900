##### Oppgave 5.33. Animer en bølgepakke####

# En bølgepakke er en sammensatt bølge
# med utslag som er begrenset i tid og rom

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# definerer funksjonen
bølge = lambda x,t: np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))


## Lager intervallet for x
x_arr = np.linspace(-6,6,1001)
t_arr = np.linspace(-1,1,61)

y_max = np.amax(bølge(x_arr, 0))

lines = plt.plot([],[]) # lager plotobjekt, med tomme brackets
# 6 frames per second

# Slik at bølge = bølge(x_matrise,t_matrise)

# Funksjonen er definert
### Først initialiseres plottet
def init():
    plt.axis([x_arr[0],x_arr[-1],-y_max-0.5,y_max+0.5])
    plt.xlabel("x")
    plt.ylabel("Amplitude")
    plt.title("Animasjon av en bølgepakke")
    lines[0].set_xdata(x_arr)
    return lines

def update(frame):
    y = bølge(x_arr,frame)
    lines[0].set_ydata(y)
    return lines

ani = FuncAnimation(plt.gcf(), update, frames = t_arr, \
        init_func = init, blit = True)
# plt.pause(0.1) Funker ikke
                ### Hvordan stiller man inn 6 frames per sekund?
plt.show()

## Kjøreeksempel
"""
>> python plot_wavepacket_movie.py
(animasjon)
"""
