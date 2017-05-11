"""
G(n) = n,                                       if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3

"""

#recursion version 
def g(n):
	if n <= 3 :
		return n
	else :
		return g(n-1) + 2 * g(n-2) + 3 * g(n-3)


#iteration version 
def g_iter(n):
	ans = 0
	first_part = n
	secon_part = n 
	third_part = n
	first_part_total = 0
	second_part_total = 0
	third_part_total = 0

	if n <= 3 :
		ans = n
	else:
		while n>3:
			first_part = first_part-1
		first_part_total 



#test using recursion versoion

print(g(0))
print(g(1))
print(g(2))
print(g(3))
print(g(4))
print(g(5))
