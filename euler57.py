"""
Euler 57: square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

print 1.+1./2.
print 1.+1./(2.+1./2.)
print 1.+1./(2.+1./(2.+1./2.))
print 1.+1./(2.+1./(2.+1./(2.+1./2.)))

"""
okay, so this isn't about square roots, it's about constructing fractions.

i actually want two series: one for the numerator and one for the denom.
n=3,7,17,41,99,239,577
d=2,5,12,29,70,169,408

d[i] = n[i-1]+d[i-1]
n[i] = 2*n[i-1]+n[i-2]

easy peasy.
"""

n_gt_d=0
d=[2,5]
n=[3,7]

for i in range(2,1000):
    d.append(d[i-1]+n[i-1])
    n.append(2*n[i-1]+n[i-2])
    this_n_gt_d=len(str(n[i]))>len(str(d[i]))
    if this_n_gt_d: n_gt_d+=1
    print "{0!s} {1!s} {2!s}/{3!s}".format(i,this_n_gt_d,n[i],d[i])

print "found {0!s} terms with more digits in numerator than denominator".format(n_gt_d)

# 153