import pygal

from die import Die

# Creating of D6 die.
die_1 = Die(8)
die_2 = Die(8)
# Series of rolls with saving results in list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# Analysis.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# Visualization of results.
hist = pygal.Bar()
hist.title = 'Results of rolling two D8s 50000 times.'
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')
