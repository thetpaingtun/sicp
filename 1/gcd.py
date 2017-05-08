"""
GCD of two number using Euclidean Algorithm(Recursion)
"""


def min_max(a,b):
	min = a if a < b else b
	max = a if a > b else b
	return min, max

def gcd(a,b):
	min , max = min_max(a,b)
	if max % min == 0 :
		return min
	else :
		return gcd(min,max % min)




print(gcd(7, 876543))

print(gcd(54,888))