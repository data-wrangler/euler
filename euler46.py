"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

# stealing some prime objects from euler 12

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
		j=0
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
    
"""
ok, so we're probably better working forward than backwards.

1. construct a list of primes
2. construct a list of square numbers and double them
3. add 'em
4. see what's missing.
"""

pL=primeList(5000)
p=pL.getList()
s=map(lambda x:2*x**2,range(1,201))

import itertools

all_combinations=list(itertools.chain.from_iterable(map(lambda x:map(lambda y:x+y,p),s)))
all_combinations.sort()

seen = set()
seen_add = res.add
a=[ x for x in all_combinations if not (x in seen or seen_add(x))]

for i in range(0,10000):
    try: _=b.index(2*i+1)
    except:
        try: _=p.index(2*i+1)
        except: print 2*i+1

# 5777
# 5993