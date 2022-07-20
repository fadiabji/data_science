import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1,4, 9, 16, 25]
plt.style.use('seaborn')


fig, ax = plt.subplots() # this function can generate one or more plots in the same figure. # it is convention way to plot using matplotlib
ax.plot(input_values, squares, linewidth=3)

# Set chart title and lable axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick lables.
ax.tick_params(axis='both', labelsize=14)
plt.show()
