class Rational:
	"""A class that represent rational number"""
	def __init__(self,n,d):
		self.numberator = n
		self.denom = d

	def __repr(self):
		return 'rational({0},{1})'.format(self.numberator,self.denom)

	def __str__(self):
		return '{0}/{1}'.format(self.numberator,self.denom)

	@property
	def float_value(self):
		return self.numberator/self.denom





r = Rational(1,2)

print(r.float_value)