import json

numbers = [2, 3, 5, 7, 11, 13]

#filename = 'numbers.json'
filename = 'numbers_1.txt'
with open(filename, 'w') as f_obj:
    #json.dump(numbers, f_obj)
    f_obj.write(str(numbers))
