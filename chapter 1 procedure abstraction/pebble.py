"""
As another example of mutual recursion, consider a two-player game in 
which there are n initial pebbles on a table. The players take turns, 
removing either one or two pebbles from the table, and the player who removes 
the final pebble wins. Suppose that Alice and Bob play this game, each using 
a simple strategy:

Alice always removes a single pebble
Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise

Given n initial pebbles and Alice starting, who wins the game?

"""

def _is_even(n):
	return n % 2 == 0


def alice_plays(n):
	n = n -1
	if n == 0:
		print("Alice wins!")
	else :
		bob_plays(n)


def bob_plays(n):
	n = n - 2 if (_is_even(n)) else n -1 
	if n == 0 :
		print("Bob wins!")
	else:
		alice_plays(n)




# if the pebble is 4 and Alice starts playing 
alice_plays(4)


bob_plays(6)


	
