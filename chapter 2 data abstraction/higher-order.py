from operator import mul

def apply_to_all(map_fn,s): #s is a sequence
	return [map_fn(x) for x in s]



def keep_if(filter_fn,s):	
	return [x for x in s if filter_fn(x)]



def reduce(reduce_fn,s,initial):
	reduced = initial
	for x in s :
		reduced = reduce_fn(x,reduced)
	return reduced


s = [1,2,3,4,5]

#double every items in list
print(apply_to_all(lambda x : x *2,s))

#select even number from list
print(keep_if(lambda x : x % 2 == 0 ,s))

#reduced by multiplying items each other
print(reduce(mul,s,1))
