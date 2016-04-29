def string_length(A):

	'''You are presented with a string or a collection of strings
	Your function should return the length of the string, or 
	strings in a list

	['Fairy', 'tale'] should return [5, 4]

	'C-sharp' should return [7]'''
	l = []
	if type(A) == str:
		l.append(len(A))
		return l
	if type(A) == list:
		for i in A:
			l.append(len(i))
		return l


