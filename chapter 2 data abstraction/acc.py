class Account:
	def __init__(self,name):
		self.name = name
		self.balance = 0

	def withdraw(self,amount):
		if amount > self.balance:
			return 'insufficient funds'

		self.balance = self.balance - amount
		return self.balance

	def deposite(self,amount):
		self.balance += amount
		return self.balance

	def get_balance(self):
		return self.balance





a = Account("thet")
a.deposite(100)


print(a.get_balance())

