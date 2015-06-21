""" Euler 32: Pandigital Numbers

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39*186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

This includes some thoughts on lexicographic permutations from 24.

Brute force gets ugly and fast. Either take all possible strings of 10 digits
(there are 10!=3.6M of them) and test inserting times and equals and testing for
truth, or start multiplying numbers and see whether they return the right 
set of digits.

We can limit our search to only those numbers who could possibly return the
right number of digits in their product. 
[1]*[4]=[4]
[2]*[3]=[4]
"""
# ok, start with some research:

def fact(n):
	f=1
	while n>1:
		f*=n
		n-=1
	return f

def nCr(n,r):
	if n>=r:
		return fact(n)/(fact(r)*fact(n-r))
	else:
		raise ValueError('n must be greater than r!')

def nPr(n,r):
	if n>=r:
		return fact(n)/fact(n-r)
	else:
		raise ValueError('n must be greater than r!')
		
"""
ok, the numbers here aren't bad.
number of total possible combinations of 9 digits = 9! = 362880 which isn't
the worst ever.
but there are only 9*70=630 possibilities for the [1]*[4]=[4] case, and 
36*35=1296 possibilities for the [2]*[3]=[4] case.

so: I need a function to determine all permutations of length l from a 
lexicon of digits, and a function to determine whether the product of two
numbers from the lexicon fits the remainder of the lexicon.

then I need to dedupe them and find their product, which is trivial.


shit, just realized that nCr doesn't account for permutations.
...there are only 9*1680=15120 possibilities for the [1]*[4]=[4] case, and 
72*210=15120 (oh, duh) possibilities for the [2]*[3]=[4] case. Actually, 
there are only 15120 permutations of five numbers and two ways to multiply 
them.
wait: then there are actually only 9P4=3042 possible answers, and I'd have 
to check through at most 120*2 possible permutations/multiplications of the other 
numbers to verify.


1234
0 12
1 13
2 14
3 23
4 24
5 34

12345
0 12
1 13
2 14
3 15
4 23
5 24
6 25
7 34
8 35
9 45

1234
0 123
1 124
2 134
3 234

0
3
[2345]
0 23
1 24
2 25
3 34
4 35
5 45

2345
0 234
1 235
2 245
3 345

"""


def sublexperm(n,res_len,lex):
	if n>nPr(len(lex),res_len):
		raise ValueError('not that many permutations!')
	# print "finding the %d permutation out of %d for %d elements of %s" % (n,nPr(len(lex),res_len),res_len,str(lex))
	c_num=n%nCr(len(lex),res_len)
	c=lexcomb(c_num,res_len,lex)
	p_num=n/nCr(len(lex),res_len)
	res=lexperm(p_num,c)
	return res
	
def lexcomb(n,res_len,lex):
	if n>=nCr(len(lex),res_len):
		print 'called lexcomb(%d,%d,%s,%s)' % (n,res_len,str(lex),res)
		raise ValueError('not that many combinations!')
	# print "finding the %d combination out of %d for %d elements of %s" % (n+1,nPr(len(lex),res_len),res_len,str(lex))
	res = ""
	while len(res)<res_len:
		thesePerms=nCr(len(lex)-1,res_len-len(res)-1)
		if n>thesePerms-1:
			lex=lex[1:]
			n-=thesePerms
		else:
			res+=lex[0]
			lex=lex[1:]
	return res

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
"""
for i in range(0,3023):
	c=i%nCr(9,4)
	p=i/nCr(9,4)
	res=sublexperm(i,4,'123456789')
	print "%d: c=%d, p=%d, res=%s" % (i,c,p,res)
"""

for i in range(0,3023):
	lex='123456789'
	res=sublexperm(i,4,lex)
	for l in res:
		lex=lex.replace(l,'')
	for l in lex:
		test=str(int(res)/int(l))
		t=list(test+res+l)
		t.sort()
		if int(res)%int(l)==0 and ''.join(t) == '123456789':
			print test+'*'+l+'='+res
	for j in range(0,20):
		d=sublexperm(j,2,lex)
		test=str(int(res)/int(d))
		t=list(test+res+d)
		t.sort()
		if int(res)%int(d)==0 and ''.join(t) == '123456789':
			print test+'*'+d+'='+res
"""
483*12=5796
157*28=4396
297*18=5346
1738*4=6952
1963*4=7852
186*39=7254
159*48=7632

45228
"""
