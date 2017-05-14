class VendingMachine:
	def __init__(self,product_name,product_price):
		self.product_name = product_name
		self.product_price = product_price
		self.quantity = 0
		self.balance = 0

	def restock(self,quantity):
		self.quantity = quantity
		return 'Current {0} stock : {1}'.format(self.product_name,self.quantity)


	def deposite(self,amount):
		assert amount > 0,"Cannot deposite the amount less than $1"
		if self.quantity == 0:
			return 'Machine is out of stock.Here is your ${}'.format(amount)
		self.balance += amount
		return 'Current balance : ${}'.format(self.balance)

	def vend(self):
		if self.quantity == 0:
			return 'Machine is out of stock'

		if self.balance < self.product_price :
			return 'You must deposite ${} more'.format(self.product_price-self.balance)

		if self.balance == self.product_price :
			self.balance = 0 # balance reset to 0
			self.quantity -= 1
			return 'Here is your {}'.format(self.product_name)

		if self.balance > self.product_price :
			change = self.balance - self.product_price
			self.balance = 0
			self.quantity -= 1
			return 'Here is your {0} and ${1} change'.format(self.product_name,change)



#test
# v = VendingMachine('candy',10)
# print(v.vend())
# print(v.restock(2))
# print(v.vend())
# print(v.deposite(7))
# print(v.vend())
# print(v.deposite(5))
# print(v.vend())
# print(v.deposite(10))
# print(v.vend())
# print(v.deposite(15))
# print(v.restock(2))
# print(v.deposite(20))
# print(v.vend())








