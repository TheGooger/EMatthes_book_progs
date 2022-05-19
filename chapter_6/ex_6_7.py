human_0 = {
    'first_name': 'georgy',
    'last_name': 'sergeev',
    'age': 22,
    'city': 'st. petersburg',
    }
human_1 = {
    'first_name': 'vladimir',
    'last_name': 'ivanov',
    'age': 23,
    'city': 'st. petersburg',
    }
human_2 = {
    'first_name': 'Dasha',
    'last_name': 'fedorovich',
    'age': 22,
    'city': 'krasnoyarsk',
    }
people = [human_0, human_1, human_2]

for human in people:
    full_name = human['first_name'] + " " + human['last_name']
    print("\nThe person's full name: " + full_name.title() + ".")
    if human['first_name'].lower() == 'dasha':
        print("She is " + str(human['age']) + " years old.")
        print("She was born in " + human['city'].title())
    else:
        print("He is " + str(human['age']) + " years old.")
        print("He was born in " + human['city'].title() + ".")
