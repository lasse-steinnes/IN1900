### Fyoppg. 2.2 Relativistic momentum ###
from math import e

## a) Skal skrive ut hastighet og bevegelsesmengde
## Definerer variablene
m = 1200     ## masse [kg]
c = 3e8
v = 0
# v_maks ## ganger 0.9 makshastighet
dV = 0.1*c  ## ganger 0.1

  ## Klassisk bevegelsesmengde
 ### nær tilnærming ved lav hastighet
print ("-----------------------")
print ("v f")
for i in range(0,10,1):
    p_klas = m*i*dV
    print("% "i*dV, p_klas) % ()


"""
p_rel = m*v*lambda_  ### faktisk bevegelsesmengde

lamda_ = 1/(1-V**2/c**2)"""
