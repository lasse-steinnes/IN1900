""" Tilnaermet Fahrenheit til Celsius """
### Lage en liste med for løkke Fahrenheit

F_degrees = []
n = 11
F_min = 0
F_maks = 100
dF = 10

for f in range(0,n):
    F = F_min + (f*dF)
    F_degrees.append(F)

## print(F_degrees)

###  Lage en liste med Celsius
## Bruker list comprehension

C_degrees = [(5/9)*(F - 32) for F in F_degrees]

## print(C_degrees)

## tilnærmet celsius

C_hat = [(F - 30)/2for F in F_degrees]

## print (C_hat)

# list comprehension for all tables
table = [[F, C, chat] for F, C, chat in zip(F_degrees, C_degrees, C_hat)]
print("""Slik ser tabellen ut for fahrenheit(F), celsius(C)\
 og en tilnærming til C(C_hat).
Observerer at C_hat er en grei\
 tilnærming til C, men feilverdien øker for lave eller høye verdier av C""")

print("""-------------------------------
F            C       C_hat """)
print("-------------------------------")

for f in range(len(F_degrees)):
    print("%-10.1f %-10.1f %-10.1f" % (F_degrees[f], C_degrees[f], C_hat[f]))
print("-------------------------------")


### Kjøreeksempel
""" >> python f2c_approx_table.py
Slik ser tabellen ut for fahrenheit(F), celsius(C) og en tilnærming til C(C_hat).
Observerer at C_hat er en grei tilnærming til C, men feilverdien øker for lave eller høye verdier av C
-------------------------------
F            C       C_hat
-------------------------------
0.0        -17.8      -15.0
10.0       -12.2      -10.0
20.0       -6.7       -5.0
30.0       -1.1       0.0
40.0       4.4        5.0
50.0       10.0       10.0
60.0       15.6       15.0
70.0       21.1       20.0
80.0       26.7       25.0
90.0       32.2       30.0
100.0      37.8       35.0
-------------------------------
"""
