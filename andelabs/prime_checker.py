class PrimeChecker(object):
	"""Create a class PrimeChecker(number), that takes 
	in a string argument. When the instance of the class is 
	called with .is_prime() it should return true if number is a 
	prime number and false if it isn't."""
	
	def __init__(self, number=None):
		self.number = number

	def is_prime(self):
		if self.number == (''):
			return False
		number = int(self.number)

		if number < 2:
			return False
		elif number == 2:
			return True
		else:
			for n in range(2, number):
				if (number % n) == 0:
					return False
				return True

n = PrimeChecker('73')
print n.is_prime()

		