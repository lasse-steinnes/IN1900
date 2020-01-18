### Oppgave 2.17: (Tre måter å skrive en tabell på)
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
# print(t_list), test

y_list = [v0*T - (1/2)*g*T**2 for T in t_list] #list comprehension
# print(y_list)

### a) Som kolonne

# print(ty_1), test

ty_1 = [t_list, y_list]

print("-----------------")
print("  T           Y")
print("-----------------")
for i in range(len(t_list)):   ### kunne vel egentlig skrevet for i in ty_1 her
    print("%5.2f %10.2f" %(ty_1[0][i], ty_1[1][i]))
print("-----------------")


### b) Som rad (tolker oppgaven at tabellen skal se lik ut som i a, men at
#      listen skal være lagret som tabell av rekker med to indekser, O og 1.)
ty_2 = [[T,Y] for T, Y in zip(t_list, y_list)]
## lager nested list som tabell av rekke
# print(ty_2), test

print ("-----------------")
print("  T           Y")
print("-----------------")
for i in ty_2:
    print("%5.2f %10.2f" %(i[0], i[1]))
print("-----------------")

### Generell uten å benytte nested list i print statement
print ("-----------------")
print("  T           Y")
print("-----------------")
for T in range(len(t_list)):
    print("%5.2f %10.2f" %(t_list[T], y_list[T]))
print("-----------------")

## Kjøreeksempel
""" python ball_table3.py

# For tabell 1
>>
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

# for tabell 2
>>
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

# for tabell 3
>>
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
