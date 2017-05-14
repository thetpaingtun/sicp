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




def make_joint(withdraw,old_pass,new_pass):
	if (type(withdraw(0,old_pass)))== str :
		return 'incorrect password'

	else :
		def can_withdraw(amount,entered_password):
			if entered_password == old_pass or entered_password == new_pass:
				return withdraw(amount,old_pass)
			else :
				return withdraw(amount,entered_password)
		return can_withdraw
		





a = make_withdraw(100,'pass')
j = make_joint(a,'pass','sec')






