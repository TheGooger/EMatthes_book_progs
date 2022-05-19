number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("The number " + str(number) + " is even.")
else:
	print("The number " + str(number) + " is odd.")
