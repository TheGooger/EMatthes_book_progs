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
        
        
class IceCreamStand(Restaurant):
    """Описывает киоск с мороженным."""
    
    def __init__(self, r_name, c_type, flavors):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты киоска с мороженным.
        """
        super().__init__(r_name, c_type)
        self.flavors = flavors
        
    def get_flavors(self):
        """Выводит список вкусов."""
        message = "In " + self.restaurant_name.title() + " we have "
        message += "the following flavors:"
        print(message)
        for flavor in self.flavors:
            print("-" + flavor)
