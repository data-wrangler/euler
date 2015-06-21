""" Euler 35: Circular Primes

The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

1. generate primes.
2. rotate digits
	test for primality
	keep primes

This is only possible for primes where all their digits are 1,3,7,9 since
they all.
"""
"""
import math

def rotate(n):
	str_n=str(n)
	rot_n=[str_n]
	for i in range(1,len(str_n)):
		str_n=str_n[1:]+str_n[0]
		rot_n.append(str_n)
	return rot_n

# 		
def circPrimes(n):
	primes=[2,3,5,7]
	i=max(primes)+1
	while i < n:
		maybe=True
		if '0' in str(i)\
		or '2' in str(i)\
		or '4' in str(i)\
		or '5' in str(i)\
		or '6' in str(i)\
		or '8' in str(i):
			maybe=False
		else:
			for prime in primes:
				if i%prime==0:
					maybe=False
					break
		if maybe: primes.append(i)
		i+=1
	return primes
	
def allPrimes(n):
	primes=[2]
	i=max(primes)+1
	while max(primes) < n:
		maybe=True
		for prime in primes:
			if i%prime==0:
				maybe=False
				break
		if maybe: primes.append(i)
		i+=1
	return primes

def primeCheck(pList):
	primes=allPrimes(math.sqrt(max(pList)))
	for prime in pList:
		maybe=True
		i=0
		while primes[i]<math.sqrt(prime):
			if prime%primes[i]==0:
				maybe=False
				break
			i+=1
		if not maybe:
			del(pList[pList.index(prime)])
	return pList

def circCheck(pList):
	circles=[]
	for prime in pList:
		rotList=rotate(str(prime))
		maybe=True
		for rot in rotList:
			if int(rot) not in pList:
				maybe=False
				break
		if maybe:circles.append(prime)
	return circles
"""

"""
I need to start over on this guy.

Ok, so we can start by limiting our set to numbers containing 1,3,7,9

there are two ways to go about this: 
1: generate primes up to x, then check whether their rotations are also 
members
2: generate possible numbers, rotate, primality testing.

definitely going with #1

"""
import math
import re

def pList(n):
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
		else:i+=1
	return pl

def winnow(checklist):
	newlist=[2,5]
	for element in checklist:
		# print "testing"+str(element) 
		if str(element).find('2')<0\
		and str(element).find('4')<0\
		and str(element).find('5')<0\
		and str(element).find('6')<0\
		and str(element).find('8')<0\
		and str(element).find('0')<0:
			newlist.append(element)
	return newlist

def rotate(n):
	rots=[n]
	for i in range(0,len(str(n))-1):
		rots.append(int(str(rots[i])[1:]+str(rots[i])[0]))
	return rots
	
def checkRots(startlist):
	passlist=[]
	for i in startlist:
		irots=rotate(i)
		maybe=True
		for j in irots:
			if not startlist.__contains__(j):
				maybe=False
				break
		if maybe:passlist.append(i)
	return passlist

p=pList(1000000)
q=winnow(p)
r=checkRots(q)
print r
print len(r)