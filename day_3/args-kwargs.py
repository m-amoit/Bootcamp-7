#Unpacking
def hello(name, age, class_=''):
	'''
	Trying args and kwargs
	'''
	if class_ != 0:
		return "I am {}, and I am {} y/o, and {} class".format(name, age, class_)
	return "I am {}, my age is {}".format(name, age)
	

people = [("Jane", 23, 'High'),
			("Joe", 25, 'Low'),
			("Brian", 60),
			("Betty", 45),
			]

#for name, age in people:
#	print hello(name, age)
#for a in people:
#	print hello(*a)
def super_sum(a, b, *args):
	'''
	Takes in variable number of items and returns
	the sum. e.
	'''
	total = 0
	for i in args:
		total += i
	return total + a +b

# print super_sum(10, 20)
# print super_sum(1, 4, 5, 7)
# a = [10, 40, 60]
# print super_sum(*a)

def hello_again(**kwargs):
	return "I am {}, my age is {}".\
	format(kwargs['name'], kwargs['age'])

# print hello_again(name='Joe', age=20)
# print hello_again(age=15, name='Peter')

other_people = [{'name': 'Joe', 'age':98},
				{'name': 'Jane', 'age':60},
				{'name': 'Trump', 'age':23}]

Joe = {'name':'Joe', 'age':98}

# print hello_again(**Joe)
# print hello_again(name='Joe', age=98)


for person in other_people:
	print hello_again(**person)