## rep. eksamen. oppg 2.1
## Skal skrive program som omgjør F til C
## og lager tabell med F i første kolonne
## C i andre kolonne.
n = 11
F = [0]*n
C = [0]*n
i = 0
print('----------------')
print(' F          C')
print('----------------')
while i < len(F):
    F[i] = 10*i
    C[i] = 5/9*(F[i] - 32)
    print('{:>5}{:> 10.2f}'.format(F[i],C[i]))
    i = i + 1
print('-----------------')
