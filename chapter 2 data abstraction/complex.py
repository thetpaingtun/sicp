from math import sin,cos,pi,atan2
from fractions import gcd

def add_complex_and_rational(c,r):
	return ComplexRI(c.real+r.num/r.denom,c.imag)

def add_rational_and_complex(r,c):
	return add_complex_and_rational(c,r)
	

#Number 
class Number:
	def __add__(self,other):
		if self.type_tag == other.type_tag: #if they are the same types
			return self.add(other)
		elif (self.type_tag,other.type_tag) in self.adders:
			return self.cross_apply(other,self.adders)

	def __mul__(self,other):
		return self.mul(other)


	def cross_apply(self,other,cross_fns):
		cross_fn = cross_fns[(self.type_tag,other.type_tag)]
		return cross_fn(self,other)
		
	#adders dictionary
	adders = {('com','rat'):add_complex_and_rational,
				('rat','com'):add_rational_and_complex}




class Complex(Number):
	type_tag = 'com'
	def add(self,other):
		return ComplexRI(self.real+other.real,self.imag+other.imag)

	def mul(self,other):
		return ComplexMA(self.magnitude*other.magnitude,self.angle+other.angle)



class ComplexRI(Complex):
	def __init__(self,real,imag):
		self.real = real
		self.imag = imag

			
	@property
	def magnitude(self):
		return (self.real**2+ self.imag**2) ** 0.5

	@property
	def angle(self):
		return atan2(self.imag,self.real)

	def __repr__(self):
		return "ComplexRI({0},{1})".format(self.real,self.imag)


class ComplexMA(Complex):
	def __init__(self,magnitude,angle):
		self.magnitude = magnitude
		self.angle = angle

	@property
	def real(self):
		return self.magnitude * cos(self.angle)

	@property 
	def passimag(self):
		return self.magnitude * sin(self.angle)

	def __repr__(self):
		return "ComplexMA({0},{1})".format(self.magnitude,self.angle)






class Rational(Number):
	type_tag = 'rat'
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









