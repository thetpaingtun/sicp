#-------------interval constructor and selector---------
def interval(a,b):
	assert a < b , 'lower bound cannot be bigger than upper bound'
	return [a,b]


def lower_bound(x):
	return x[0]

def upper_bound(x):
	return x[1]



# -----------------abstracting upon the interval data structure
def str_interval(x):
	"""
	string representation of the interval
	"""
	return "{0} to {1}".format(lower_bound(x),upper_bound(x))



def add_interval(x,y):
	lower = lower_bound(x) + lower_bound(y)
	upper = upper_bound(x) + upper_bound(y)
	return interval(lower,upper)


def mul_interval(x,y):
	p1 = lower_bound(x) * lower_bound(y)
	p2 = lower_bound(x) * upper_bound(y)
	p3 = upper_bound(x) * lower_bound(y)
	p4 = upper_bound(x) * upper_bound(y)
	return interval(min(p1,p2,p3,p4),max(p1,p2,p3,p4))


def div_interval(x,y):
	reciprocal_y = interval(1/upper_bound(y),1/lower_bound(y))
	return mul_interval(x,reciprocal_y)

def sub_interval(x,y):
	lower = lower_bound(x) - upper_bound(y)
	upper = upper_bound(x) -lower_bound(y)
	return interval(lower,upper)
	



#test
i = interval(3,4)
print(str_interval(i))

print(str_interval(add_interval(interval(-1,2),interval(4,8))))
print(str_interval(mul_interval(interval(-1,2),interval(4,8))))
print(str_interval(div_interval(interval(-1,2),interval(4,8))))
print(str_interval(sub_interval(interval(-1,2),interval(4,8))))




