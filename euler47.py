"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

# gonna need these prime boys agan.

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
shit, how do I even get started on this?

if you were going to brute force it:
1. start at 647 and 
2. pfact -- if it has 4 factors, keep it and go on; else increment and do 2 again
3. increment and pfact -- if it has 4 factors, 
    if those factors are distinct from 3, keep it and go on; else put this in 1st position and repeat this step
    ; else increment and do 2 again
4. increment and pfact -- if it has 4 factors, 
     if those factors are distinct from 2, 
         if those factors are distinct from 1; return the set; else 2>1 & 3>2, increment and do this step again
         else put this in 1st position and repeat 3
    else increment and do 2 again

"""

def have_common_factors(pfa,pfb):
    for i in range(min(len(pfa),len(pfb))):
        if pfa[i]==pfb[i] and pfa[i]>0:
            return True
    return False

def iterative_test(i,j):
    # create a working prime list with enough #s to test this range
    pL=primeList(100000)
    # initialize the resultset
    res=[]

    # start testing
    while i < j:
        # grab the prime factorization of i
        ipf=pfact(i,pL)
        
        # first check if this number has four prime factors
        if len(ipf)-ipf.count(0) == 4:
            print "{0!s} has 4 prime factors.".format(i)
            # if it does, behavior is based on how many #s we already have
            if len(res)==0:
                # if this is the first, just add it.
                print "adding it."
                res.append(ipf)
            elif len(res) == 1:
                # this could be the second, check that they are distinct
                if have_common_factors(ipf,res[0]):
                    # they have common factors; set this to the starting # and continue
                    print "{0!s} has common factors with {1!s}; starting over with {0!s}.".format(i,pconstruct(res[0],pL))
                    res=[ipf]
                else:
                    # no common factors, append & continue
                    print "no common factors! adding it."
                    res.append(ipf)
            elif len(res) == 2:
                # gotta check both. most recent first
                if have_common_factors(ipf,res[1]):
                    # nope. start over with this
                    print "{0!s} has common factors with {1!s}; starting over with {0!s}.".format(i,pconstruct(res[1],pL))
                    res=[ipf]
                else:
                    # cool with set 2, check 1
                    if have_common_factors(ipf,res[0]):
                        # 2 is cool but 1 has gotta go
                        print "{0!s} has common factors with {1!s}; starting over with {2!s} and {0!s}.".format(i,pconstruct(res[0],pL),pconstruct(res[1],pL))
                        res.__delitem__(0)
                        res.append(ipf)
                    else:
                        # cool with both, append it
                        print "no common factors! adding it."
                        res.append(ipf)
            elif len(res) == 3:
                # almost there! most recent first
                if have_common_factors(ipf,res[2]):
                    # nope. start over with this
                    print "{0!s} has common factors with {1!s}; starting over with {0!s}.".format(i,pconstruct(res[2],pL))
                    res=[ipf]
                else:
                    # cool with 3, check 2
                    if have_common_factors(ipf,res[1]):
                        # keep 3, scrap 1&2
                        print "{0!s} has common factors with {1!s}; starting over with {2!s} and {0!s}.".format(i,pconstruct(res[1],pL),pconstruct(res[2],pL))
                        res.__delitem__(1)
                        res.__delitem__(0)
                        res.append(ipf)
                    else:
                        # cool with 3 and 2, check 1
                        if have_common_factors(ipf,res[0]):
                            print "{0!s} has common factors with {1!s}; starting over with {3!s}, {2!s} and {0!s}.".format(i,pconstruct(res[0],pL),pconstruct(res[1],pL),pconstruct(res[2],pL))
                            res.__delitem__(0)
                            res.append(ipf)
                        else:
                            # it works!
                            print "no common factors! all done."
                            res.append(ipf)
                            return res
        else:
            # if this number doesn't have four prime factors, start over with the next one
            if len(res)>0:
                print "{0!s} doesn't have 4 prime factors. starting over.".format(i)
            res=[]
        i+=1
