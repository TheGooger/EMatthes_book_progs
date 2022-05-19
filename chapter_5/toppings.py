#requested_toppings = ['mushrooms', 'onions', 'pineapple', 'anchovies']

#if requested_topping != 'anchovies':
#    print('Hold the anchovies!')
#if 'anchovies' in requested_toppings:
#    print('True')
#else:
#    print('False')
#requested_toppings = ['mushrooms', 'extra cheese']

#if 'mushrooms' in requested_toppings:
#    print('Adding mushrooms')
#if 'pepperoni' in requested_toppings:
#    print('Adding pepperoni')
#if 'extra cheese' in requested_toppings:
#    print('Adding extra cheese')

#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now!")
#    else:
#        print('Adding ' + requested_topping + '.')
#print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print("\nFinished making your pizza!")
else: 
    print("Are you sure you want to plane pizza?")

        
