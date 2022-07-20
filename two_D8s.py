from die import Die
from plotly.graph_objs import Bar, Layout 
from plotly import offline

die8_1 = Die(8)
die8_2 = Die(8)

# Make some rolls. and store results in a list.
results = []
for roll_num in range(1000):
    result = die8_1.roll() * die8_2.roll()
    results.append(result)


# Analizing the Results by counting how many times we roll each number
frequences = []
max_result = die8_1.num_sides + die8_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequences.append(frequency)

# Visualize the results.
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequences)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1000 times.', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename= 'd8_d8.html')


