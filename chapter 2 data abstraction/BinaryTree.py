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



class BinaryTree(Tree):
	empty = Tree(None)
	empty.is_empty = True
	def __init__(self,entry,left=empty,right=empty):
		Tree.__init__(self,entry,(left,right))
		self.is_empty = False


	@property
	def left(self):
		return self.branches[0]

	@property
	def right(self):
		return self.branches[1]





def set_contains(s,v):
	if s.is_empty : # u got the end of the tree
		return False 
	elif s.entry == v :
		return True
	elif s.entry < v :
		return set_contains(s.right,v)
	elif s.entry > v :
		return set_contains(s.left,v)


def adjoin(s,v):
	if s.is_empty :
		return BinaryTree(v)
	elif s.entry == v :
		return s 
	elif s.entry < v :
		return BinaryTree(s.entry,s.left,adjoin(s.right,v))
	elif s.entry > v :
		return BinaryTree(s.entry,adjoin(s.left,v),s.right)









 