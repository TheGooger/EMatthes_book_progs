cities = {
    'st. petersburg': {
        'country': 'russia',
        'population': 300,
        'fact': 'beautiful',
        },
    'new york': {
        'country': 'usa',
        'population': 500,
        'fact': 'central park in it',
        },
    'london': {
        'country': 'great britain',
        'population': 350,
        'fact': 'the capital of UC',
        },
    }
visited_cities = ['st. petersburg', 'krasnoyarsk', 'london', 'krakow']

print("Here is the list of cities I have visited last year:")
for v_city in visited_cities:
    print(v_city.title())
print("I have information about some of them:")
for city, city_info in cities.items():
    if city in visited_cities:
        print(city.title() + ":")
        print("\t" + city.title() + " is in " +
            city_info['country'].title() + ".")
        print("\tPopulation is about " + str(city_info['population']) + ".")
        print("\tInteresting fact about " + city.title() + ": " + 
            city_info['fact'])
