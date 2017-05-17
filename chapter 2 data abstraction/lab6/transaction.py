class Account(object):
	def __init__(self,name):
		self.name = name
		self.balance = 0
		self.transaction_list = []

	def deposite(self,amount):
		self.balance += amount
		self.transaction_list.append(('deposite',amount))
		return self.balance


	def withdraw(self,amount):
		if amount > self.balance :
			return 'insufficient fund'
		self.balance -= amount
		self.transaction_list.append(('withdraw',amount))
		return self.balance
	




a = Account("Thet")

print(a.deposite(1000))
print(a.withdraw(550))
print(a.transaction_list)