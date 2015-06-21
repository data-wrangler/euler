"""Euler 45: 

An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of 
the following expression.

d1*d10*d100*d1000*d10000*d100000*d1000000

assuming we want to know the nth digit:
log10(n)+1 tells me how many digits the numbers will be into. no! shit.
so n<10 = 1
10<=n<200=2
200<=n<5000=3
...
ok, so it's
(n-1)*10**(n-1) <= x < n*10**n will consist of numbers containing n digits.

91011121314
01111111111
90123456789
"""
def find_n(x):
	n=1
	lsf=9
	while x >= lsf:
		n+=1
		lsf+=9*n*10**(n-1)
	return n,lsf
	
def repdigit(x):
	n,lsf=find_n(x)
	y=(x-lsf+9*n*10**(n-1))/n+10**(n-1)
	i=(x-lsf+9*n*10**(n-1))%n
	return str(y)[i]

digits=[]
digits.append(int(repdigit(0)))
digits.append(int(repdigit(9)))
digits.append(int(repdigit(99)))
digits.append(int(repdigit(999)))
digits.append(int(repdigit(9999)))
digits.append(int(repdigit(99999)))
digits.append(int(repdigit(999999)))

print digits
prod=1
for dig in digits:
	prod*=dig
print prod

def buildString(n):
	res=''
	for i in range(1,n):
		res+=str(i)
	return res
