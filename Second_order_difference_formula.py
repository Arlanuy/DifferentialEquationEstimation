
'''

Arlan Vincent Uy

2015-09385

CS 131 THU

'''



'''

Juico, Jules Gerard E.

2014-40314

CS 131 THU

'''


def e_func(x):
    return math.exp(x)

def findTripleFDiff(h, find_at):
    denom = 2*(h ** 3)
    
    numer = e_func(find_at + (2*h)) - e_func(find_at - (2*h)) - (2*e_func(find_at + h)) + (2 * e_func(find_at - h))
    return numer/denom


# In[45]:

def main:
	import math

	find_at = 0
	h_values = [10**(x-10) for x in range(0, 10)]
	#print(h_values)
	x = 0.1





	for h in h_values:
	    print("at h = " + str(h) + "the estimated value of f at x = " + str(find_at) + " is " + str(findTripleFDiff(h, find_at)))

main()




