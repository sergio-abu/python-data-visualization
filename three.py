import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

point_ord = list(range(rw.num_points))

plt.scatter(rw.x_val, rw.y_val, s=2, c=point_ord, cmap=plt.cm.Purples, edgecolors='none')

plt.scatter(0, 0, c='green', edgecolors='none', s=20)
plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', edgecolors='none', s=20)

# for resize, background color, dimensions use plt.figure()
plt.show()