"""Euler 48: Power Series
Find the last ten digits of the sum of n**n n=1,100
ie: 1**1+2**2+3**3+...+999**999+1000**1000

obvs 1000**1000 can be ignored.
I can trim after each multiplication.
This is (n-1)*(n/2) = 999*500 = 499,500 multiplications.
let's try it.
"""
total=0
for i in range(1,1000):
	subtotal=1
	for j in range(1,i+1):
		subtotal*=i
		subtotal=int(str(subtotal)[-10:])
	total+=subtotal
	total=int(str(total)[-10:])
	print total