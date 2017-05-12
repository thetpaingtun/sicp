from math import sqrt

#i replace this function with lambda expression
# def is_square(n):
# 	return float(sqrt(n)) == int(sqrt(n))



def perfect_square(lst):
	return [i for i in lst if (lambda x : float(sqrt(x))== int(sqrt(x)))(i)]




lst1 = [49, 8, 2, 1, 102]
lst2 = [500,30]
lst3 = [9,16,25,41]


print(perfect_square(lst1))
print(perfect_square(lst2))
print(perfect_square(lst3))