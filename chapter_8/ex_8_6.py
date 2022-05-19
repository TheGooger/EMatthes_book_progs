def city_country(city, country):
    c_c = city.title() + ', ' + country.title() + "."
    return c_c

message = city_country('st. petersburg', 'russia')
print(message)
print(city_country('boston', 'usa'))
print(city_country(country='uk', city='london'))
