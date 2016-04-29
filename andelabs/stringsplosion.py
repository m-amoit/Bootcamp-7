class StringSplosion(object):
	def __init__(self, string):
		self.string = string

	def manipulate(self):
		s = self.string
		count = 0
		l = ''
		while (count <= len(s)):
			l += s[:count]
			count +=1
		return l
