"""
Euler 70: Totient Permutation

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1<=n<=10**7, for which phi(n) is a permutation of n and the ratio of n/phi(n)
is minimized.
"""

import prime
import qa
v=qa.v
srt=qa.srt()

n=10**7

if v:first_tick=qa.tick("finding n where phi(n) is a permutation of n, n<{0!s}".format(n))
if v:tick=qa.tick("generating primelist")
pl=prime.primeList()
pl.add_til(n)
if v:_=qa.tock(first_tick,"generated primelist up to {0!s}".format(pl.getList()[-1]))

found_permutations=0

min_ratio=100.0
min_phi=0
min_i=0

"""
for i in range(2,n+1):
    if v and i%int(n/10)==0:tick=qa.tock(tick,"found {0!s} permutations for n < {1!s}; min n/phi(n)={2!s} for phi({3!s})={4!s}".format(found_permutations,i,min_ratio,min_i,min_phi))
    
    srt.tick("calculating phi")
    i_phi=prime.faster_phi(i,pl)
    srt.tock("calculating phi")
    
    srt.tick("testing permutation")
    i_digits=list(str(i))
    i_digits.sort()
    phi_digits=list(str(i_phi))
    phi_digits.sort()
    srt.tock("testing permutation")
    
    if phi_digits==i_digits:
        found_permutations+=1
        srt.tick("checking minimum")
        i_ratio=float(i)/float(i_phi)
        if i_ratio<min_ratio:
            min_i=i
            min_phi=i_phi
            min_ratio=i_ratio
        srt.tock("checking minimum")
    
print "minimal n/phi(n)={0!s} for phi({1!s})={2!s}".format(min_ratio,min_i,min_phi)

if v:_=qa.tock(first_tick,"completed")
srt.summary()
pl.done()
"""

"""

ok, it's working but slow. if I wanted to speed it up, I can limit it to where n/phi(n) is sure to
be minimized, eg when low-exponent prime divisors are maximized.

n/phi(n)= n/(n*(1-1/p1)*(1-1/p2)*...*(1-1/pi)) 
        = 1/((p1-1)/p1)*((p2-1)/p2)*...*((pi-1)/pi)
        = p1*p2* ... *pn/((p1-1)*(p2-1)*...*(pi-1))

so phi is maximized for large primes? yes, but primes can't be permutations because n-1 can't have
the same digits as n. but products of large primes can -- so the best phi will come out of products
of primes.

brute-forcing cross-multiplication:
every meaningful candidate for a product less than x will have one multiple between sqrt(x) and 
x/5, say. Definitely x/2. 

plus, i don't even need to factor them to calculate phi, because I have the factors to begin with!
"""
import math
import bisect

if v:tick=qa.tick("generating test set of 2-prime products up to {0!s}".format(n))
srt.tick("generating test set")
test_set=[]

highest_prime_to_test=bisect.bisect_left(pl.getList(),int(n/5))
lowest_prime_to_test=bisect.bisect_right(pl.getList(),int(math.sqrt(n)))

for i in pl.getList()[lowest_prime_to_test:highest_prime_to_test]:
    highest_factor_prime_to_test=bisect.bisect_right(pl.getList(),int(n/i))
    for j in pl.getList()[:highest_factor_prime_to_test]:
        k=i*j
        if k < n:
            test_set.append(tuple([k,i,j]))
srt.tock("generating test set")
if v:tick=qa.tock(tick,"generated {0!s} products to test".format(len(test_set)))

how_many=0
for k,i,j in test_set:
    how_many+=1
    if v and how_many%int(len(test_set)/10)==0:tick=qa.tock(tick,"found {0!s} permutations for n < {1!s}; min n/phi(n)={2!s} for phi({3!s})={4!s}".format(found_permutations,i,min_ratio,min_i,min_phi))
    
    srt.tick("calculating phi")
    i_phi=(j-1)*(i-1)
    srt.tock("calculating phi")
    
    srt.tick("testing permutation")
    i_digits=list(str(k))
    i_digits.sort()
    phi_digits=list(str(i_phi))
    phi_digits.sort()
    srt.tock("testing permutation")
    
    if phi_digits==i_digits:
        found_permutations+=1
        srt.tick("checking minimum")
        i_ratio=float(k)/float(i_phi)
        if i_ratio<min_ratio:
            min_i=k
            min_phi=i_phi
            min_ratio=i_ratio
        srt.tock("checking minimum")
    
print "minimal n/phi(n)={0!s} for phi({1!s})={2!s}".format(min_ratio,min_i,min_phi)

if v:_=qa.tock(first_tick,"completed")
srt.summary()
pl.done()

"""
2015-06-19 00:39:00: finding n where phi(n) is a permutation of n, n<10000000
2015-06-19 00:39:00: generating primelist
2015-06-19 00:39:09: generated primelist up to 10000019 in 9.246115 seconds
2015-06-19 00:39:09: generating test set of 2-prime products up to 10000000
2015-06-19 00:39:10: generated 1514877 products to test in 1.449864 seconds
2015-06-19 00:39:12: found 67 permutations for n < 7417; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.692766 seconds
2015-06-19 00:39:14: found 119 permutations for n < 16901; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.671692 seconds
2015-06-19 00:39:15: found 156 permutations for n < 36997; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.659249 seconds
2015-06-19 00:39:17: found 192 permutations for n < 77191; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.769303 seconds
2015-06-19 00:39:19: found 222 permutations for n < 150571; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.728886 seconds
2015-06-19 00:39:21: found 262 permutations for n < 280589; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.787186 seconds
2015-06-19 00:39:22: found 284 permutations for n < 491167; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.641517 seconds
2015-06-19 00:39:24: found 303 permutations for n < 813997; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.673418 seconds
2015-06-19 00:39:26: found 333 permutations for n < 1315309; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.632181 seconds
2015-06-19 00:39:27: found 365 permutations for n < 1999969; min n/phi(n)=1.00070905112 for phi(8319823)=8313928 in 1.649173 seconds
minimal n/phi(n)=1.00070905112 for phi(8319823)=8313928
2015-06-19 00:39:27: completed in 27.601633 seconds
Summary statistics for 4 tracked subroutines:
testing permutation: 1514877 calls, 0:00:05.776148 total (avg 3.81294851003e-06 seconds)
calculating phi: 1514877 calls, 0:00:02.440610 total (avg 1.61109449809e-06 seconds)
checking minimum: 365 calls, 0:00:00.001022 total (avg 2.8e-06 seconds)
generating test set: 1 calls, 0:00:01.449814 total (avg 1.449814 seconds)

"""
