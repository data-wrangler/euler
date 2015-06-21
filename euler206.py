""" Euler 206

Find the unique positive integer which takes the form: 1_2_3_4_5_6_7_8_9_0 
where each "_" is a single digit.

Minimally: sqrt(1020304050607080900) = 1010101010.1010101
Maximally: sqrt(1929394959697989990) = 1389026623.1062636

"""
from math import sqrt


def test_case(nsq):
	# nsq=n**2
	if str(nsq)[0]=='1'\
	and str(nsq)[2]=='2'\
	and str(nsq)[4]=='3'\
	and str(nsq)[6]=='4'\
	and str(nsq)[8]=='5'\
	and str(nsq)[10]=='6'\
	and str(nsq)[12]=='7'\
	and str(nsq)[14]=='8'\
	and str(nsq)[16]=='9'\
	and str(nsq)[18]=='0'\
	and len(str(nsq))==19:
		return True
	else: return False
	
""" 
Has to end in "0", so has to end in "00"
Must be between:
1010101010
and 
1389026620
so:
37,892,561 options

Actually...
has to end in "70" to get the "900"

"""

