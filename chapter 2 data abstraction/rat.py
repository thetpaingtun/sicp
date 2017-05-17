from fractions import gcd
from Number import Number

class Rational(Number):
	def __init__(self,num,denom):
		g = gcd(num,denom)
		self.num = num // g
		self.denom = denom // g

	def __repr__(self):
		return 'Rational({0},{1})'.format(self.num,self.denom)

	def __str__(self):
		return "{0}/{1}".format(self.num,self.denom)


	def add(self,other):
		nx , dx = self.num , self.denom
		ny , dy = other.num , other.denom
		return Rational(nx*dy+ny*dx,dx*dy)


	def mul(self,other):
		num =  self.num * other.num
		denom = self.denom * other.denom
		return Rational(num,denom)