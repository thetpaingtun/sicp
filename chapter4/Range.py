class Range:
	def __init__(self,start,end=None):
		if end is None :
			start , end = 0 , start
		self.start = start
		self.end = end

	def __len__(self):
		return max(0,self.end - self.start)


	def __getitem__(self,k):
		if k > len(self):
			raise IndexError("index out of bound error")
		return self.start + k


	def __repr__(self):
		return "Range({0},{1})".format(self.start,self.end)


class RangeIter:
	def __init__(self,start,end):
		self.next_num = start
		self.end = end

	def __next__(self):
		if self.next_num >= self.end:
			raise StopIteration
		result = self.next_num
		self.next_num += 1
		return result