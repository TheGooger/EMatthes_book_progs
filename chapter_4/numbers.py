numbers = list(range(1,6))
print(numbers)

#even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

#squares
squares = []
for i in range(1,11):
	squares.append(i**2)
print(squares)
print('\nMinimum: ' + str(min(squares)))
print('\nMaximum: ' + str(max(squares)))
print('\nSum: ' + str(sum(squares)))

#list comprehension
c_squares = [i**2 for i in range(1,11)]
print(c_squares)
