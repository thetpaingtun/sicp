def has_seven(n):
	all_but_last , last = n//10 , n % 10
	if last == 7 : 			  # found 7 , stop the recursion
		return True
	elif all_but_last == 0 :  #out of number,stop the recursion
		return False
	else:
		return has_seven(all_but_last) 



# print(has_seven(47444))
# print(has_seven(663444))

