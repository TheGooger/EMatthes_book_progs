favorite_numbers = {
    'dasha': [5, 15, 52, 0],
    'vova': [13, 25, 45, 95],
    'gosha': [7],
    'garik': [27, 72],
    'pasha': [39, 69, 85, 5214],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print("\n" + name.title() + "'s favorite number is:")
    else:
        print("\n" + name.title() + "'s favorite numbers are")
    for number in numbers:
        print("\t" + str(number))
