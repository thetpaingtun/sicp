def fact(n):
	assert n >= 0 , 'cannot be negative'
	if n < 2 :
		return 1
	else :
		return n * fact(n-1)



fact(0)
print(fact(3))