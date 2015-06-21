"""
Euler 73: Counting Fractions in a range

Consider the fraction n/d, where n and d are positive integers. If n<d and gcd(n,d)=1, it
is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen there are 3 fractions in the range 1/3 to 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions with d <=12000?

-----

Oof. Can I even repurpose my previous work? phi doesn't give me shit about a range.

-> all numbers > 2 will have even numbers of prime divisors because all fractions have a complement other than 1/2 
25

ok, so less than 1/2 is easy. now how do we figure out how many of them are > 1/3?

what about numbers ===0 mod 3?

60 (2,3,5) = 60/2 = 30 * 2/3 = 20 * 4/5 = 16

1 7 11 13 17 19 23 29 31 37 41 43 47 49 53 59
               |           |
hm.

wait, but brute force here should be relatively easy.

12000 iterations, max 2000 checks
84M total.
"""

from fractions import gcd
import qa
v=qa.v

max_test=12000
reduced_fractions=[]

if v:first_tick=tick=qa.tick("calculating phi for integers up to {0!s}".format(max_test))
for i in range(5,max_test+1):
    start_loop_at=int(i/3)+1
    end_loop_at=int(i/2)
    step_by=1
    for j in range(start_loop_at,end_loop_at+1,step_by):
        if gcd(i,j)==1 and float(j)/float(i)>1./3. and float(j)/float(i)<1./2.:
            reduced_fractions.append(tuple([j,i]))
    if v and i%1000==0:tick=qa.tock(tick,"{0!s} reduced proper fractions for denominators less than {1!s}".format(len(reduced_fractions),i))

print "total {0!s} reduced proper fractions for denominators less than {1!s}".format(len(reduced_fractions),max_test)
#for f in reduced_fractions:
#    print "{0!s}/{1!s}".format(f[0],f[1])
if v:_=qa.tock(first_tick,"completed")