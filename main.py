def decorator(f):
	def wrapper(*args):
		print('before')
		f(*args)
		print('after')
	return wrapper





@decorator
def print_name(name):
	print(name)





print_name("thet")