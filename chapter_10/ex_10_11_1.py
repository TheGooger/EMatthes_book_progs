import json

number = input("What is your number? ")
filename = 'user_number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
