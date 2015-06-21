"""
euler 41: pandigital primes

We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. For example, 2143 
is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

""" 
Brute force 1:
find all pandigital permutations
test for primality
--> n!
2 2
3 6
4 24
5 120
6 720
7 5,040
8 40,320
9 362,880

Brute Force 2:
find all primes with n digits
test for pandigitalness
--> primes with n digits or less:
2 25
3 168	 
4 1,229	 
5 9,592	 
6 78,498	 
7 664,579	 
8 5,761,455	 
9 50,847,534

we can further limit 1 by skipping anything with an even last digit, 
cutting testing in half.

"""
import itertools
import math
import time

# find all permutations of a set

def all_combinations(letterset,permset=[]):
	if len(permset)==0: permset=letterset
	for i in range(len(letterset)-1):
		permset=list(itertools.chain.from_iterable(map(lambda l:map(lambda p:p+l,permset),letterset)))
	return permset

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
		
def pList(n):
	s=time.time()
	pl=[2,3,5,7]
	i=11
	while max(pl)<n:
		j=0
		maybe=True
		while pl[j]<=math.sqrt(i):
			if i%pl[j]==0:
				maybe=False
				break
			j+=1
		if maybe:
			pl.append(i)
			i=max(pl)+2
		else:i+=2
	took=time.time()-s
	print "it took "+ str(took)
	return pl

def intersect(a,b):
	c=[int(val) for val in a if int(val) in b]
	return c

'''
# Test 1
n=5
primelist=pList(10**n)
digitlist=[str(i+1) for i in range(n)]
permlist=[lexperm(i,digitlist) for i in range(fact(n))]
reslist=intersect(permlist,primelist)
print reslist
'''

"""
it takes 30 seconds to generate a list for 5-digit vs .5s for 4.
I'll do six, but it'll take forever. this is inefficient.
"""
pl=pList(10000)

def prime_test(i):
	j=0
	maybe=True
	while pl[j]<=math.sqrt(i):
		if i%pl[j]==0:
			maybe=False
			break
		j+=1
	return maybe


n=9
digitlist=[str(i+1) for i in range(n)]
permlist=[lexperm(i,digitlist) for i in range(fact(n))]
reslist=[]
for perm in permlist:
	if prime_test(float(perm)):
		reslist.append(int(perm))
print reslist