from die import Die
# Making a Histogram
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two dice.
die_1 = Die()
die_2 = Die()

# Make some rolls. and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analizing the Results by counting how many times we roll each number
frequences = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequences.append(frequency)

# Visualize the results.
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequences)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename= 'd6_d6.html')






