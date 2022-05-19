filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
	while True:
		name = input("Enter your name ('q' for quit): ")
		if name == 'q':
			break
		else:
			print("Hello, " + name.title() + "!")
			file_object.write(name.title() + "\n")
