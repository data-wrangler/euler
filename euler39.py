"""
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?

a+b+c=n
a<b<c
a**2+b**2=c**2

n/3 + 1 <= c <= n/2-1
(n-c)/2 <= b <= n-c-1
1 <= a <= b

is 3-4-5 the minimal integer-valued right triangle?

"""

def findsols(n):
	sols=[]
	for c in range(n/3+1,n/2):
		for b in range((n-c+1)/2,c):
			a=n-b-c
			# print "%d,%d,%d" % (a,b,c)
			if a**2+b**2==c**2:
				sols.append([a,b,c])
	return sols

def checksols(maxn):	
	ns=[]
	allsols=[]
	lensols=[]
	for n in range(12,maxn):
		isols=findsols(n)
		ns.append(n)
		allsols.append(isols)
		lensols.append(len(isols))
	topn=ns[lensols.index(max(lensols))]
	print topn
	print max(lensols)
	print allsols[lensols.index(max(lensols))]
