""" Euler 28: Spiral Diagonals
Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

43 44 45 46 47 48 59
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

0: 1
1: skip 1 and add the next 4 times
2: skip 3 and add the next 4 times
3: skip 5 and add the next 4 times
...
n: skip (2n-1) and add the next 4 times
until 500
"""

def spiral_diag(n):
	total_diag = 1
	i=1
	for r in range(1,n):
		counter = 0
		while counter < 4:
			i += (2*r)
			total_diag += i
			counter += 1
	print total_diag

