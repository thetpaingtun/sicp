class Link:
	empty = ()
	def __init__(self,first,rest=()):
		self.first = first
		assert rest is Link.empty or isinstance(rest,Link)
		self.rest = rest


	def __repr__(self):
		if self.rest :
			rest_repr = "," + repr(self.rest)
		else :
			rest_repr = ""
		return "Link({0}{1})".format(self.first,rest_repr)

	def __len__(self):
		return 1 + len(self.rest)

	def __getitem__(self,i):
		if i == 0:
			return self.first
		else :
			return self.rest[i-1]


def extend_link(s,t):
	if s is Link.empty :
		return t
	else :
		return Link(s.first,extend_link(s.rest,t))


def filter_link(f,s):
	if s is Link.empty :
		return s
	else :
		filtered = filter_link(f,s.rest)
		if f(s.first) :
			return Link(s.first,filtered)
		return filtered



def empty(s):
	return s is Link.empty


def set_contains(s,v):
	if empty(s) :
		return False
	elif s.first == v :
		return True
	else :
		return set_contains(s.rest,v)


def adjoin_set(s,v):
	if set_contains(s,v):
		return s
	else :
		return Link(v,s)



def intersect_set(set1,set2):
	in_set2 = lambda v : set_contains(set2,v)
	return filter_link(in_set2,set1)


def union_set(set1,set2):
	not_in_set2 = lambda v : not set_contains(set2,v)
	set1_not_set2 = filter_link(not_in_set2,set1)
	return extend_link(set1_not_set2,set2)








