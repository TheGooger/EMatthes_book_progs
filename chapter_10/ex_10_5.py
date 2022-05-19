filename = 'programming.txt'

with open(filename, 'a') as file_object:
	while True:
		reason = input("Why do you love programming ('q' for quit)? ")
		if reason == 'q':
			break
		else:
			file_object.write(reason + "\n")
