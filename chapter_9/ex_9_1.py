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
        

restaurant = Restaurant('davido', 'shawarma')
#print("We opened restaurant '" + restaurant.restaurant_name.title() + "'!")
#print("We cook " + restaurant.cuisine_type + " here!")
restaurant.describe_restaurant()
restaurant.open_restaurant()
