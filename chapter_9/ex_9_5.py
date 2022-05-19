class User():
    """Создает пользователя."""
    
    def __init__(self, f_name, l_name, u_age, u_nickname):
        """Инициализирует имя, фамилию, возраст и никнейм пользователя."""
        self.first_name = f_name
        self.last_name = l_name
        self.age = u_age
        self.nickname = u_nickname
        self.login_attempts = 0
    
    def describe_user(self):
        """Выводит информацию о пользователе."""
        print("User's full name is " + self.first_name.title() + " " +
            self.last_name.title() + ".")
        print("User's age is " + str(self.age) + ".")
        print("User's nickname is " + self.nickname + ".")
        
    def greet_user(self):
        """Персональное приветствие пользователя."""
        print("Hello, " + self.nickname + "!")
        
    def increment_login_attempts(self):
        """Увеличивает число попыток входа на 1."""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Обнуляет количество попыток входа."""
        self.login_attempts = 0
        

user_0 = User('vova', 'ivanov', 23, 'TheGooger')
print(user_0.login_attempts)
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)
