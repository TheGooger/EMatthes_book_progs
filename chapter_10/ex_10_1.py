with open('learning_python.txt') as file_object:
	lines = file_object.readlines()
	message = file_object.read()
	print(message)
#	for line in file_object:
#		print(line.rstrip())
	
for line in lines:
	print(line.rstrip())
