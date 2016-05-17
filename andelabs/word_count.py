import re

def words(A):
	count = dict ()
	x = re.findall('\S+', A) # All none whitespace characters, one or more
	for i in x:
		count[i] = count.get(i, 0) + 1

	return count

	
	# for i in A.split():
	# 	if i is '':
	# 		continue
	# 	else:
	# 		if i not in count:
	# 			count[i] = 1
	# 		else:
	# 			count[i] = count [i] + 1
	# return count


		

