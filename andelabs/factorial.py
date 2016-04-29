def factorial(number):
	'''Have a function factorial(number), take the number 
	parameter been passed and return the factorial of it.
	For example: if number is 4, it should return 
	(4 * 3 * 2 * 1) which is 24.
	'''
	for i in str(number):
		if i == 1:
			return i
		product = 1
		while number > 1:
			product *= number
			number -= 1
		return product