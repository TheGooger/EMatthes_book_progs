import json

filename = 'user_number.json'
with open(filename) as f_obj:
    u_number = json.load(f_obj)
    print("Your number is " + str(u_number) + "!")
