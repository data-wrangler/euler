"""
The rules for writing Roman numerals allow for many ways of writing each number 
(see About Roman Numerals...). However, there is always a "best" way of writing a 
particular number.

For example, the following represent all of the legitimate ways of writing the number 
sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of 
numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one 
thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, 
they are arranged in descending units and obey the subtractive pair rule (see About Roman 
Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four 
consecutive identical units.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.

2 ways to do this: convert to numeral and back, or grouping reduction.


"""

r={
None:0
,'I':1
,'V':5
,'X':10
,'L':50
,'C':100
,'D':500
,'M':1000
}	

def addNumeral(numeral,value=0):
	nextNumeral=numeral[0]
	try:
		oneAfter=numeral[1]
	except:
		oneAfter=None
	
	if r[nextNumeral]<r[oneAfter]:
		value+=r[oneAfter]-r[nextNumeral]
		numeral=numeral[2:]
	else:
		value+=r[nextNumeral]
		numeral=numeral[1:]
	
	if len(numeral)==0:
		return value
	else:
		return addNumeral(numeral,value)

def makeNumeral(value,numeral=''):
	steps=[{'value':1000, 'letter':'M', 'value-1':100, 'letter-1':'C'}
	,{'value':500, 'letter':'D', 'value-1':100, 'letter-1':'C'}
	,{'value':100, 'letter':'C', 'value-1':10, 'letter-1':'X'}
	,{'value':50, 'letter':'L', 'value-1':10, 'letter-1':'X'}
	,{'value':10, 'letter':'X', 'value-1':1, 'letter-1':'I'}
	,{'value':5, 'letter':'V', 'value-1':1, 'letter-1':'I'}
	,{'value':1, 'letter':'I', 'value-1':0, 'letter-1':''}
	]
	for step in steps:
		numeral+=step['letter']*(value/step['value'])
		value%=step['value']
	
		if value/(step['value']-step['value-1'])==1:
			numeral+=step['letter-1']+step['letter']
			value%=(step['value']-step['value-1'])
	return numeral
