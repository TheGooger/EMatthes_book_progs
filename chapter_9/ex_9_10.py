#import restaurant
from restaurant import Restaurant, IceCreamStand

davido = Restaurant('davido', 'shawarma')
davido.describe_restaurant()
davido.open_restaurant()

tasty = IceCreamStand('tasty', 'ice cream', ['apple', 'banana'])
tasty.describe_restaurant()
tasty.get_flavors()

