
#global variable / not good practice

people = [
			('Joe', 78),
			('Janet', 90),
			('Brian', 67)
		   ]
		   
def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "I am {} and I am {} y/o".format(name, age)

def max_min(A):
	'''
	Returns max value - min value
	'''
	# return max(A) - max(A)
	max_, min_, = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			max_ = i
	return max_ - min_