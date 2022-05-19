class User():
    """Создает пользователя."""
    
    def __init__(self, f_name, l_name, u_age, u_nickname):
        """Инициализирует имя, фамилию, возраст и никнейм пользователя."""
        self.first_name = f_name
        self.last_name = l_name
        self.age = u_age
        self.nickname = u_nickname
    
    def describe_user(self):
        """Выводит информацию о пользователе."""
        print("User's full name is " + self.first_name.title() + " " +
            self.last_name.title() + ".")
        print("User's age is " + str(self.age) + ".")
        print("User's nickname is " + self.nickname + ".")
        
    def greet_user(self):
        """Персональное приветствие пользователя."""
        print("Hello, " + self.nickname + "!")
        

user_0 = User('vova', 'ivanov', 23, 'TheGooger')
user_1 = User('dasha', 'fedorovich', 22, 'desp.df')
user_2 = User('gosha', 'sergeev', 22, 'georgy')

user_0.describe_user()
user_0.greet_user()
print("---")
user_1.describe_user()
user_1.greet_user()
print("---")
user_2.describe_user()
user_2.greet_user()
print("---")

