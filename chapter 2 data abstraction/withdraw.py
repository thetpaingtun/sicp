def initailize_acc(balance):
	def withdraw(withdraw_amount):
		nonlocal balance
		if withdraw_amount > balance:
			return 'insufficient funds'
		balance = balance - withdraw_amount
		return balance
	return withdraw



#using mutable value
# def initailize_acc(balance):
# 	b = [balance]
# 	def withdraw(amount):
# 		if b[0] < amount:
# 			return 'insufficient funds'
# 		b[0] = b[0] - amount
# 		return b[0]
# 	return withdraw


 


withdraw = initailize_acc(100)
print(withdraw(25))
 