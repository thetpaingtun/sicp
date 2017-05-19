from math import sqrt

def is_divisible(n,k):
	return n % k == 0

def fact(n):
	total = 0
	for k in range(1,n+1):
		if is_divisible(n,k):
			total += 1
	return total


def count(f):
	def counted(*args):
		counted.count_call += 1
		return f(*args)
	counted.count_call = 0
	return counted


def fact_fast(n):
	sqrt_n = sqrt(n)
	k , total = 1 , 0
	while k < sqrt_n:
		if is_divisible(n,k):
			total += 2
		k += 1
	if k * k == n :
		total += 1
	return total



 


