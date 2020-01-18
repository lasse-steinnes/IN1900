## Oppgave 5.22 Plot en turs strekning og hastighet ###

# Første linje i fila: s , antall sekunder
# Posisjonen er lagret som x,y

# a) Skal plotte 2D-kurven for dataene i fila. Dvs y som en funksjon av x

# Krever at man først leser fila
import numpy as np

innfil = open('pos.txt','r')

sec = float(innfil.readline())

dat_list = []
for line in innfil:
    dat_list.append(line.split())

# print(dat_list)

x_arr = np.zeros(len(dat_list))
y_arr = np.zeros(len(dat_list))

for i in range(len(dat_list)):
    x_arr[i] = float((dat_list[i][0]))
    y_arr[i]=  float((dat_list[i][1])) # Array automatisk float (merk)

# Dermed har jeg arrayene og kan plotte
import matplotlib.pyplot as plt

plt.plot(x_arr, y_arr, label = "Oversikt over turen")
plt.xlabel('Breddegrader')
plt.ylabel('Lengdegrader')
plt.title('Posisjon målt hvert 15. sekund')
plt.legend()
plt.grid()
plt.show()

########  Oppgave b) ########
# Vi ser at posisjon x,y er registert hvert 15. sek
# Siden vi ikke har en kontinuerlig kurve må vi tilnærme den reelle situasjone
# med numerisk differensiering.
# Vi ser på gjennomsnittsfarten over intervaller (numerisk differensiering)

v_x = [(x_arr[i+1]-x_arr[i])/sec for i in range(0,len(x_arr)-1)] # På tide å repetere list comprehension
#print(v_x)
v_y = [(y_arr[i]-y_arr[i-1])/sec for i in range(1,len(x_arr))]
#print(v_y)

# Lager array for s verdiene
s = np.linspace(0, sec*len(v_x),23) # 23 punkter med likt mellomrom.
# print(len(v_x))

plt.figure(figsize =(8,6))

plt.subplot(121)
plt.plot(s,v_x[:-1], label = 'A: Breddegrader' )
# plt.legend(loc = 'upper right')
plt.title('A: Breddegrader')
plt.xlabel('Tid[sek]')
plt.ylabel('Hastighet[grad/sek]')

plt.subplot(122)
plt.plot(s,v_y[:-1], label = 'B: Lengdegrader')
# plt.legend(loc = 'upper right')
plt.title('B: Lengdegrader')
plt.xlabel('Tid[sek]')

plt.subplots_adjust(left=0.15, right=0.9,\
                wspace=0.4)
#plt.tight_layout()
plt.show()

####### Kjøreeksempel ####
"""
>> python position2velocity.py
(plot1)
(plot2)
"""
