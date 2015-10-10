
# save me from copying this shit so many times

import math
from fractions import gcd

import psycopg2 as pg
import bisect
import itertools

class primeListDb(object):
    conn=pg.connect("dbname=jmatthew user=jmatthew")
    cursor=conn.cursor()
    primes=[]
    def __init__(self,n=10000):
        self.add_n(n)
    def getList(self):
        return self.primes
    def add_n(self,n):
        if n>len(self.primes):
            self.cursor.execute("select prime from primes where id > {0!s} and id <= {1!s} order by prime".format(len(self.primes),n))
            db_primes=self.cursor.fetchall()
            self.primes+=[row[0] for row in db_primes]
            i=self.primes[-1]+2
            while len(self.primes) < n:
                self.add_if_prime(i)
                i+=2
    def add_til(self,x):
        if x>self.primes[-1]:
            self.cursor.execute("select prime from primes where id > {0!s} and id <= coalesce((select id from primes where prime >= {1!s} order by id limit 1),(select max(id) from primes)) order by prime".format(len(self.primes),x))
            db_primes=self.cursor.fetchall()
            self.primes+=[row[0] for row in db_primes]
            i=self.primes[-1]+2
            while self.primes[-1] < x:
                self.add_if_prime(i)
                i+=2
    def add_if_prime(self,i):
        maybe=True
        j=0
        while self.primes[j]<=math.sqrt(i):
            if i%self.primes[j]==0:
                maybe=False
                break
            j+=1
        if maybe: 
            self.primes.append(i)
            self.cursor.execute("insert into primes (prime) values ({0!s})".format(i))
            self.conn.commit()
    def isPrime(self,x):
        if x in [2,3]:
            return True
        elif x%2==0: 
            return False
        elif x%3==0:
            return False
        elif self.primeSearch(x):
            return True
        elif x > self.primes[-1]:
            self.add_til(x)
            if self.primeSearch(x):
                return True
            else:
                return False
        else: 
            return False
    def primeSearch(self,x):
        i=bisect.bisect_left(self.primes,x)
        if i != len(self.primes) and self.primes[i]==x:
            return i
        else:
            return None
    def done(self):
        self.cursor.close()
        self.conn.close()

class primeList(primeListDb):
    pass

# return prime factorization of n
def pfact(n,primes):
	pf=[0]
	remainder=n
	i=0
	p_i=2
	while remainder > 1:
		try:
			if remainder%p_i==0:
				remainder/=p_i
				pf[i]+=1
			else:
				i+=1
				p_i=primes.getList()[i]
				pf.append(0)
		except IndexError:
			primes.add_til(remainder)
	return pf

# construct number from prime factorization
def pconstruct(pf,primes):
	if len(pf)>len(primes.getList()):
		primes.add_n(len(pf))
	n=1
	for i,p in zip(pf,primes.getList()[:len(pf)]):
		n*=p**i
	return n

# return number of relatively prime divisors less than n
def phi(n,primes):
    pf_n=pfact(n,primes)
    rpf=n
    for i in range(len(pf_n)):
        if pf_n[i]>0:
            p_i=primes.getList()[i]
            rpf=rpf*(p_i-1)/p_i
    return int(rpf)

# get the 1/0 existence of prime factors, map to an integer as though this were a binary number
def fast_pfact(n,primes):
	pf=0
	remainder=n
	i=0
	while remainder > 1:
		try:
			p_i=primes.getList()[i]
			if remainder%p_i==0:
				pf+=2**i
				while remainder%p_i==0:
					remainder/=p_i
			i+=1
		except IndexError:
			primes.add_til(remainder)
	return pf

def fast_phi(pf_n,primes):
    rpf_n=1
    rpf_d=1
    remainder=pf_n
    while remainder>0:
        i=int(round(math.log(remainder,2),10))
        p_i=primes.getList()[i]
        rpf_n*=(p_i-1)
        rpf_d*=p_i
        rpf_gcd=gcd(rpf_n,rpf_d)
        rpf_n/=rpf_gcd
        rpf_d/=rpf_gcd
        remainder-=2**i
    return rpf_n,rpf_d
    
def faster_phi(n,primes):
    if primes.isPrime(n):
        return n-1
    pf_n=fast_pfact(n,primes)
    rpf=n
    remainder=pf_n
    while remainder>0:
        i=int(round(math.log(remainder,2),10)) 
        # rounding is necessary to account for small errors in logarithms inherent to floating point math. 
        # This .10 precision works up to 1m at least, but could fail at higher n.
        p_i=primes.getList()[i]
        rpf=rpf*(p_i-1)/p_i
        remainder-=2**i
    return rpf

"""
def isprime(n):
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False

      i += w
      w = 6 - w

   return True
   
"""

# basically deprecated

class primeListLocal(object):
    primes=[2,3]
    def __init__(self,n=10000):
        self.primes=self.add_n(n)
    def getList(self):
        return self.primes
    def add_n(self,n):
        i=self.primes[len(self.primes)-1]+2
        while len(self.primes) < n:
            self.add_if_prime(i)
            i+=2
        return self.primes
    def add_til(self,x):
        i=max(self.primes)+2
        while self.primes[len(self.primes)-1] < x:
            self.add_if_prime(i)
            i+=2
        return self.primes
    def add_if_prime(self,i):
        maybe=True
        j=0
        while self.primes[j]<=math.sqrt(i):
            if i%self.primes[j]==0:
                maybe=False
                break
            j+=1
        if maybe: self.primes.append(i)
    def isPrime(self,x):
        if x in self.primes:
            return True
        elif x > self.primes[len(self.primes)-1]:
            self.add_til(x)
            return x in self.primes
        else: 
            return False
