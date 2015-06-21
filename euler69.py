"""
Euler 69: Totient Maximum

Euler's totient function, phi(n), is used to determine the number of numbers less than n which are 
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8 are all less than 9 and relatively prime
to 9, phi(9)=6.

n   rel prime   phi n/phi
2   1           1   2
3   1,2         2   1.5
4   1,3         2   2
5   1,2,3,4     4   1.25
6   1,5         2   3
7   1,2,3,4,5,6 6   1.166..
8   1,3,5,7     4   2
9   1,2,4,5,7,8 6   1.5
10  1,3,7,9     4   2.5

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1000000 for which n/phi(n) is maximized.

-----

Well, I feel like I cheated a little bit here by googling the totient function, but it made sense 
in less than a minute so I'm just going to use it. I was probably supposed to derive it.

given the prime factorization p(n)=p1^e1*p2^e2...pi^ei, the number of relatively prime numbers less
than n is given by:

phi(n)=n*(1-1/p1)*(1-1/p2)* ... *(1-1/pi)

right, and this works because all primes are relatively prime to each other, so their ratios apply 
even after the others have been removed.
"""
import prime
import qa

v=qa.v

if v:first_tick=tick=qa.tick("generating prime list")
pl=prime.primeListDb(82500) # primes up to 1M
if v:tick=qa.tock(tick,"prime list generated up to {0!s}".format(pl.getList()[-1]))

def phi(n,prime_list):
    pf_n=prime.pfact(n,prime_list)
    rpf=float(n)
    for i in range(len(pf_n)):
        if pf_n[i]>0:
            rpf*=(float(1)-float(1)/float(prime_list.getList()[i]))
    return int(rpf)

max_n=1000000
phis=[]

if v:tick=qa.tick("calculating phi for numbers up to {0!s}".format(max_n))

# pretty much guaranteed that whatever we end up with as a max is =0 mod 210 (2*3*5*7)
for n in range(210,max_n+1,210):
    phis.append(tuple([phi(n,pl),n]))
    if v and n%10000==0:tick=qa.tock(tick,"done up to {0!s}".format(n))

if v:tick=qa.tock(tick,"calculated")

max_ratio=1.0
n_with_max_ratio=1

if v:tick=qa.tick("finding the maximum")

for phi_x,x in phis:
    if float(x)/float(phi_x) > max_ratio:
        max_ratio = float(x)/float(phi_x)
        n_with_max_ratio=x

if v:_=qa.tock(tick,"found")

print n_with_max_ratio, phi(n_with_max_ratio,pl), max_ratio

if v:_=qa.tock(first_tick,"completed")

# 510510 92160 5.53938802083