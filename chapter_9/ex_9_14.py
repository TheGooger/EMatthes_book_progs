from random import randint

class Die():
	"""Имитирует бросок кубика."""
	
	def __init__(self, sides=6):
		"""Инициализирует количество сторон кубика."""
		self.sides = sides
		
	def roll_die(self):
		"""Выводит случайное число на грани кубика."""
		r_v = randint(1, self.sides)
		print("The result of rolling die is " + str(r_v) + ".")
	

die_0 = Die()
die_1 = Die(10)
die_2 = Die(20)
for i in range(0,10):
	print(str(i) + ")")
	die_2.roll_die()
