class Link:
	empty = ()
	def __init__(self,first , rest =()):
		self.first = first
		self.rest = rest

	def __repr__(self):
		if self.rest :
			rest_str = ',' + repr(self.rest)
		else :
			rest_str = ''
		return "Link({0}{1})".format(self.first,rest_str)




class Stream:
	class empty :
		def __repr__(self):
			return 'Stream.empty'
	empty = empty()
	def __init__(self,first,compute_rest= lambda:empty):
		assert callable(compute_rest) , 'compute_rest must be callable'
		self.first = first
		self._compute_rest = compute_rest


	@property
	def rest(self):
		if self._compute_rest is not None:
			self._rest = self._compute_rest()
			#self._compute_rest = None
		return self._rest

	def __repr__(self):
		return "Stream({0},<....>)".format(repr(self.first))



def integer_stream(first):
	def compute_rest():
		return integer_stream(first+1)
	return Stream(first,compute_rest)




def first_k(s,k):
	#return the first k element of the stream
	if k == 0 :
		return []
	return [s.first] + first_k(s.rest,k-1)



def square_stream(s):
	squared = s.first * s.first 
	return Stream(squared,lambda:square_stream(s.rest))


def add_stream(s,t):
	added = s.first + t.first
	return Stream(added,lambda:add_stream(s.rest,t.rest))



def map_stream(fn,s):
	if s is Stream.empty:
		return s
	def compute_rest():
		return map_stream(fn,s.rest)
	return Stream(fn(s.first),compute_rest)


def filter_stream(fn , s):
	if s is Stream.empty :
		return s
	def compute_rest():
		return filter_stream(fn,s.rest)

	if fn(s.first) :
		return Stream(s.first,compute_rest)

	else :
		return compute_rest()







