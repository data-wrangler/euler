"""Euler 24: lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is 
one possible permutation of the digits 1, 2, 3 and 4. If all of the 
permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012,021,102,120,201,210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Is there a deterministic algorithm to produce lexicographic permutations?

012 001
021 010
102 011
120 100
201 101
210 110

1234
1243
1324
1342
1423
1432

012345
012354
012435
012453

the number of permutations is determined by factorials.
there are 2 ways to arrange 2 things: 01, 10
when we add a third, there are three ways to put that in front, and two ways
to arrange the remaining two behind them: hence, six
when we add a fourth, there are four ways, and six each for the remaining,
etc.

there's a way to do this by essentially using the factorials as bases and 
working back through.
9!=362880, so up until that permutation the first digit is always zero. 
Then, the remaining digits will be arranged behind it. The millionth perm-
utation falls somewhere between 3-4, so the first digit should be 2.
"""

olex=[0,1,2,3,4,5,6,7,8,9]
lex=[0,1,2,3,4,5,6,7,8,9]

def fact(n):
	f=1
	while n>1:
		f*=n
		n-=1
	return f

def lexperm(n,mylex,res=""):
	lex=mylex
	print "finding the %d permutation out of %d for %s" % (n,fact(len(lex)),str(lex))
	if n>fact(len(lex)):
		raise ValueError('not that many permutations!')
	f=fact(len(lex)-1)
	nth_element=n/f
	rem=n%f
	print "element %d is %s" % (len(res),str(lex[nth_element]))
	res+=str(lex[nth_element])
	print "result so far: " + res
	del(lex[nth_element])
	print "remaining: " + str(lex)
	if len(lex)==1:
		print res+str(lex[0])
	else:
		lexperm(rem,lex,res)

