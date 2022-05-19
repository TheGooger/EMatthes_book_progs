topping = ""
prompt = "Please, choose the topping: "
prompt += "\nIf you're finished, enter 'quit'."
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print("You've ordered a pizza with " + topping)

