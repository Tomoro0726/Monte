import random
import numpy
import time

def sim(trial):
    true = 0
    for i in range(trial):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 < 1:
            true += 1

    print(4*true / trial)

start = time.time()
trial = 1000000
sim(trial)
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")