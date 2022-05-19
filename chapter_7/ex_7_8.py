sandwich_orders = ['fish', 'meat', 'vegan', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I am cooking your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
    
print("\nHere is the list of cooked sandwiches: ")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " sandwich.")
