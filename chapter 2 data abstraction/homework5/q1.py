def make_withdraw(balance,password):
	attempt_lst = []
	def withdraw(amount,entered_password):
		nonlocal balance
		if len(attempt_lst) ==3 :
			return "Your account is locked. Attempts : [{0},{1},{2}]".format(attempt_lst[0],attempt_lst[1],attempt_lst[2])
		if entered_password ==  password:
			if amount > balance :
				return 'insufficient fund'
			balance -= amount
			return balance
		else:
			attempt_lst.append(entered_password)
			return 'incorrect password'

	return withdraw





withdraw = make_withdraw(100,'pass')
print(withdraw(23,"pa"))
print(withdraw(23,"pas"))
print(withdraw(23,"past"))
print(withdraw(23,"pase"))