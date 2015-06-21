"""Euler 30: Sum of 5th Powers of their Digits

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.

eg: 1634 = 1**4 + 6**4 + 3**4 + 4**4

Ok, so since 9**5 == 59049, it's unlikely we could get to more than a 
six-digit number. 

there are 5733 combinations of 2 to 6 digits. 
"""

# brute force forward test
res=[]
for i in range(100,1000000):
	fifths=0
	maybe=True
	for digit in str(i):
		fifths+=int(digit)**5
		if fifths>i:
			maybe=False
			break
	if maybe and fifths==i:
		res.append(i)

print res