### Oppgave 3.36: Omskrive en matematisk funksjon ###

## summen av L(x,n)
## Får ut feil sum, men koden fungerer.

def L(x,epsilon):
    ci = 0
    for i in range(1,epsilon+1,1):
        ci += (1/i)*(x/(1 + x))**i
    return ci

### Kommentar: Hva skjer om jeg skriver ci += ci etterpå

sum_x4_n2 = L(4,2)

sum_x4_n3 = L(4,3)

sum_x4_n4 = L(4, 4)

print(sum_x4_n2)
print(sum_x4_n3)
print(sum_x4_n4)

### a) Summen kan skrives på formen
# ci = ac(i-1)
# der a = (x/(1+x))*((i-1)/i)

## b) skriver programmet l3_ci(epsilon)
### Riktig!!!!

def L3_ci(x,epsilon):
    term = (1/1)*(x/(1 + x))**1
    ci = term
    for i in range(2,epsilon+1,1):
        a = ((x/(1+x))*((i-1)/i))
        term = term*a
        ci += term
    return ci

sum_x4_n2new = L3_ci(4,2)

print("Dette er den samme summen: %.2f" %(sum_x4_n2new))

# c) test_L3_ci , kunne gjort dette på annen måte?

def test_L3_ci(x, epsilon):
    if L3_ci(x,epsilon) == L(x,epsilon):
        statement = "True"
    else:
        statement = "False"
    return statement

en_test = test_L3_ci(4,2)

print(en_test)
