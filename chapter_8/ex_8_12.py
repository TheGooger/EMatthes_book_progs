def make_sandwiches(*toppings):
    print("You've ordered a sandwich with:")
    for topping in toppings:
        print("- " + topping)
        
make_sandwiches('pepperoni')
make_sandwiches('meat', 'fish', 'tomato')
make_sandwiches('pepper', 'oil')
