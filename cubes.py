import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values ,c=y_values ,cmap= plt.cm.Blues ,s=1)

ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel('values',fontsize=12)
ax.set_ylabel('cubes of vaules', fontsize=12)


plt.show()

