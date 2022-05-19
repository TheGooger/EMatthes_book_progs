exit_cond = True
prompt = "Please, choose the topping: "
prompt += "\nIf you're finished, enter 'quit'."
while exit_cond:
    topping = input(prompt)
    if topping == 'quit':
        exit_cond = False
    else:
        print("You've ordered a pizza with " + topping)
