sandwich_orders = ['pastrami', 'fish', 'meat', 'pastrami',
    'vegan', 'cheese', 'pastrami']
finished_sandwiches = []

print("Here is the list with ordered sanwiches: ")
print(sandwich_orders)
print("Sorry, we don't have pastrami sandwiches!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\nNew list: ")
print(sandwich_orders)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I am cooking your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
    
print("\nHere is the list of cooked sandwiches: ")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " sandwich.")

