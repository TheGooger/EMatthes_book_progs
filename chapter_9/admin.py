#from user import User
import user

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
    
            
class Admin(user.User):
    """Создает администратора."""
    
    def __init__(self, f_name, l_name, u_age, u_nickname):
        """
        Инициализирует атрибуты класса-родителя.
        Инициализирует атрибуты администратора.
        """
        super().__init__(f_name, l_name, u_age, u_nickname)
        self.privileges = Privileges()
