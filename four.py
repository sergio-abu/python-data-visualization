import matplotlib.pyplot as plt
from random_walk import RandomWalk

# MOLECULAR MOTION

rw = RandomWalk()
rw.fill_walk()

plt.plot(rw.x_val, rw.y_val, linewidth=1)

plt.scatter(0, 0, c='green', edgecolors='none', s=500)
plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=500)

# for resize, background color, dimensions use plt.figure()
plt.show()