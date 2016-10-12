#Exercise 3.1
from random import randint
"""
Program to roll a random dice throw.
"""

class Die:
	"""
		This is the die.
	"""

	def __init__(self):
		"""
			The die object which has not been thrown yet so value will be None.
		"""
		self.value = None

	def roll(self):
		"""
			Random number between 1 - 6 to represent the sides of the die.
		"""
		self.value = randint(1,6)
			
	def __str__(self):
		"""
			Returns a string version of the die.
		"""
		if self.value:
			return "Die roll " + str(self.value)
		else:
			return "Die has not been rolled yet"

if __name__ == "__main__":

    my_die = Die()
    print my_die
    
