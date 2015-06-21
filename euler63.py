"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

10**(n-1) >= x**n < 10**n
"""
results=[]
for i in range(1,100):
	for j in range(2,10):
		if len(str(j**i))==i:
			results.append(str(i)+"**"+str(j)+"=="+str(i**j))

for result in results:
	print result
print len(results)