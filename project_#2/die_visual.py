import pygal

from die import Die

# Creating of D6 die.
die = Die()
# Series of rolls with saving results in list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# Analysis.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
# Visualization of results.
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
