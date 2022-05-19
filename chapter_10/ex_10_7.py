print("Give me two numbers and I'll tell you the sum!")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:    
        total = int(first_number) + int(second_number)
    except ValueError:
        msg = "Please, enter the number."
        print(msg)
    else:
        print("The sum is " + str(total))
    

