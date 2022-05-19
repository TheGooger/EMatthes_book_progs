filename = 'pi_digits.txt'

with open(filename) as file_object:
#	for line in file_object:
#		print(line.rstrip())
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())
	
print(lines)
