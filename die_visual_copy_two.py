from plotly_review import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store result in a list
results = [die_1.roll() * die_2.roll() for result in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in range(1,die_1.num_sides + die_2.num_sides+1)]

# Visualize the results.
x_values = list(range(1, die_1.num_sides + die_2.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Reequency of Result'}

my_layout = Layout(title = 'Result of rolling three d6 1000 times', xaxis= x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout': my_layout}, filename='d6_d6.html')
