class Car():
    """Простая модель автомобиля."""
    
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles  
        
    def fill_gas_tank(self):
        """Заправляет автомобиль."""
        print(self.make.title() + " " + self.model.title() + " is refueling!")
        

class ElectricCar(Car):
    """Представляет аспекты автомобилей, специфические для электроомбилей."""
    
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make,model,year)
        self.battery_size = 70
        
    def describe_battery(self):
        """Выводит информацию о мощности аакамулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def fill_gas_tank(self):
        """У электромобилей нет бензобака!"""
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_old_car = Car('skoda', 'octavia', 2000)
print(my_old_car.get_descriptive_name())
my_old_car.fill_gas_tank()
my_tesla.fill_gas_tank()
