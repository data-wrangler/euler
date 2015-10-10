"""
Euler 75: Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form 
an integer sided right angle triangle in exactly one way, but there are many more 
examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
sided right angle triangle, and other lengths allow more than one solution to be 
found; for example, using 120 cm it is possible to form exactly three different 
integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L<1.5*10**6 can 
exactly one integer sided right angle triangle be formed?

notes from 39:

a+b+c=n
a<b<c
a**2+b**2=c**2

n/3 + 1 <= c <= n/2-1
(n-c)/2 <= b <= n-c-1
1 <= a <= b

"""
import qa
v=qa.v
srt=qa.srt()

def findsols(n):
	if v:first_tick=tick=qa.tick("finding right triangles for n={0!s}".format(n))
	sols=[]
	for c in range(n/3+1,n/2):
		for b in range((n-c+1)/2,c):
			a=n-b-c
			# print "%d,%d,%d" % (a,b,c)
			if a**2+b**2==c**2:
				if v:tick=qa.tock(tick,"found solution: [{0!s},{1!s},{2!s}]".format(a,b,c))
				sols.append([a,b,c])
	if v:_=qa.tock(first_tick,"found {0!s} solutions".format(len(sols)))
	return sols

def findones(maxn):
	if v:first_tick=tick=qa.tick("finding single-solution triangles for vales n<={0!s}".format(maxn))
	allones=[]
	for n in range(6,(maxn+1)/2):
		isols=findsols(2*n)
		if len(isols)==1:
			allones.append(2*n)
	if v:_=qa.tock(first_tick,"found {0!s} single-solution values".format(len(allones)))
	return allones

"""
it's fast for low n, but slow up higher. findones(1000) ran 1s, but just findsols(10K) ran in .5s,
and 100K took 57s.

>>> e.findones(1000)
2015-06-23 19:51:23: finding single-solution triangles for vales n<=1000
2015-06-23 19:51:23: finding right triangles for n=12

...
2015-06-23 19:51:24: found 111 single-solution values in 0.959463 seconds
[12, 24, 30, 36, 40, 48, 56, 70, 72, 80, 96, 108, 112, 126, 140, 150, 154, 
156, 160, 176, 182, 192, 198, 200, 204, 208, 216, 220, 224, 228, 234, 260,
276, 286, 306, 308, 320, 324, 340, 348, 350, 352, 364, 372, 374, 378, 380,
384, 392, 400, 416, 418, 442, 444, 448, 476, 490, 492, 494, 516, 532, 544,
564, 572, 594, 598, 608, 636, 640, 644, 646, 648, 650, 696, 702, 704, 708,
714, 732, 736, 744, 748, 750, 768, 782, 784, 798, 804, 832, 836, 850, 852,
858, 874, 876, 882, 884, 888, 896, 928, 930, 948, 950, 966, 972, 980, 984,
986, 988, 992, 996]
>>> e.findsols(10000)
2015-06-23 19:49:35: finding right triangles for n=10000
2015-06-23 19:49:35: found solution: [2000,3750,4250] in 0.167368 seconds
2015-06-23 19:49:35: found 1 solutions in 0.546943 seconds
[[2000, 3750, 4250]]
>>> e.findsols(100000)
2015-06-23 19:49:42: finding right triangles for n=100000
2015-06-23 19:49:57: found solution: [21875,36000,42125] in 15.29851 seconds
2015-06-23 19:49:58: found solution: [20000,37500,42500] in 1.1923 seconds
2015-06-23 19:50:39: found 2 solutions in 57.203703 seconds
[[21875, 36000, 42125], [20000, 37500, 42500]]

there's gotta be an easy pattern here. definitely multiples of 12 for the 3-4-5, and this probably
works for 5-12-13 and 8-15-17. How many indivisible sets are there, and then multiples of them will
also work unless they overlap, in which case there's more than one solution.

can I derive the unique set by running a test and reducing the solutions?

"""
from fractions import gcd
sols=[]

for i in range(12,1000,2):
    i_sols=[sol for sol in findsols(i) if len(sol)>0]
    for [a,b,c] in i_sols:
        g=gcd(a,b)
        g=gcd(g,c)
        this_sol=[a/g,b/g,c/g]
        print "{0!s} -> [{1!s},{2!s},{3!s}] * {4!s}".format(i,a,b,c,g)
        if not this_sol in sols:
            print "that's a new one!"
            sols.append(this_sol)

for sol in sols:
    print sol
    
"""
less than 100:

[3, 4, 5]
[5, 12, 13]
[8, 15, 17]
[7, 24, 25]
[20, 21, 29]
[12, 35, 37]
[9, 40, 41]

less than 1000:
[3, 4, 5]
[5, 12, 13]
[8, 15, 17]
[7, 24, 25]
[20, 21, 29]
[12, 35, 37]
[9, 40, 41]
[28, 45, 53]
[11, 60, 61]
[16, 63, 65]
[33, 56, 65]
[48, 55, 73]
[13, 84, 85]
[36, 77, 85]
[39, 80, 89]
[20, 99, 101]
[65, 72, 97]
[15, 112, 113]
[60, 91, 109]
[44, 117, 125]
[17, 144, 145]
[24, 143, 145]
[88, 105, 137]
[51, 140, 149]
[85, 132, 157]
[19, 180, 181]
[52, 165, 173]
[119, 120, 169]
[57, 176, 185]
[28, 195, 197]
[104, 153, 185]
[95, 168, 193]
[21, 220, 221]
[84, 187, 205]
[133, 156, 205]
[60, 221, 229]
[140, 171, 221]
[32, 255, 257]
[105, 208, 233]
[23, 264, 265]
[120, 209, 241]
[69, 260, 269]
[96, 247, 265]
[115, 252, 277]
[68, 285, 293]
[25, 312, 313]
[160, 231, 281]
[36, 323, 325]
[161, 240, 289]
[75, 308, 317]
[136, 273, 305]
[207, 224, 305]
[27, 364, 365]
[204, 253, 325]
[76, 357, 365]
[175, 288, 337]
[180, 299, 349]
[40, 399, 401]
[225, 272, 353]
[135, 352, 377]
[29, 420, 421]
[152, 345, 377]
[252, 275, 373]
[189, 340, 389]
[120, 391, 409]
[87, 416, 425]
[228, 325, 397]
[84, 437, 445]
[145, 408, 433]
[31, 480, 481]

ok, it'll just keep going up. but still, finding these from a list of squares for i up to 750K
is less terrible than brute force at n**2, right?

I could make a list of all the integer-valued pythagorean triplets with c<750K, sum them, make 
lists of each of their multiples up to 1.5M, then subtract the lists.

"""

squares=[n**2 for n in range(1,750000)]

