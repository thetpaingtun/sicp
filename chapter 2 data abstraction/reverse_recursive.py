def reverse_recursive(lst):
	if not lst:
		return []
	return reverse_recursive(lst[1:]) + [lst[0]]



#iterative version
def reverse_iter(lst):
	new =[]
	while lst:
		new += [lst[-1]]
		lst = lst[:-1]
	return new 



lst = [1,2,3,4]
print(reverse_recursive(lst))
print(reverse_iter(lst))