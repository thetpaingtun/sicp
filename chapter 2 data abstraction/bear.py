class Bear:
	def __init__(self):
		self.__repr__ = lambda : 'oski'
		self.__str__ = lambda : 'oski the bear'

	def __repr__(self):
		return 'Bear()'
	def __str__(self):
		return 'a bear'



def repr(obj):
	return type(obj).__repr__(obj)


def str(obj):
	if hasattr(type(obj),'__str__'):
		return type(obj).__str__(obj)
	else:
		return repr(obj)


def print_bear():
	oski = Bear()
	print(oski)
	print(str(oski))
	print(repr(oski))
	print(oski.__repr__())
	print(oski.__str__())



print_bear()