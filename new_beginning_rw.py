import matplotlib.pyplot as plt
from newbeginning290622 import RandomWalk

# Make a random walk
rw = RandomWalk(50000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use("classic")
fig, ax = plt.subplots(figsize=(15,9))
point_numbers = range(rw.num_points)

ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
ax.scatter(0, 0, c='green', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

# Removing the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()