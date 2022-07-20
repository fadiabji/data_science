from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die6_1 = Die()
die6_2 = Die()
die6_3 = Die()

# Make some rolls. and store results in a list.
results = []
for roll_num in range(1000):
    result = die6_1.roll() + die6_2.roll() + die6_3.roll()
    results.append(result)


frequences = []
max_result = die6_1.num_sides + die6_2.num_sides + die6_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequences.append(frequency)



# Visualize the results.
x_values = list(range(3,max_result+1))
data = [Bar(x=x_values, y=frequences)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 dice 1000 times.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename= 'd6_d6_d6.html')