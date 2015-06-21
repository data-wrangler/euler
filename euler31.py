"""Euler 31: English currency

How many ways are there to make 2 pounds (200p) with the circulating 
denominations of english currency?

if we could only take one of each denomination then this is the knapsack 
problem we saw before. Since we can take however many we want without breaking 
L2, it gets more complicated. Slightly.

we can take any coin worth d in a number (0,200/d)
200 0 1
100 0 1 2
 50 0 1 2 3 4
 20 (0,10)
 10 (0,20)
  5 (0,40)
  2 (0,100)
  1 (0,200)
  
each coin could be described in combinations of its nearest replacement coins.


so the most efficient way abstractly might be to start at one two-pound coin and 
replace it with each combination possible. This could be iterated, appending to 
the currently known set of sets a new set of sets made by replacing one coin at a 
time from the set with other coins. This would work, and would have the benefit of 
never touching non-L2 sets, but would be highly repetitive and thus slow.

So the real question is how to efficiently cache the number of distinct ways to 
make smaller change, and then leverage knowledge of those numbers to make 
calculating higher values more efficient, and this is where it's definitely a
knapsack problem.

working up: how many ways are there to make:
representing things as [1p,2p,5p,10p,...] so we can ignore denominations above 
our consideration:
1: 1 [1]
2: 2 [2],[0,1]
3: 2 [3],[1,1]
4: 3 [4],[0,2],[2,1]
5: 4 [5],[1,2],[3,1],[0,0,1]

ok, let's take a split approach here: we can use tradeoffs to figure out how many 
ways there are to make change, then we can use a lookup to cache those ways.

"""

p=[1,2,5,10,20,50,100,200]

def count_brute(value,denom,memo):
	print "finding ways to make %d with these coins: %s" % (value,str(denom))
	ways = 0
	i=len(denom)-1
	while i >= 0:
		print "can I subtract %d from %d?" % (denom[i],value)
		if value >= denom[i]:
			print "yes -- is this the last coin?"
			if i==0:
				print "yes -- will it make change"
				if value%denom[i]==0: 
					print "yes"
					memo[i][value]=1
					ways+=1
				else: print "no"
			else:
				print "no -- how many times can I use it?"
				for n in range (1,value/denom[i]+1):
					value_left=value-n*denom[i]
					print "using it %d times leaves %d" % (n,value_left)
					if value_left == 0:
						ways+=1
						print "works cleanly, adding one way. %d so far" % ways
					elif value_left in memo[i]:
						this_ways=memo[i][value_left]
						ways+=this_ways
						print "I've seen this before, there are %d ways to finish. %d so far." % (this_ways, ways)
						# print "used memo:"
						# print memo
					else: 
						print "I haven't seen this before, checking how many ways to finish"
						this_ways=count_brute(value_left,denom[:i],memo)
						memo[i][value_left]=this_ways
						ways+=this_ways
						print "%d so far" % ways
		else: print "no"
		i-=1
	print "found %d ways" % ways
	return ways
	
def count(value,denom):
	global memo
	memo=[]
	for i in range(len(denom)):
		memo.append({0:0})
	return count_brute(value,denom,memo)
	
"""
ways = 0
value = 2
can I add a L2? no
...
can I add a 2? yes
	is this the last coin? no
	for n=1
	value_left = 0
		ways +=1
	i-1
can I add a 1? yes
	is this the last coin?


10:

10
5,5
5,2,2,1
5,2,1,1,1
5,1,1,1,1,1
2,2,2,2,2
2,2,2,2,1,1
2,2,2,1,1,1,1
2,2,1,1,1,1,1,1
2,1,1,1,1,1,1,1,1
1,1,1,1,1,1,1,1,1,1

ec=[1,2,5,10,20]
25:

0,0,1,0,1
1,2,0,0,1
3,1,0,0,1
5,0,0,0,1
0,0,1,2,0
1,2,0,2,0
3,1,0,2,0
5,0,0,2,0
0,0,3,1,0
1,2,2,2,0
3,1,2,2,0
5,0,2,2,0
1,2,2,1,0

{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}
{0: 0, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 4, 8: 1, 10: 1}

"""