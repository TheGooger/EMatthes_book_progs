def make_car(prod, name, **car_info):
    car = {}
    car['producer'] = prod
    car['name'] = name
    for key, value in car_info.items():
        car[key] = value
    return car
    
car_0 = make_car('skoda', 'octavia', age=22,
                 distance=237)
print(car_0)
car_1 = make_car('lada', 'granta', age=4,
                 color='silver',
                 eco=True)
print(car_1)
