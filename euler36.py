"""Euler 36: Palindromes in base 10 and base 2:

Find the sum of all numbers, less than one million, which are palindromic 
in base 10 and base 2.

All numbers of six digits or fewer can be reduced to all numbers three 
digits or fewer twice: once with an even number of digits (repeating all 
including the last digit) and once with an odd number (repeating all but 
the last digit). 

So let's build them.
"""

pals=[]
for i in range (1,1000):
	pal_even = str(i)+str(i)[::-1]
	pal_odd = str(i)+str(i)[::-1][1:]
	pals.append(pal_even)
	pals.append(pal_odd)

"""
Then we need to convert them to binary.
"""

def ibin(n):
	return bin(int(n))[2:]

"""
and check whether they're palindromes
"""

def ispal(s):
	if len(str(s))==1:
		return True
	else:
		return str(s)[:len(str(s))/2]==str(s)[-(len(str(s))/2):][::-1]
	
doublepals=[]
for n in pals:
	if ispal(ibin(n)):
		doublepals.append([n,ibin(n)])

len(doublepals)