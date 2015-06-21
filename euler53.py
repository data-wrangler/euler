""" Euler 53: Combinatoric Selections
There are exactly ten ways of selecting three from five, 12345:
	123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.

In general,
	nCr = n! / r!(n-r)!
where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, 
are greater than one-million?
"""

from itertools import combinations

# brute force:
def bf(i):
	for j in range(1,i+1):
		for k in range(1,k):
			if len(list(combinations('x'*j,k))) >= 1000000:
				print "{0!s}C{1!s}".format(j,k)

"""
ok, so my old thought was to set up a dictionary of the factorials and try to run the calculations faster. 

I'll leave that here and come back to it later.
"""

# factorial w/ dictionary

fdict={0:1,1:1,2:2}

def fact(n):
	try:
		return fdict[n]
	except:
		fdict[n]=n*fact(n-1)
		return fdict[n]

def fact_nonrecursive(n):
    return None

"""
so this is kinda set theory.

i know nothing under 23 has a combination value gt 1M, so for n between 23 and 100, how many values 
of nCr, r<n, are greater than 1M?

generating a list of factorials from 1-100 is fast using the fact dictionary above.

so the question is then reduced to:

1000000 < n!/(r!*(n-r!))

1000000*(r!*(n-r!)) < n!

and for this I actually only need to check half, because the math is symmetrical. 23C10 = 23C(23-10)
and more than that, i only need to check until I get to one that's more than a million, 
because the numbers will max out in the middle.
so if nCi>1M, then nCj>1M for i<=j<=n-i

ok. so let's think this through again:

23C10 is the first:
FFFFFFFFFTTTTFFFFFFFFF
"""
fact(100)

n_gt_mil=0
for i in fdict:
    j=1
    gt_mil=False
    while j<i/2:
        if fdict[i]/fdict[j]/fdict[i-j]>1000000:
            gt_mil=True
            break
        j+=1
    if gt_mil:
        print "{0!s}C{1!s}>1M -- adding {2!s}".format(i,j,i-2*j+1)
        n_gt_mil+=i-2*j+1
print n_gt_mil

# 4075