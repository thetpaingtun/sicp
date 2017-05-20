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



#if set is in ordered
#this is faster
def intersect_set(set1 , set2):
	if empty(set1) or empty(set2):
		return Link.empty
	else :
		e1 , e2 = set1.first , set2.first
		if e1 == e2 :
			return Link(e1,intersect_set(set1.rest,set2.rest))
		elif e1 < e2 :
			return intersect_set(set1.rest,set2)
		elif e2 < e1 :
			return intersect_set(set1,set2.rest)











