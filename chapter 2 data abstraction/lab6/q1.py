class Account(object):
	interest = 0.02
	def __init__(self,name):
		self.name = name
		self.balance = 0

	def deposite(self,amount):
		self.balance += amount
		print("yes")
		return self.balance





a = Account("Billy")
print(a.name)

Account.interest = 0.03
print(a.interest)
print(a.deposite(100))
print(a.balance)

a.interest = 9001

print(Account.interest)