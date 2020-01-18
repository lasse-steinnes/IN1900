"""2.9 Store values from a formula in list"""
## Utgangspunkt i 2.8

n = 8
v0 = 5
g = 9.81
t0 = 0
t_end = (2*v0)/g
# y = v0*t - (1/2)*g*t**2
dt = (t_end)/(n+1)

t_list = []
for t in range(0,n,1):
    T = t0 + t*dt
    t_list.append(T)
# print(t_list) test

y_list = [v0*T - (1/2)*g*T**2 for T in t_list] #list comprehension
# print(y_list) test

table_yt = [[T,Y] for T, Y in zip(t_list, y_list)] ## lager nested list som tabell av rekke
# print(table_yt) test

print("Jeg har brukt en for løkke til å lage \
 denne fantastiske tabellen.")

print ("-----------------")
print("  T           Y")
print("-----------------")
for T,Y in table_yt:
    print("%5.2f %10.2f" %(T, Y))
print("-----------------")


## Kjøreeksempel
""" python ball_table2.py
>>

Jeg har brukt en for løkke til å lage  denne fantastiske tabellen.
-----------------
  T           Y
-----------------
 0.00       0.00
 0.11       0.50
 0.23       0.88
 0.34       1.13
 0.45       1.26
 0.57       1.26
 0.68       1.13
 0.79       0.88
-----------------
"""
