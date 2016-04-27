def data_type(x):
	'''
	Takes in an argument, x:
		- For a integer, return x**2
		- For a float, return x/2
		- For a string, return "hello" + x
		- For a boolean, return "boolean"
		- For a long, return "long"
	'''
	if type(x) == int:
		return x**2
	elif type(x) == float:
		return x/2
	elif type(x) == str:
		return "hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"
	else:
		pass



