""" Euler 27: Quadratic Formula
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly 
divisible by 41.

Using computers, the incredible formula  n**2 + 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values n = 0 to 79. The product 
of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a|<=1000 and |b|<=1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
"""
import math

class primeList(object):
	primes=[2]
	def __init__(self,n=10000):
		self.add_n(n)
	def getList(self):
		return self.primes
	def add_n(self,n):
		i=max(self.primes)+1
		while len(self.primes) < n:
			self.add_if_prime(i)
			i+=1
	def add_til(self,x):
		i=max(self.primes)+1
		while max(self.primes) < x:
			self.add_if_prime(i)
			i+=1
	def add_if_prime(self,i):
		maybe=True
		j=0
		while self.primes[j]<=math.sqrt(i):
			if i%self.primes[j]==0:
				maybe=False
				break
			j+=1
		if maybe: self.primes.append(i)

def consecutive_primes(a,b,pl=primeList(),v=0):
	x=0
	y=b
	if v: print y
	while abs(y) in pl.getList():
		x+=1
		y=x*x+a*x+b
		if v: print y
		if abs(y)>max(pl.getList()):
			pl.primes=pl.add_til(abs(y))
	return x

myPrimes=primeList(10000)
maxA,maxB,maxPrimes = 0,0,0
bi=0
b=-myPrimes.getList()[bi]
while abs(b) <= 1000:
	a=0
	while a<=1000:
		thisPrimes=consecutive_primes(a,b,myPrimes)
		if maxPrimes<thisPrimes:
			maxA=a
			maxB=b
			maxPrimes=thisPrimes
		print "a="+str(a)+" b="+str(b)+" primes = "+str(thisPrimes) 
		a+=1
	bi+=1
	b=-myPrimes.getList()[bi]

print "a="+str(maxA)+" b="+str(maxB)+" max primes = "+str(maxPrimes)

# a=-61 b=971 max primes = 71
