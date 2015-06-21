# project euler problem 12
#  
# What's the first triangle number to have over 500 divisors?
#

from datetime import datetime as dt
import matplotlib.pyplot as plt

# generate list of triangle numbers

def pop_tri(n): 
	tri = [0]
	for i in range(1,n):
		tri.append(tri[i-1]+i)
	return tri

def ndiv(n):
	div=[1,n]
	for i in range(n/2,1,-1):
		j=float(n)/float(i)
		if int(j)==j:
			div+=[i]
	return len(div)

def find_div(tri):
	tri_div=[[],[]]
	for t in tri:
		start_time = dt.now()
		nd=ndiv(t)
		it_took=(dt.now()-start_time)
		print "%d : found %d divisors in %s" % (t,nd,it_took.__str__())
		tri_div[0].append(t)
		tri_div[1].append(nd)
	return tri_div

def plot_it(tri_div):
	plt.plot(tri_div[0],tri_div[1],'ro')
	plt.xlabel('triangular numbers')
	plt.ylabel('number of divisors')
	plt.title('number of divisors of triangular numbers')
	plt.show()

def tri_n(n):
	return (n-1)*(float(n)/2.0)

def getPrimes(n):
	start_time = dt.now()
	primes=[2]
	i=3
	while len(primes) < n:
		maybe=True
		for prime in primes:
			if i%prime==0:
				maybe=False
				break
		if maybe: primes.append(i)
		i+=1
	it_took=dt.now()-start_time
	print "found %d primes in %s" % (n,it_took.__str__())
	return primes
				
def pfact(n,primes):
	pf=[0]
	remainder=n
	i=0
	while remainder > 1:
		try:
			if remainder%primes[i]==0:
				remainder/=primes[i]
				pf[i]+=1
			else:
				i+=1
				pf.append(0)
		except IndexError:
			raise IndexError('ran out of primes!')
	return pf
	
def pconstruct(pf,primes):
	n=1
	for i in range(len(pf)):
		n*=primes[i]**pf[i]
	return n

def nfacts(pf):
	nf=1
	for i in range(max(pf)+1):
		nf*=(i+1)**pf.count(i)
	return nf

"""
so: knowing that triangular numbers are of the form (n-1)*(n/2), 
I want to find the lowest (even) n such that the elementwise sum of the 
prime factorizations of (n-1) and (n/2) yeilds over 500 divisors.
"""

def sumElements(a,b):
	if len(a)<len(b):
		c=b
		b=a
		a=c
	for i in range(0,len(b)):
		a[i]+=b[i]
	return a

def triFact_n(n,primes):
	m=2*n-1
	fm=pfact(m,primes)
	fn=pfact(n,primes)
	tot=sumElements(fm,fn)
	nf = nfacts(tot)
	print "triangle number %d has %d factors" % (2*n,nf)
	return nf

def run_sim(n,nprimes):
	plist=getPrimes(nprimes)
	for i in range(n+1):
		nfacts = triFact_n(i,plist)