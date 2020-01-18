"""Fra Fahrenheit til Celsius"""
def C(f):
    C = (5/9)*(f - 32)
    return(C)

def F(c):
    F = (9/5)*c + 32
    return(F)

print(F(C(10)))  ### Skal være samme som f

print(C(F(12)))  ### skal være det samme som c
