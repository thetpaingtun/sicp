class Account:
	interest = 0.02

	def __init__(self,name):
		self.name = name
		self.balance = 0

	def depostie(self,amount):
		self.balance += amount 
		return self.balance

	def withdraw(self,amount):
		if amount > self.balance:
			return 'insufficient funds'
		self.balance = self.balance - amount
		return self.balance

	def get_interest(self):
		return self.interest





class CheckingAccount(Account):
	interest = 0.01 #overriding attr

	withdraw_fee = 1 #new attr

	def withdraw(self,amount): #overriding method
		return Account.withdraw(self,amount+self.withdraw_fee)

class Bank:
	def __init__(self):
		self.accounts = []  #composite (list of accounts)

	def open_account(self,name,balance,acc_type = Account):
		account = acc_type(name)
		account.depostie(balance)
		self.accounts.append(account)
		return account

	def pay_interest(self):
		for acc in self.accounts:
			acc.depostie(acc.balance * acc.interest)




#test
b = Bank()
thet_acc = b.open_account("thet",100,Account)
paing_acc = b.open_account("paing",10,CheckingAccount)

print(thet_acc.balance)
print(paing_acc.balance)

b.pay_interest()

print(thet_acc.balance)
print(paing_acc.balance)





