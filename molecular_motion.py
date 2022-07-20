import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(19.2, 10.08)) # figsize to alter the size to fill the screen
    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values,linewidth=2)
    # edgecolors to get rid of the black outline around each point

    # emphasize the first and last points.
    ax.scatter(0, 0 , c='green', edgecolors='none', s=200)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c= 'red', edgecolors='none', s=200)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break


