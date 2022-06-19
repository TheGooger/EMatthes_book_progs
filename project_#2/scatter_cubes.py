import matplotlib.pyplot as plt
import pylab as pl

x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Greens)
plt.title('Cubes of Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
pl.tick_params(axis='both', labelsize=14)
plt.axis([0, 1100, 0, 1100000000])
plt.show()
