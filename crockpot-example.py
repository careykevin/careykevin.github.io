import time
from random import randint

RAND = randint(0, 9)

if RAND < 2:
    raise Exception("Simulated exception")
elif RAND < 4:
    print "Simulated delay"
    time.sleep(30)

print RAND
