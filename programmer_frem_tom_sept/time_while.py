import time
t0 = time.time()
while time.time() - t0 < 10:
    print(".... I like while loops!")
    time.sleep(2)
print("Oh, no - the loop is over.")

### Algoritme for programmet
# 1. importerer tidsmodulen
# 2. bruker funksjonen time.time() som stoppeklokke
# 3. Utfører loop hvert 2. sekund til s=10.
# Repeterer string 5 ganger.

# Om ulikheten endres blar den aldri inn i loopen
