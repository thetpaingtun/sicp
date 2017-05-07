"""
	is even using recursion
"""

def is_even(n):
	if n == 0 :
		return True
	elif n-1 == 0: #mean n is 1
		return False
	else:
		return is_even((n-1)-1)
	


print(is_even(1003))