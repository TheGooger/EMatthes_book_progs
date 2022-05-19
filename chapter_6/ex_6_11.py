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

for city, city_info in cities.items():
    print("\n" + city.title() + " is in " + city_info['country'].title() + ".")
    print("Population of " + city.title() + " is about " + 
        str(city_info['population']) + ".")
    print("Interesting fact about " + city.title() + " is: " + 
        city_info['fact'] + ".")
