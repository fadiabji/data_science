import matplotlib.pyplot as plt
plt.style.use('seaborn')


# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
#ax.scatter(x_values,y_values,c='red',s=10)
#ax.scatter(x_values,y_values,c=(0, 0.8, 0),s=10)
ax.scatter(x_values,y_values, cmap=plt.cm.Blues ,s=10)



# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

# set the range for each axis.
ax.axis([0,1100, 0, 1210000])

# plt.show()

#Saving Your Plots Automatically
plt.savefig('squares_plot.png', bbox_inches='tight')
