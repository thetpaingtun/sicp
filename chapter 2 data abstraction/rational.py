"""
Rational arithmetic
"""

from fractions import gcd

#Arithmetic
def add_rational(x,y):
	return rational((numerator(x)*denom(y))+(numerator(y)*denom(x)),denom(x)*denom(y))

def mul_rational(x,y):
	return rational(numerator(x)*numerator(y),denom(x)*denom(y))

def rational_are_equal(x,y):
	return numerator(x) * denom(y) == numerator(y) * denom(x)


def print_rational(x):
	print("{}/{}".format(numerator(x),denom(x)))
	


#constructors and selector

def rational(n,d):
	g = gcd(n,d)
	return [n//g,d//g]

def numerator(x):
	return x[0]

def denom(x):
	return x[1]




"""
2nd implementation of rational number using higher order function 
instead of list

def rational(n,d):
	g = gcd(n,d)
	n , d = n // g , d // g
	def select(name):
		if name == 'n':
			return n
		elif name == 'd':
			return d
	return select

def numerator(x):
	return x('n')

def  denom(x):
	return x('d')

"""


a = rational(1,2)
b = rational(2,4)


print(rational_are_equal(a,b))

print_rational((add_rational(a,b)))

print_rational((mul_rational(a,b)))

print_rational(b)

