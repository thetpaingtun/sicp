"""
Returns a dictionary of each word in message mapped
to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
"""

def counter(message):
	dict = {}
	word_list = message.split()
	for s in word_list:
		if s in dict:
			dict[s] = dict[s] + 1
		else :
			dict[s] = 1
	return dict


x = counter('to be or not to be')
print(x)


