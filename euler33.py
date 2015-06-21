"""
Project Euler Problem #33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find 
the value of the denominator. 


notes:
we need only actually consider fractions where one number is shared, of the form:
for a,b,c in [1,9]
ab/ac == b/c
ab/ca == b/c
ba/ac == b/c
ba/ca == b/c

9**3*4 = 2916 cases

"""
sols = []

for a in range(1,10):
	for b in range(1,10):
		for c in range(1,10):
			# print a,b,c
			nums=[float(a*10+b),float(b*10+a)]
			dens=[float(a*10+c),float(c*10+a)]
			for n in nums:
				for d in dens:
					if n/d==float(b)/float(c) and n<d:
						print int(n).__str__()+"/"+int(d).__str__()+"=="+b.__str__()+"/"+c.__str__()
"""
16/64==1/4
26/65==2/5
19/95==1/5
49/98==4/8

4*5*5 = 100
"""