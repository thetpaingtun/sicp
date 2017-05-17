class Number:
	def __add__(self,other):
		if self.type_tag == other.type_tag: #if they are the same types
			return self.add(other)
		elif (self.type_tag,other.type_tag) in self.adders
			return self.cross_apply(other,self.adders)

	def __mul__(self,other):
		return self.mul(other)


	def cross_apply(self,other,cross_fns):
		cross_fn = cross_fns[(self.type_tag,other.type_tag)]
		return cross_fn(self,other)
		


	#adders dictionary
	adders = {}