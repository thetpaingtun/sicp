# i read the implementation of scheme synatatic calculator interpreter
class Pair(object):
	def __init__(self,first,second):
		self.first = first
		self.second = second

	def __repr__(self):
		return "Pair({0},{1})".format(self.first,repr(self.second))

	def __str__(self):
		s = "(" + str(self.first)
		second = self.second
		while isinstance(second,Pair):
			s += " " + str(second.first)
			second = second.second
		if second is not nil:
			s += " . " + str(second)
		return s + ")"


	def __len__(self):
		n , second = 1 , self.second
		while isinstance(second,Pair):
			n += 1
			second = second.second
		if second is not nil :
			raise TypeError('ill-formed list')
		return n


	def __getitem__(self,k):
		if k < 0 :
			raise IndexError("index cannot be negative")
		y = self
		for _ in range(k):
			if y.second == nil:
				raise IndexError("index out of bound")
			elif not isinstance(y.second,Pair):
				raise TypeError('ill-formed list')
			y = y.second
		return y.first

	def map(self,fn):
		mapped = fn(self.first)
		if self.second is nil or isinstance(self.second,Pair):
			return Pair(mapped,self.second.map(fn))
		else :
			raise TypeError('ill-formed list')

	




class nil:
	#empty list
	def __repr__(self):
		return 'nil'

	def __str__(self):
		return "()"

	def __len__(self):
		return 0

	def __getitem__(self):
		raise IndexError("Index out of bound")

	def map(self,fn):
		return self



nil = nil()
