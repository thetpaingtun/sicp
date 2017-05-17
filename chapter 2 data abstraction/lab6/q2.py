class Person(object):

	"""docstring for Person"""
	def __init__(self, name):
		self.name = name
		self.repeat_text = "starts at whatever value you'd like I squirreled it away before it could catch on fire."


	def say(self,stuff):
		self.repeat_text = stuff
		return self.repeat_text

	def ask(self,stuff):
		q = "Would you please {}?".format(stuff)
		self.repeat_text = q
		return self.repeat_text

	def greet(self):
		return self.say("Hello my name is "+self.name)

	def repeat(self):
		return self.say(self.repeat_text)



#test
steven = Person("Steven")
print(steven.repeat())
print(steven.say("hello"))
print(steven.repeat())
print(steven.greet())
print(steven.repeat())
print(steven.ask("preserve abstraction barrier"))
print(steven.repeat())



	
		