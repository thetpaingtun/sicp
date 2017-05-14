from q3 import VendingMachine
from operator import add 


class MissManners:
	def __init__(self,obj):
		self.obj = obj

	def ask(self,*args):
		first_part = len(args[0].split())
		please_part =  args[0].split()[0] if first_part >= 1  else 0
		method_part  = args[0].split()[1] if first_part == 2 else 0
		arguments = args[1:]

		if  please_part != "please":
		 	return 'You must learn to say please first'
		if first_part > 2 :
			remove_please_part =  args[0].split()[1:]
			return 'Thanks for asking, but I know not how to {}'.format(" ".join(remove_please_part))
		if first_part < 2 :
			return 'What do u want me to do?You did not put any command'
		
		if not hasattr(self.obj,method_part):
			return 'Thanks for asking, but I know not how to {}'.format(method_part)


		call_string = '{0}.{1}('.format(self.obj,method_part)

		for s in arguments:
			call_string += '{},'.format(str(s))

		# call_string = call_string[:-1]

		call_string += ')'
		print(call_string)
		eval(call_string)
		

		

	   


		 








v = VendingMachine('candy',10)

m = MissManners(v)

print(m.ask("please vend"))

# print(eval('v.vend()'))


