def fib(n):
	if n == 0 or n == 1:
		return n
	else :
		return fib(n-2) + fib(n-1)



def count(f):
	def counted(*args):
		counted.count_call += 1
		return f(*args)
	counted.count_call = 0
	return counted


def memo(f):
	cache = {}
	def memoized(*args):
		if args not in cache :
			cache[args] =  f(*args)
		return cache[args]
	return memoized


