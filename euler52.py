""" Euler 52: same digits

It can be seen that the number, 125874, and its double, 251748, contain 
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.

"""

def fact(n):
	f=1
	while n>1:
		f*=n
		n-=1
	return f

def lexperm(n,lex,res=""):
	if n>=fact(len(lex)):
		raise ValueError('not that many permutations!')
	# print "finding the %d permutation out of %d for %s" % (n+1,fact(len(lex)),str(lex))
	f=fact(len(lex)-1)
	nth_element=n/f
	rem=n%f
	# print "element %d is %s" % (len(res),str(lex[nth_element]))
	res+=str(lex[nth_element])
	# print "result so far: " + res
	newlex=lex[:nth_element]+lex[nth_element+1:]
	# print "remaining: " + str(newlex)
	if len(newlex)>1:
		res=lexperm(rem,newlex,res)
		return res
	else:
		return res+str(newlex[0])
		
def allperm(lex):
	perm=[]
	for i in range(fact(len(lex))):
		perm.append(lexperm(i,lex))
	return perm

def perm_test(n):
	same_digits=allperm(str(n))
	maybe=True
	for i in range(2,7):
		if str(i*n) not in same_digits:
			maybe=False
			break
	return maybe

""" some limitations:

it has to start with a one. no other number could return 2x - 6x with the 
same number of digits. which means it must also be at least six digits long.
starting with six digits, we'll only need to test between 100000 and 166667.
"""

def perform_test(low_lim,up_lim):
	for n in range(low_lim,up_lim+1):
		if perm_test(n):
			print n
			print 2*n
			print 3*n
			print 4*n
			print 5*n
			print 6*n
			break
		else: print "%d failed" % n

"""
it's motherfucking sevenths.

142857	285714	428571	571428	714285	857142

"""

