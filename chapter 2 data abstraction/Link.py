class Link:
	empty = ()
	def __init__(self,first,rest=empty):
		assert rest is Link.empty or isinstance(rest,Link)
		self.first = first
		self.rest = rest

	def __getitem__(self,i):
		if i == 0:
			return self.first
		else :
			return self.rest[i-1]


	def __len__(self):
		return 1 + len(self.rest)

	def __repr__(self):
		if self.rest :
			rest_str = ',' + repr(self.rest)
		else :
			rest_str = ""
		return 'Link({0}{1})'.format(self.first,rest_str)


def extend_link(s,t):
	if s is Link.empty:
		return t
	else :
		return Link(s.first,extend_link(s.rest,t))



def map_link(f,s):
	if s is Link.empty :
		return s
	else :
		return Link(f(s.first),map_link(f,s.rest))



def filter_link(f,s):
	if s is Link.empty :
		return s
	else :
		filtered = filter_link(f,s.rest)
		if f(s.first) :
			return Link(s.first,filtered)
		return filtered



def join_link(s,seperator):
	if s is Link.empty :
		return ""

	elif s.rest is Link.empty :
		return str(s.first)

	else :
		return str(s.first) + seperator + join_link(s.rest,seperator)











