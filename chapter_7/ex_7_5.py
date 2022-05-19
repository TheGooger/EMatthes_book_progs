prompt = "Enter your age to know the price: "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Ticket is free!")
    elif age <= 12:
        print("Ticket costs $10!")
    else:
        print("Ticket costs $15!")
