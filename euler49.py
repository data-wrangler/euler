"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""

# gonna need my prime stuff again.
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
ok, so there are two sequences of three four-digit numbers that has three properties:
1. all prime
2. has the same step between incremental numbers.
3. permutations of each other

so we can start with a list of four-digit primes, group them into sets of at least three numbers that share digits, and check for increasing sequences.

the smallest 4-digit prime is 1009, the largest is 9973, indexes 179 and 1253 respectively
"""

p=primeList()
pl=p.getList()

# list of all 4-digit primes
a=pl[179:1254]

"""
so let's pull in some lexical permutations work.
"""

def fact(n):
	f=1
	while n>1:
		f*=n
		n-=1
	return f

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
		
def allperm(lex):
	perm=[]
	for i in range(fact(len(lex))):
		perm.append(lexperm(i,lex))
	return perm

def perm_test(n):
	same_digits=allperm(str(n))
	maybe=True
	for i in range(2,7):
		if str(i*n) not in same_digits:
			maybe=False
			break
	return maybe
    
"""
ok, so I can quickly get all permutations of a string.

here's the test:
1) pop the first prime in the list
2) find all its lexical permutations
3) pop them from the list if they exist
4) check if there are more than three
5) if so, iterate through combinations of two excluding the highest number
6) take the difference between the first two and add it to the second, see if that number exists in the list.

"""

while len(a)>0:
    first=a.pop(0)
    a_perms=allperm(str(first))
    prime_perms=[int(n) for n in a_perms if int(n) in a]
    for n in prime_perms: 
        try: 
            a.remove(n)
        except:
            pass
    if len(prime_perms)<3:
        pass
    else:
        for i in range(len(prime_perms)-2):
            for j in range(i+1,len(prime_perms)-1):
                k = 2*prime_perms[j]-prime_perms[i]
                if k in prime_perms and prime_perms[j] != prime_perms[i]:
                    print "{0!s}, {1!s}, {2!s}".format(prime_perms[i],prime_perms[j],k)
