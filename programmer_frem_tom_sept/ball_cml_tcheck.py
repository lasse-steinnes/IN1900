### Test validity of input data
import sys

v0 = float(sys.argv[1])    # fart [m]
g = 9.81                  # gravitasjonskonstanten[]
t = float(sys.argv[2])     # tid [sek]

if  0 < t < 2*v0/g:
    y = (v0*t) - 0.5*g*(t**2)
    print("""Ballens posisjon over bakken er %.2f m evaluert
    når v0=%.2f og t=%.2f."""%(y,v0, t))
else:
    print("t er utenfor definisjonsmengden")
    sys.exit("(1)Feilmelding")                       ### er dette riktig?

#### Kjøreeksempel
"""
# (Kommentar: med verdier innenfor)
>> python ball_cml_tcheck.py 5 0.6
Ballens posisjon over bakken er 1.23 m evaluert
når v0=5.00 og t=0.60.
# (Kommentar: Med verdier utenfor)
>> python ball_cml_tcheck.py 5 0
t er utenfor definisjonsmengden
"""
