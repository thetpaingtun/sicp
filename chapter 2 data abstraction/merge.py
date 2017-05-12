#merge two sorted list into a new sorted list
def merge(lst1,lst2):
	if not lst1 or not lst2:
		return lst1 + lst2
	elif lst1[0] < lst2[0]:
		return [lst1[0]]+merge(lst1[1:],lst2) 
	else:
		return [lst2[0]] + merge(lst1,lst2[1:])



#iterative version
def merge_iter(lst1,lst2):
	new = []
	while lst1 and lst2:
		if lst1[0] < lst2[0]:
			new = new + [lst1[0]]
			lst1 = lst1[1:]
		else:
			new = new + [lst2[0]]
			lst2 = lst2[1:]

	if lst1:
		new += lst1
	else : 
		new += lst2
	return new





lst1 = [1,3,5]
lst2 = [2,4,6]



# lst1 = []
# lst2 = []


print(merge(lst1,lst2))
print(merge_iter(lst1,lst2))