
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

#decorator
def count(f):
	def counted(*args):
		counted.count_call += 1
		return f(*args)
	counted.count_call = 0
	return counted




counted_fact = count(fact)
print(counted_fact(12))
print("it took {} steps".format(counted_fact.count_call))
