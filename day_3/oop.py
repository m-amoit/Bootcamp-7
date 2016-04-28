from person import Person
from kenyan import Kenyan
# Instance vs class variables

p = Person('Joe', 23)
# print p


p2 = Person('Jane', 23)
p3 = Person('George', 40)

# print p.say_hello()

a = [('Jane', 23), ('Joe', 50), ('Jackie', 34), ('Jacob', 23), ('Jee', 18), ('Josh', 60)]

b = []
for name, age in a:
	person = Person(name, age)
	b.append(person)

# for person in b:
	# print person.say_hello()


k = Kenyan('Miguna', 20)

k.probe(True)

print "Is {} corrupt? {}".format(k.name, k.is_corrupt())



# print b



