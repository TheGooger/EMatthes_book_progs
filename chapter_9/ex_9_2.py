class Restaurant():
    """Создает ресторан."""
    
    def __init__(self, r_name, c_type):
        """Инициализирует имя ресторана и тип кухни."""
        self.restaurant_name = r_name
        self.cuisine_type = c_type
        
    def describe_restaurant(self):
        """Описывает ресторан."""
        print("Restaurant's name is " + self.restaurant_name.title() + ".")
        print("Cuisine type is " + self.cuisine_type + ".")
        
    def open_restaurant(self):
        """Открывает ресторан."""
        print(self.restaurant_name.title() + " is opened!")
        
restaurant_0 = Restaurant('davido', 'shawarma')
restaurant_1 = Restaurant('mollies', 'beer')
restaurant_2 = Restaurant('mcdonalds', 'fastfood')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
