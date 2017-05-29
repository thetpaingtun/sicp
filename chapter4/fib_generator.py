def fib_generator():
	yield 0
	prv , cur = 0 , 1
	while True:
		yield cur
		prv , cur = cur , prv + cur