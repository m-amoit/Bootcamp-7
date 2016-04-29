def reverse_string(string):
	'''
	You are to write a function, reverse_string(string), 
	that returns the reverse of the string provided. If the 
	reverse of the string is the same as the original string, 
	as in the case of palindromes, return true instead.
	'''
	if string == '':
		return None

	if string == string[::-1]:
		return True
	return string[::-1]