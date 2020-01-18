#### Oppgave 4.9: Prompt the user for input to a formula ###

v0 = float(input("v0=?"))    # fart [m]
g = 9.81                    # gravitasjonskonstanten []
t = float(input("t=?"))      # tid [sek]

y = (v0*t) - 0.5*g*(t**2)
print("""Ballens posisjon over bakken er %.2f m evaluert
når v0=%.2f og t=%.2f."""%(y,v0, t))

##### Kjøreeksempel
"""
>> python ball_qa.py
Ballens posisjon over bakken er 1.23 m evaluert
når v0=5.00 og t=0.60.
"""
