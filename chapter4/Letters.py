class LetterIter:
	#iterator object
	def __init__(self,start='a',end='z'):
		self.next_letter = start
		self.end = end

	def __next__(self):
		if self.next_letter >= self.end:
			raise StopIteration
		result = self.next_letter
		self.next_letter = chr(ord(result)+1)
		return result



class Letters:
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __iter__(self):
		return LetterIter(self.start,self.end)

	def __len__(self):
		return max(0,ord(self.end)-ord(self.start))

	def __getitem__(self,k):
		start_ord , end_ord = ord(self.start) , ord(self.end)
		if (start_ord + k) >= end_ord :
			raise IndexError
		return chr(start_ord+k)

	def __repr__(self):
		return "Letters({},{})".format(self.start,self.end)





#short way to create iterator
def letter_gen(next_letter,end):
	while next_letter <= end :
		yield next_letter
		next_letter = chr(ord(next_letter)+1)

