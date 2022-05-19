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
        full_name = self.first_name.title() + " " + self.last_name.title()
        print("User's full name is " + full_name + ".")
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
   
   
class Privileges():
    """Создает привилегии администратора."""
    
    def __init__(self):
        """Инициализирует атрибуты привилегий."""
        self.privileges = [
            'can send messages',
            'can delete user',
            'can ban user',
            'can edit other\'s messages'
            ]
    
    def show_privileges(self):
        """Показывает привелегии администратора."""
        print("Admin has the gollowing privileges:")
        for privilege in self.privileges:
            print("-" + privilege)
    
            
class Admin(User):
    """Создает администратора."""
    
    def __init__(self, f_name, l_name, u_age, u_nickname):
        """
        Инициализирует атрибуты класса-родителя.
        Инициализирует атрибуты администратора.
        """
        super().__init__(f_name, l_name, u_age, u_nickname)
        self.privileges = Privileges()

    
admin = Admin('vova', 'ivanov', 23, 'TheGooger')
admin.describe_user()
print("\n")
admin.privileges.show_privileges()


