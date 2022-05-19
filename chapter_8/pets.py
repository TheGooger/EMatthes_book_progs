def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('hamster', 'harry')
#describe_pet(pet_name='ustas', animal_type='dog')
describe_pet('ustas')
