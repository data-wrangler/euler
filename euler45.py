"""Euler 45: tri, pent, hex
40755 is triangular, pentagonal and hexagonal: 

tri = n(n+1)/2
pen = n(3n-1)/2
hex = n(2n-1)

t = n(n+1)/2
n**2 + n -2p == 0
(-1 +- sqrt( 1 + 8t))/2 == n

0 = 3n*2 -n -2p
(1+-sqrt(1-4*3*-2p))/6 == n
(1+- sqrt(1+24p))/6 == n

0 = 2n**2 -n -h
(1+-sqrt(1+8h))/4 == n

ok.
"""
import math

def isTri(t):
	n=(-1.0 + math.sqrt(1.0 + 8.0*t))/2.0
	if n==int(n): return True
	else: return False

def isPen(p):
	n=(1.0 + math.sqrt(1.0 + 24.0*p))/6.0
	if n==int(n): return True
	else: return False


def isHex(h):
	n=(1.0 + math.sqrt(1.0 + 8.0*h))/4.0
	if n==int(n): return True
	else: return False
	
"""
so we'll start with hexes 'cause they move the quickest, and we're starting 
with n=144 to get to the "next" tripenthex number.
"""

n = 144
while not (isPen(n*(2*n-1)) and isTri(n*(2*n-1))):
	n+=1

x=n*(2*n-1)
print "n=%d, hex=%d" % (n,x)
h=(1.0 + math.sqrt(1.0 + 24.0*x))/6.0
print "n=%d, pent=%d" % (h,x)
t=(-1.0 + math.sqrt(1.0 + 8.0*x))/2.0
print "n=%d, tri=%d" % (t,x)