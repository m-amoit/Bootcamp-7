
def fizz_buzz(i):
	if i % 15 == 0:
		return 'FizzBuzz'
	elif i % 5 == 0:
		return 'Buzz'
	elif i % 3 == 0:
		return 'Fizz'
	return i