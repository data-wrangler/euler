"""
Euler 54: Poker

In the card game poker, a hand consists of five cards and are ranked, from lowest 
to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest 
value wins; for example, a pair of eights beats a pair of fives (see example 1 
below). But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); if the highest 
cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD 		2C 3S 8S 8D TD	Player 2
		Pair of Fives		Pair of Eights

2	 	5D 8C 9S JS AC		2C 5C 7D 8S QH 	Player 1
		Highest card Ace	Highest card Queen

3	 	2D 9C AS AH AC 		3D 6D 7D TD QD 	Player 2
		Three Aces			Flush with Diamonds

4	 	4D 6S 9H QH QC 		3D 6D 7H QD QS 	Player 1
		Pair of Queens		Pair of Queens
		Highest card Nine	Highest card Seven

5	 	2H 2D 4C 4D 4S 		3C 3D 3S 9S 9D 	Player 1
		Full House			Full House
		With Three Fours	with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the 
first five are Player 1's cards and the last five are Player 2's cards. You 
can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear 
winner.

How many hands does Player 1 win?
"""
import re

f=open('poker.txt','r')
p1=[]
p2=[]
while 1:
	l=f.readline()
	if l:
		p1.append(l.replace('\r\n','').split(' ')[:5])
		p2.append(l.replace('\r\n','').split(' ')[5:])
	else:
		break

#print p1
#print p2

#for i in range(0,10):
#	print p1[i]
#	print p2[i]
#	print (''.join(p1[i]))+' - '+(''.join(p2[i]))

crank={'2':1 \
	,'3':2 \
	,'4':3 \
	,'5':4 \
	,'6':5 \
	,'7':6 \
	,'8':7 \
	,'9':8 \
	,'T':9 \
	,'J':10 \
	,'Q':11 \
	,'K':12 \
	,'A':13 \
	}

"""
Hand Rankings in regex

4K:8,cr
FH:7,cr
3K:4,cr
2P:3,cr,2r,hcr
2K:2,cr,hcr

FL:6,hcr
ST:5,hcr
	SF:9,hcr
HC: 1,cr

"""

fk=re.compile('(?P<cr>[23456789TJQKA]).(?P=cr).(?P=cr).(?P=cr).')
fhl=re.compile('(?P<cr>[23456789TJQKA]).(?P=cr).(?P=cr).(?P<sr>[23456789TJQKA]).(?P=sr).')
fhh=re.compile('(?P<sr>[23456789TJQKA]).(?P=sr).(?P<cr>[23456789TJQKA]).(?P=cr).(?P=cr).')
tk=re.compile('(?P<cr>[23456789TJQKA]).(?P=cr).(?P=cr).')
wp=re.compile('(?P<lc>[23456789TJQKA][SHCD])?(?P<cr>[23456789TJQKA]).(?P=cr).(?P<mc>[23456789TJQKA][SHCD])?(?P<sr>[23456789TJQKA]).(?P=sr).(?P<hc>[23456789TJQKA][SHCD])?')
wk=re.compile('(?P<c1>[23456789TJQKA][SHCD])?(?P<c2>[23456789TJQKA][SHCD])?(?P<c3l>[23456789TJQKA][SHCD])?(?P<cr>[23456789TJQKA]).(?P=cr).(?P<c3h>[23456789TJQKA][SHCD])?(?P<c4>[23456789TJQKA][SHCD])?(?P<c5>[23456789TJQKA][SHCD])?')	
fl=re.compile('.(?P<s>[CSHD]).(?P=s).(?P=s).(?P=s).(?P=s)')
st=re.compile('([23456789TJQKA]).([23456789TJQKA]).([23456789TJQKA]).([23456789TJQKA]).([23456789TJQKA])')


def evaluate(hand):
	hand.sort()
	hstr=''.join(hand)
	
	fks=fk.search(hstr)
	fhls=fhl.search(hstr)
	fhhs=fhh.search(hstr)
	tks=tk.search(hstr)
	wps=wp.search(hstr)
	wks=wk.search(hstr)
	
	if fks:
		return [8,crank[fks.group('cr')]]
	elif fhhs:
		return [7,crank[fhhs.group('cr')],crank[fhhs.group('sr')]]
	elif fhls:
		return [7,crank[fhls.group('cr')],crank[fhls.group('sr')]]
	elif tks:
		return [4,crank[tks.group('cr')]]
	elif wps:
		prs=[crank[wps.group('cr')],crank[wps.group('sr')]]
		prs.sort()
		kicker=crank[max(wps.group('lc'),wps.group('mc'),wps.group('hc'))[0]]
		return [3,prs[1],prs[0],kicker]
	elif wks:
		ocs=[wks.group('c1'),wks.group('c2'),wks.group('c3l'),wks.group('c3h'),wks.group('c4'),wks.group('c5')]
		ors=[]
		for oc in ocs:
			try: ors.append(crank[oc[0]])
			except:pass
		ors.sort()
		ors.reverse()
		return [2,crank[wks.group('cr')]]+ors
	else:
		fls=fl.match(hstr)
		rs=[]
		for c in st.findall(hstr)[0]: rs.append(crank[c])
		rs.sort()
		if rs[0]+4==rs[4] and fl: sr=rs[4]
		elif rs[0]==1 and rs[3]==4 and rs[4]==13: sr=4
		else: sr=None
		if fls and sr:
			return [9,sr]
		elif fls:
			rs.reverse()
			return [6]+rs
		elif sr:
			return [5,sr]
		else:
			rs.reverse()
			return [1]+rs

# test hands
strfl=['4D','5D','6D','7D','8D']
fullboat=['QD','9S','QH','QS','9H']
twopair=['5C','AD','5D','AC','9C']
pairajacks=['JC','JH','QH','KH','8H']
strait=['8C','9D','TC','JD','QS']
lostrait=['AS','2D','3S','4H','5H']
fourtwos=['2S','2H','2D','2C','5D']
threethrees=['3C','TD','3D','3S','QH']
twotens=['TD','QS','TS','3S','4S']
flush=['3H','5H','7H','6H','QH']

def playgames(n):
	res=[]
	for i in range(0,len(p1)):
		one=evaluate(p1[i])
		two=evaluate(p2[i])
		while 1:
			r1=one.pop(0)
			r2=two.pop(0)
			if r1>r2:
				res.append(1)
				break
			elif r1<r2:
				res.append(2)
				break
			elif r1==r2==None:
				res.append(None) 
				break
		if i>=n:
			break
	return res
