class Restaurant():
    """Создает ресторан."""
    
    def __init__(self, r_name, c_type):
        """Инициализирует имя ресторана и тип кухни."""
        self.restaurant_name = r_name
        self.cuisine_type = c_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Описывает ресторан."""
        print("Restaurant's name is " + self.restaurant_name.title() + ".")
        print("Cuisine type is " + self.cuisine_type + ".")
        
    def open_restaurant(self):
        """Открывает ресторан."""
        print(self.restaurant_name.title() + " is opened!")
        
    def set_number_served(self, num_serv):
        """Задает число обслуженных посетителей."""
        self.number_served = num_serv
        
    def increment_number_served(self, num):
        """Увеличивает число обслуженных на определенное значение."""
        self.number_served += num


restaurant = Restaurant('davido', 'shawarma')
print(restaurant.number_served)
restaurant.set_number_served(50)
restaurant.increment_number_served(50)
restaurant.set_number_served(0)
restaurant.increment_number_served(50)
restaurant.increment_number_served(50)
print(restaurant.number_served)
