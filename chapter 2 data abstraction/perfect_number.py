def  divisor(n):
	"""
	return a list of number that can divide n evenly
	"""
	return [1] + [x for x in range(2,n) if n % x == 0]



def find_perfect_number(n):
	"""
	to find a perfect number within a range of n
	- a perfect number is a positive number that is equal to 
	the sum of its divisor
	"""
	return [n for n in range(2,n) if sum(divisor(n)) == n]

print(divisor(400))

#perfect number within 1000
print(find_perfect_number(1000))