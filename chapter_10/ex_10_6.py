print("Give me two numbers and I'll tell you the sum!")

first_number = input("First number: ")
second_number = input("Second number: ")
try:    
    total = int(first_number) + int(second_number)
except ValueError:
    msg = "Please, enter the number."
    print(msg)
else:
    print("The sum is " + str(total))
    
