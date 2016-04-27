class Person(object):
	people_count = 0 #Class variable
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "<object:{}, {}>".format(self.name, self.age)

	def say_hello(self):
		return "Hello, I'm {} and {} y/o".format(self.name, self.age)

#end of class
