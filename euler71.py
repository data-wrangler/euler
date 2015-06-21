"""
Euler 71: Ordered Fractions

Consider the fraction n/d, where n and d are positive integers. If n<d and gcd(n,d)=1, it
is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

it can be seen that 2/5 is the fraction immediately to the left of 3/7.

by listing the set of reduced proper fractions for d<= 1000000 in ascending order of 
size, find the numerator of the fraction immediately to the left of 3/7.

-----

i really don't need to do that much work here.

for any number, find the highest integer relatively prime to it and less than 3/7.

realistically, i probably don't even need to count the ones where I would have to 
decrement to find the highest relatively prime number, but it can't really hurt to
do it, it'll just add time.
"""

from fractions import gcd

max_d=1000000
target_n=3
target_d=7
best_fractions=[]

for d in range(2,max_d+1):
    if gcd(d,target_d)!=1:
        continue
    n=d*target_n/target_d
    while gcd(n,d)!=1:
        n-=1
    best_fractions.append(tuple([n,d]))

min_fraction=tuple([0,1])

for n,d in best_fractions:
    if float(n)/float(d) > float(min_fraction[0])/float(min_fraction[1]):
        min_fraction = tuple([n,d])

print min_fraction

# (428570, 999997)