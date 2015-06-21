"""
Let p(n) represent the number of different ways in which n coins can be separated 
into piles. For example, five coins can separated into piles in exactly seven 
different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

ok, so combinatorics. 

2:
OO
O O

3:
OOO
OO O
O O O

4:
OOOO
OOO O
OO OO
OO O O
O O O O


"""

def fact(n):
	if n>1:
		f=1
		while n>1:
			f*=n
			n-=1
		return f
	else: 
		return 1

def nCr(n,k):
	if n>k:
		return fact(n)/(fact(k)*fact(n-k))
	else:
		return 0