import has_seven
"""
The ping-pong sequence counts up starting from 1 and is always either 
counting up or counting down. At element k, the direction switches 
if k is a multiple of 7 or contains the digit 7. The first 30 elements of 
the ping-pong sequence are listed below, with direction swaps marked using 
brackets at the 7th, 14th, 17th, 21st, 27th, and 28th elements:

1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
"""

#iteratiive version
def ping_pong_iter(n):
	current_state = True
	k = 1
	value = 0
	while  k <= n :
		value = count_up_and_down(value,current_state)
		if has_seven.has_seven(k) or k % 7 == 0 :
			current_state = not (current_state)  #swap direction
		k  = k + 1
	return value

def count_up_and_down(n,up):
	if up : 
		return n + 1
	else :
		return n - 1
	
#recursive version
def _pingpong(n,k,value,up):
	if has_seven.has_seven(k) or k % 7 == 0 :
		up = not up
	if k == n :
		return value
	return _pingpong(n,k+1,count_up_and_down(value,up),up)




def pingpong(n):
	return _pingpong(n,1,1,True)
	



# print(ping_pong_iter(27))
# print(ping_pong_iter(68))
# print(ping_pong_iter(71))
# print(ping_pong_iter(69))
# print(ping_pong_iter(70))
# print(ping_pong_iter(71))



print("27=>{}".format(pingpong(27)))
print("68=>{}".format(pingpong(68)))
print("71=>{}".format(pingpong(71)))
print("69=>{}".format(pingpong(69)))
print("70=>{}".format(pingpong(70)))

