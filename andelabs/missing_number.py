def find_missing(A=None, B=None):
	'''
	You are presented with two arrays, all containing 
	positive integers. One of the arrays will have one 
	extra number, see below:
	[1,2,3] and [1,2,3,4] should return 4
	[4,66,7] and [66,77,7,4] should return 77
	'''
	if A !=None and B!=None:

		c = set(A).symmetric_difference(B)
		for i in list(c):
			return i

	return 0
