"""
Project Euler #12: Find the first Triangle Number with over 500 divisors.

condensed: knowing that triangular numbers are of the form (n-1)*(n/2), 
I want to find the lowest (even) n such that the elementwise sum of the 
prime factorizations of (n-1) and (n/2) yeilds over 500 divisors.
Then, I only need to check triangle number n-1 (odd) to see if it also has
over 500 divisors, and one of those two is the winner.
"""
import math

class primeList(object):
	primes=[2,3]
	def __init__(self,n=10000):
		self.primes=self.add_n(n)
	def getList(self):
		return self.primes
	def add_n(self,n):
		i=max(self.primes)+1
		while len(self.primes) < n:
			self.add_if_prime(i)
			i+=1
		return self.primes
	def add_til(self,x):
		i=max(self.primes)+1
		while max(self.primes) < x:
			self.add_if_prime(i)
			i+=1
		return self.primes
	def add_if_prime(self,i):
		maybe=True
		j=1
		while self.primes[j]<math.sqrt(i):
			if i%self.primes[j]==0:
				maybe=False
				break
			j+=1
		if maybe: self.primes.append(i)

# return prime factorization of n
def pfact(n,primes):
	pf=[0]
	remainder=n
	i=0
	while remainder > 1:
		try:
			if remainder%primes.getList()[i]==0:
				remainder/=primes.getList()[i]
				pf[i]+=1
			else:
				i+=1
				pf.append(0)
		except IndexError:
			primes.add_til(remainder/2)
	return pf

# construct number from prime factorization
def pconstruct(pf,primes):
	n=1
	for i in range(len(pf)):
		n*=primes.getList()[i]**pf[i]
	return n

# return number of factors using prime factorization
def nfacts(pf):
	nf=1
	for i in range(max(pf)+1):
		nf*=(i+1)**pf.count(i)
	return nf

# perform element-wise sum of two lists
def sumElements(a,b):
	if len(a)<len(b):
		c=b
		b=a
		a=c
	for i in range(0,len(b)):
		a[i]+=b[i]
	return a

# brute force count of divisors
def ndiv(n):
	div=[1,n]
	for i in range(n/2,1,-1):
		j=float(n)/float(i)
		if int(j)==j:
			div+=[i]
	return len(div)

# return nth triangle number
def tri_n(n):
	return (n-1)*(float(n)/2.0)

""" here comes the actual simulation part """

def triFact(n,primes):
	m=2*n-1
	fm=pfact(m,primes)
	fn=pfact(n,primes)
	tot=sumElements(fm,fn)
	nf = nfacts(tot)
	# print "triangle number %d has %d factors" % (2*n,nf)
	return nf

def run_sim(factLimit):
	myprimes = primeList()
	i=1
	while True:
		nf=triFact(i,myprimes)
		print "triangle number %d is %d with %d factors" % (2*i,tri_n(2*i),nf)
		if nf > factLimit:
			print "triangle number %d is %d with %d factors" % (2*i,tri_n(2*i),nf)
 			break
 		i+=1
	