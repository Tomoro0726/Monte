import random
import numpy
import matplotlib.pyplot as plt
import time

start = time.time()

trial = 1000000
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


c1 = plt.Circle((0, 0), radius=1, fc="None",
                ec="r", linewidth=2, color="black")
ax = plt.gca()
ax.add_patch(c1)
plt.axis("scaled")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("PLOT")

plt.scatter(x, y, marker=".", color="blue", label="POINT")
plt.show()
