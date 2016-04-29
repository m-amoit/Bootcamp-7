def find_max_min(A):
	l = []
	max_, min_ = (A[0], A[0])
	
	for i in A:
		if i > max_:
			max_ = i
		
		if i < min_:
			min_ = i
	
	l.append(min_)
	l.append(max_)
	return l

print find_max_min([87, 4, 45, 2, 20, 98])
