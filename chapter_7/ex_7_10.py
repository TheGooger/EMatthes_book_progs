responses = {}

while True:
    name = input("What is your name? ")
    weekend = input("Where do you want to go to weekend? ")
    responses[name] = weekend
    temp = input("Do you want to continue? (yes/no) ")
    if temp == 'no':
        break

print("\n--- Results ---")
for name,weekend in responses.items():
    print(name.title() + " wants to go to " + weekend + ".")
