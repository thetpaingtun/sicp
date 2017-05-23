# just repeat link class to practice
class Link:
	empty  = ()
	def __init__(self,first,rest = empty):
		self.first = first
		assert rest is Link.empty or isinstance(rest,Link)
		self.rest = rest 

	def __getitem__(self,i):
		if i == 0 :
			return self.first
		else :
			return self.rest[i-1]

	def __repr__(self):
		if self.rest :
			rest_str = ',' + repr(self.rest)
		else :
			rest_str = ""

		return 'Link({0}{1})'.format(self.first,rest_str)

	def __len__(self):
		if self is Link.empty :
			return 0
		else :
			return 1 + len(self.rest)

def extend_link(s,t):
	if s is Link.empty :
		return t 
	else :
		return Link(s.first,extend_link(s.rest,t))


def map_link(fn , s):
	if s is Link.empty :
		return s 
	else :
		return Link(fn(s.first) , map_link(fn, s.rest))


def filter_link(fn,s):
	if s is Link.empty :
		return s
	else :
		filtered = filter_link(f,s.rest)
		if (fn(s.first)):
			return Link(s.first,filtered)
		return filtered


def join_link(s,seperator):
	if s is Link.empty:
		return ""
	elif s.rest is Link.empty:
		return str(s.first)
	else :
		return str(s.first) + seperator + join_link(s.rest,seperator)











