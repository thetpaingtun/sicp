def invert(x) :
	return 1/x



def safe_invert(x):
	try :
		return invert(x)
	except ZeroDivisionError as e :
		print(e)
		return 0



