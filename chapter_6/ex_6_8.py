ustas = {
    #'name': 'ustas',
    'animal': 'dog',
    'owner': 'vova',
    }
grey = {
    'animal': 'dog',
    'owner': 'ksenia',
    #'name': 'grey',
    }
thomas = {
    'animal': 'cat',
    'owner': 'lena',
    #'name': 'thomas',
    }
pets = [ustas, grey, thomas]

#for pet in pets:
#    print(pet['name'].title() + " is a " + pet['animal'] + "." +
#        " It's owner is " + pet['owner'].title() + ".")
print("We have three pets.")
for pet in pets:
    print("If the owner is " + pet['owner'].title() + 
        " then his/her pet is " + pet['animal'] + ".")

