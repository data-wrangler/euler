""" Euler 25: First term in the Fibonacci Sequence to have 1,000 digits

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

To my knowledge there isn't a deterministic formula for the nth term of the 
fibonacci sequence... but as terms increase, their ratio approaches phi,
or 1.61803399. 

We can estimate the order of magnitude of the fibonacci sequence somewhere 
by solving out assuming exponents base phi?
"""
"""
import matplotlib.pyplot as pl

def fib(n):
	memo={0:1,1:1}
	return fast_fib(n,memo)

def fast_fib(n,memo):
	if n not in memo:
		memo[n]= fast_fib(n-1,memo)+fast_fib(n-2,memo)
	return memo[n]

fib_one_thousand = []
est_one_thousand = []
phi=1.61803399
for i in range(100):
	fib_one_thousand.append(fib(i))
	est_one_thousand.append(phi**i)

pl.plot(fib_one_thousand)
pl.plot(est_one_thousand)
pl.show()

"""
"""
Ok, so we're overflowing shit now. Clearly there will be no actual 
calculation of thousand-digit numbers tonight. This is a game of the order
of magnitude of the numbers. How fast does the fibonacci sequence gain
orders of magnitude? Is there a deterministic formula for -- not the number,
but the order of magnitude of any digit?

It's exponential, so we should be able to work starting with a knowledge
that clearly 10**1000 is a thousand-digit number. What's the relationship
between orders of magnitude and bases? 10**1000 = 2**? = 1.61803399**??

eg:
log(x,n) == log(x)/log(n)

'cause we know that the nth term of the fibonacci sequence for all n~>66 is 
bounded by (1.61)**n below and (1.62)**n above. If we can solve for when 
these numbers about equal 10**1000, we're in business.

1.61**n == 10**1000
log(1.61**n) == log(10**1000)
n*log(1.61) == 1000*log(10)
n=1000*log(10)/log(1.61)

f(100)+(1.61803399)**n==10**1000
f(100)=3.54225E+20
"""

"""
class of fib with three properties:
	index -- term #
	value -- decomposed to floating-point
	exponent -- scientific notation style 10**n
	needs to know its predecessor
	init returns F2. 
	increment returns next fib
	add adds values, exponents
	getPred, getIndex, getValue, getExponent
"""

class fib:
	def __init__(self,idx=None,pred1=None,pred2=None,val=None,exp=None):
		if idx==None:
			self.index = 2
			self.value=1.0
			self.exponent=0
			self.pred = fib(1,None,None,1.0,0)
		else:
			self.index = idx
			if pred1==None:
				self.value=val
				self.exponent=exp
			else:
				[self.value,self.exponent] = self.fibAdd(pred1,pred2)
			self.pred=pred1
		return None
	def fibAdd(self,fib1,fib2):
		if fib1.getExponent() == fib2.getExponent():
			newVal=fib1.getValue() + fib2.getValue()
			if newVal < 10:
				newExp=fib1.getExponent()
			else:
				newVal/=10
				newExp=fib1.getExponent()+1
		else:
			newVal=fib1.getValue()+fib2.getValue()/10
			newExp=fib1.getExponent()
		return [newVal,newExp]
	def getPred(self):
		return self.pred
	def getIndex(self):
		return self.index
	def getValue(self):
		return self.value
	def getExponent(self):
		return self.exponent
	def increment(self):
		return fib(self.index+1,self,self.pred)
	def printVal(self):
		print self.getValue()*10**self.getExponent()
		
f=fib()
while f.getExponent()<999:
	f=f.increment()
print f.getIndex()
