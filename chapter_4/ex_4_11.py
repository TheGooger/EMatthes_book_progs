my_pizzas = ['dodo', 'meat', 'cheese', 'shrimp', 'vagan']
friend_pizzas = my_pizzas[:]

my_pizzas.append('4 seasons')
friend_pizzas.append('fish')

print('My favorite pizzas are:')
for i in my_pizzas:
	print(i)
print('\nFriend\'s pizzas:')
for i in friend_pizzas:
	print(i)
