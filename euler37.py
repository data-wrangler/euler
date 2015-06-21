"""
Euler 37: Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each stage: 
	3797, 797, 97, and 7. 
Similarly we can work from right to left: 
	3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

first and last digits must be 2,3,5,7; middle digits must be 1,3,7,9

"""
import re
import math
import time

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
	
def winnow(checklist):
	endlist=[]
	for element in checklist:
		r=re.match('^[2357][1379]*[2357]$',str(element))
		if r:
			endlist.append(element)
	return endlist

def pwinnow(primelist):
	newplist=[]
	for element in primelist:
		r=re.match('^[123579][1379]*[123579]$',str(element))
		if r:
			newplist.append(element)
	return set(newplist)

def trunc(n):
	tset=[n]
	ln=str(n)
	rn=str(n)
	while len(ln)>1:
		tset.append(int(ln))
		tset.append(int(rn))
		ln=ln[1:]
		rn=rn[:-1]
	return tset

def testset(tset,pset):
	if len(set(tset).difference(pset))==0:
		return tset[0]
	else: return None

def runtest(x):
	p=pList(x)
	print "primes generated"
	q=winnow(p)
	print "test list winnowed"
	k=pwinnow(p)
	print "prime list winnowed"
	for i in q:
		t=trunc(i)
		r=testset(t,k)
		if r: print r
"""
23
37
53
73
313
317
373
797
3137
3797
739397
"""
