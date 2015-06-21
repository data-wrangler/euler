"""Euler 34: Sum of Factorials of their Digits

trying the same thing as 30, 5th powers.

wtf? I only come up with 1, 2, and 145. 1 & 2 are dq'd for not being sums, 
and 145 was their example. I put in 145 and they say no. Tried everything up
to 5 million.
"""

def fact(n):
	f=1
	while n>1:
		f*=n
		n-=1
	return f

# make a lookup
facts={0:1,1:1}
for i in range(2,10):
	facts[i]=fact(i)

# brute force forward test
def facttest(n,m):
	res=[]
	for i in range(n,m):
		facttot=0
		maybe=True
		for digit in str(i):
			facttot+=facts[int(digit)]
			if facttot>i:
				maybe=False
				break
		if maybe and facttot==i:
			res.append(i)
	return res
	
# revised brute force forward test
def factzeros(n,m):
	res=[]
	for i in range(n,m):
		facttot=0
		for digit in str(i):
			facttot+=facts[int(digit)]
		if int(str(facttot).replace('0',''))==i:
			res.append(i)
	return res
	
"""
ok, so checking with forward tests I'm being redundant. I only need to check
each combination of digits and see if the sum of their factorials without its
zeroes returns the same set.

two digits could be done bluntly in a test with two for loops, three with three.
i could keep a running array of known things, then append.
"""

dig=['1','2','3','4','5','6','7','8','9']

def testset(test):
	testres=[]
	for i in test:
		# print "testing " + i
		ilist=list(i)
		ilist.sort()
		facttot=0
		for digit in str(i):
			facttot+=facts[int(digit)]
		l=list(str(facttot).replace('0',''))
		l.sort()
		if ''.join(l)==''.join(ilist):
			print "matched "+ i
			testres.append(i)
	return testres

def iterset(old):
	# print 'iterating set'
	new=[]
	for elementi in ['1','2','3','4','5','6','7','8','9']:
		for elementj in old:
			new.append(elementi+elementj)
	return new

#res=[]
#for i in range(0,7):
#	res+=testset(dig)
#	dig=iterset(dig)
#	print res
	
"""
This is still brute force. How can I narrow down the set of numbers that 
could petentially be the sums of the factorials of their digits?
"""

"""
the set of digit factorials establishes a set similar to prime factorials. 
There was something about this in number theory, I'm sure of it. Given two numbers,
what other numbers can be made out of combinations of them?


0=1
1=1
2=2
3=6
4=24
5=120
6=720
7=5040
8=40320
9=362880

edit: shit, zero factorial = 1. I think I did a lot of previous stuff here assuming
it was zero.

wtf.

40585 is the only other one.
"""

# array of digit factorials:
df=[1
,1
,2
,6
,24
,120
,720
,5040
,40320
,362880
]