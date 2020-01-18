### While loop ###
"""s = 0; k = 1; M = 100

while k < M:
    s += 1/k
    print(s)
    k += 1"""

### Det samme skrevet som for loop ###
# for er begrenset av en liste
# ofte beskrevet med range
# loop er avgrensen av boolsk logikk (ulikheter)
"""
s = 0
for i in range(100):
    s += (1/(i+1))
    print("%.5f" %s)
"""
# kan også skrives på måten

s = 0
for i in range(1,100,1):
    s = s + 1/i
    print("%.5f" %s)

##2.13: Simulere et program for hånd
