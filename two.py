import matplotlib.pyplot as plt

x_val = list(range(1, 1001))
y_val = [x**2 for x in x_val]


plt.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Greys, edgecolors='none', s=25)
plt.title('sqare numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)
plt.tick_params(axis='both', which='major')
plt.axis([0, 1100, 0, 1100000])

plt.show()