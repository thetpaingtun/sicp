#tree implementation
def tree(root,branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root] + branches


def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]



def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if  not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

# -----------------------tree processing ---------------------
def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		counts = [count_leaves(b) for b in branches(tree)]
		print("count : {}".format(counts))
		return sum(counts)


def leaves(tree):
	if is_leaf(tree): 
		return [root(tree)]
	else:
		counts = [leaves(b) for b in branches(tree)]
		print(counts)
		return sum(counts,[])


# -----------------------tree processing ---------------------


#----------------------fib tree ----------------------------

#fib_tree
def fib_tree(n):
	if n == 0 or n == 1:
		return tree(n)
	else:
		left , right = fib_tree(n-2) , fib_tree(n-1) #recursive call occured here
		fib_n = root(left) + root(right)
		return tree(fib_n,[left,right])

#----------------------fib tree ----------------------------

#----------------------partition tree ----------------------------
def partition_tree(n,m):
	if n == 0 :
		return tree(True)
	elif n < 0 or m == 0 :
		return tree(False)
	else:
		left = partition_tree(n-m,m)
		right = partition_tree(n,m-1)
		return tree(m,[left,right])


def print_parts(tree , partition=[]):
	if is_leaf(tree):
		if root(tree):
			print(partition)
	else:
		left , right = branches(tree)
		print_parts(left,partition+[root(tree)])
		print_parts(right,partition)

#----------------------partition tree ----------------------------






