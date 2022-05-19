import json

def get_number():
    """Загружает число пользователя из файла, если оно там есть."""
    filename = 'user_number.json'
    try:
        with open(filename) as f_obj:
            u_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return u_number

def show_number():
    """Выводит сообщение с числом, если оно есть."""
    u_number = get_number()
    if u_number:
        print("I know your number, it is " + str(u_number) + "!")
    else:
        load_number()
        print("I'll remember your number!")
        
def load_number():
    """Загружает имя в файл, если его нет."""
    filename = 'user_number.json'
    with open(filename, 'w') as f_obj:
        u_number = input("What is your number? ")
        json.dump(u_number, f_obj)
        


#filename = 'user_number.json'
#try:
#    with open(filename) as f_obj:
#        u_number = json.load(f_obj)
#except FileNotFoundError:
#    u_number = input("What is your number? ")
#    with open(filename, 'w') as f_obj:
#        json.dump(u_number, f_obj)
#        print("I'll remember your number!")
#else:
#    print("I know your number, it is " + str(u_number) + "!")
show_number()
