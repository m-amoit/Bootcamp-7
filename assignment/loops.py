f = [(10, 20, 30), (10, 40), (4, 5, 50)]
'''
x:10, y:20, z:30
x:10, y:40, 
x:4, y:5, z: 50
'''

for i in f:
	if len(i)==3:
		print "x:{} y:{} z:{}".format(*i)
	print "x:{} y:{}".format(*i)