class Tree:
	def __init__(self,entry,branches=()):
		self.entry = entry
		for branch in branches :
			assert isinstance(branch,Tree)
		self.branches = list(branches)

	def __repr__(self):
		if self.branches :
			branch_repr = "," + repr(self.branches)
		else :
			branch_repr = ""
		return "Tree({0}{1})".format(self.entry,branch_repr)






def fib_tree(n):
	if n == 0 or n == 1 :
		return Tree(n)
	else :
		left ,right = fib_tree(n-2) ,fib_tree(n-1)
		entry = left.entry + right.entry
		return Tree(entry,(left,right))