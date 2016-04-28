def super_sum(*args):
	'''
	Returns a sum of numbers
	e.g 
		
		super_sum() ==> "Please enter number"
		super_sum(1,2,3) ==> 6
		super_sum('string') ==> 0
		super_sum([1,2,3]) ==> 6
		super_sum([10], [20, 30]) ==> 60
	
	'''
	
	total = 0
	if not args:
		return 0
	
	for arg in args:
		if type(arg) == list:
			total += sum(arg)
		
		elif type(arg) == str:
			return 0
		
		else: 
			total += arg
	
	return total
