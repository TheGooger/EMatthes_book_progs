pizzas = ['dodo', 'meat', 'cheese', 'shrimp', 'vagan']
print('The first three items in the list are:')
for i in pizzas[:3]:
	print(i.title())
print('\nThree items frome the middle of the list are:')
for i in pizzas[1:4]:
	print(i)
print('\nThe last three items:')
for i in pizzas[-3:]:
	print(i)
