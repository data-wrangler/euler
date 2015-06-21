"""
Euler 58: Spiral Diagonal Primality

Starting with 1 and spiralling anticlockwise in the following way, a square 
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right 
diagonal, but what is more interesting is that 8 out of the 13 numbers lying 
along both diagonals are prime.

If one complete new layer is wrapped around the spiral above, a square spiral 
with side length 9 will be formed. If this process is continued, what is the 
side length of the square spiral for which the ratio of primes along both 
diagonals first falls below 10%?

-----

here's one more iteration:

65 64 63 62 61 60 59 58 57
66 37 36 35 34 33 32 31 56
67 38 17 16 15 14 13 30 55
68 39 18  5  4  3 12 29 54
69 40 19  6  1  2 11 28 53
70 41 20  7  8  9 10 27 52
71 42 21 22 23 24 25 26 51
72 43 44 45 46 47 48 49 50
73 74 75 76 77 78 79 80 81

"""
import math
import prime

def spiral_diag(n):
	d=[]
	i=(2*(n-1)+1)**2
	counter = 0
	while counter < 4:
		i += (2*n)
		d.append(i)
		counter += 1
	return d

# 3987
"""
pc_total = 1
print "populating initial primelist"
pl=prime.primeListDb(10000000)
spiral=[1]
print "populating spiral"
primespiral=[]
i=1
primeratio=1
while primeratio>.1:
	spiral+=spiral_diag(i)
	for a in spiral[-4:-2]: # don't need to check the last one because it's always a square
		if pl.isPrime(a): primespiral.append(a)
	primeratio = float(len(primespiral))/float(len(spiral))
	print "{0!s} {1!s}/{2!s}={3!s}".format(2*i+1,len(primespiral),len(spiral),primeratio)
	i+=1
"""

"""
The above will probably work, but I don't want to let it run for long enough. It got up to 50K numbers 
in the diagonals (side length over 25K) and was close but no cigar.

There's gotta be a way I can test faster. I also know I can make it faster by removing the fourth test 
for the # that's always square, but it's the constant prime testing that keeps slowing it down.

It'd be better to start higher and iterate less. I'd have to generate a long prime list, but with the 
DB module now that won't be a dead loss. 

let's try it without the growing arrays. should help memory usage? not needing to count?
"""
import qa
v=qa.v

pc_total = 1
if v:first_tick=tick=qa.tick("generating prime list")
pl=prime.primeListDb(20485513)
if v:tick=qa.tock(tick,"generated")
spiral=[]
nspiral=1.0
if v:tick=qa.tick("generating spiral")
nprimespiral=0.0
i=1
primeratio=1
while primeratio>.1:
    spiral=spiral_diag(i)
    nspiral+=4.0
    for a in spiral[0:3]: # don't need to check the last one because it's always a square
        if pl.isPrime(a): nprimespiral+=1.0
    primeratio = nprimespiral/nspiral
    if v:tick=qa.tock(tick,"{0!s} {1!s}/{2!s}={3!s}".format(2*i+1,nprimespiral,nspiral,primeratio))
    i+=1
if v:_=qa.tock(first_tick,"all done")
pl.done()