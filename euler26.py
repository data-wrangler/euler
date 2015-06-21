"""
A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.

notes:
how do I identify recurring items?
"""

def longdiv(r,d):
	sigs=10000
	q=str(r/d)
	r=r%d
	q+='.'
	for i in range(0,sigs):
		if r==0: break
		q+=str((r*10)/d)
		r=(r*10)%d
	return q

n=range(1,1000)

res=[[],[]]

maxp=0
for i in n:
	s=longdiv(1,i)[2:]
	p=''
	lenp=0
	for c in s:
		p+=c
		lenp+=1
		if s[:lenp*3]==(p+p+p)[:len(s)] and len(s) >= (2*lenp + 1):
			if lenp >= maxp:
				print "1/%d=0.%s repeats phrase of length %d" % (i,s[:12],lenp)
				res[0].append(i)
				res[1].append(lenp)
				maxp=lenp
			break
			
print "longest phrase of length "+max(res[1]).__str__()+" for 1/"+res[0][res.index(max(res[1]))].__str__()
