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





class BadBankAccount(Account):
	def withdraw(self,amount):
		if self.overdrawn :
			return "You have been overdrawn put some money first to deposite"
	
		self.balance -= amount
		return self.balance

	@property
	def overdrawn(self):
		if self.balance < 0:
			return True
		else:
			return False




#test
b = BadBankAccount("Thet")

print(b.name)
print(b.deposite(100))
print(b.withdraw(10))
print(b.overdrawn)
print(b.withdraw(100))
print(b.overdrawn)
print(b.withdraw(100))
print(b.deposite(20))
print(b.overdrawn)
		