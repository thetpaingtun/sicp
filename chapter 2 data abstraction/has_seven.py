def _has_seven(all_but_last,last):
	if last == 7 :
		return True
	if all_but_last < 10 :
		return False
	else :
		return _has_seven(n//10, n%10)



def has_seven(n):
	return _has_seven(n//10,n%10)



print(has_seven(7513))