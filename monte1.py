import random
import numpy
import time

start = time.time()

pi = 3.14
trial = 10000000
x = []
y = []
true = 0
false = 0
for i in range(trial):
    x.append(random.uniform(0, 1))
    y.append(random.uniform(0, 1))
    i = i+1

for i in range(trial):
    if numpy.sqrt(x[i]**2+y[i]**2) < 1:
        true = true+1
    elif numpy.sqrt(x[i]**2+y[i]**2) > 1:
        false = false+1

result = 4*(true/(true+false))

print(result)

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
