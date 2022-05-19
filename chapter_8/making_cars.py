def make_car(prod, name, **car_info):
    car = {}
    car['producer'] = prod
    car['name'] = name
    for key, value in car_info.items():
        car[key] = value
    return car
