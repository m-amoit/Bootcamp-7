def funky(a,b):	
	'''
	A function that will add numbers and concatenate strings, lists and dictionaries
	'''
	if type(a) == type(b):
		try:
			return a + b
		except TypeError:
			return dict(a.items() + b.items())

	elif type(a)==int and type(b)==float or type(a)==float and type(b)==int:
		return (a+b)
	else:
		return 'Type Error'


