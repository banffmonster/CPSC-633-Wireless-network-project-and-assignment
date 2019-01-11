import random
import numpy as np
data = []
sink = [0, random.randint(0, 50), random.randint(0, 50), 100, 0]
data.append(sink)
for i in range(50):
    d = [i+1, random.randint(0, 50), random.randint(0, 50), random.randint(30, 50), random.random()]
    data.append(d)


np.savetxt('AFN.dat', data)


Delay = [[0 for i in range(51)]for j in range(51)]
for i in range(51):
    for j in range(51):
        if i == j:
            Delay[i][j] = 0
        else:
            Delay[i][j] = random.random()

np.savetxt('Delay.dat', Delay)
