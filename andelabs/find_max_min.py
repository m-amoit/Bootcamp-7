		

def find_max_min(A):
	l = []
	max_, min_ = (A[0], A[0])
	
	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			min_ = i
	
	if min_ == max_:
		return [len(A)]
	else:
		l.append(min_)
		l.append(max_)
	
	return l
	



