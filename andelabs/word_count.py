import re

def words(A):
	count = dict ()
	for i in A.split():
		if i is '':
			continue
		else:
			if i not in count:
				count[i] = 1
			else:
				count[i] = count [i] + 1
	return count


		

