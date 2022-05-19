from user import User
from admin import Admin

vova = Admin('vova', 'ivanov', 23, 'TheGooger')
dasha = User('dasha', 'fedorovich', 22, 'desp.df')

vova.greet_user()
vova.privileges.show_privileges()

dasha.describe_user()
dasha.greet_user()
