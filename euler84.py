"""
Euler 84: Monopoly

00 GO
01 A1
02 CC -> Draw CC
03 A2
04 T1
05 R1
06 B1
07 CH -> Draw Chance
08 B2
09 B3

10 JAIL
11 C1
12 U1
13 C2
14 C3
15 R2
16 D1
17 CC -> Draw CC
18 D2
19 D3

20 FP
21 E1
22 CH -> Draw Chance
23 E2
24 E3
25 R3
26 F1
27 F2
28 U2
29 F3

30 GJ -> 10
31 G1
32 G2
33 CC -> Draw CC
34 G3
35 RR
36 CH -> Draw Chance
37 H1
38 T2
39 H2

Chances: 7, 22, 36
CCs: 2,17,33
RR: 5, 15, 25, 35
U: 12,28


Community Chest (2/16 cards):
	Advance to GO -> go0
	Go to JAIL ->go10
Chance (10/16 cards):
	Advance to GO -> go0
	Go to JAIL ->go10
	Go to C1 ->go11
	Go to E3 ->go24
	Go to H2 ->go39
	Go to R1 ->go5
	Go to next R (railway company) ->nxr
	Go to next R ->nxr
	Go to next U (utility company) -> nxu
	Go back 3 squares. back3

"""
import random

v=False

snames={
	0:'GO', \
	1:'Medeterranean Ave', \
	2:'Community Chest', \
	3:'Baltic Ave', \
	4:'Income Tax', \
	5:'Reading RR', \
	6:'Oriental Ave', \
	7:'Chance', \
	8:'Vermont Ave', \
	9:'Connecticut Ave', \
	10:'JAIL', \
	11:'St. Charles Pl', \
	12:'Electric Company', \
	13:'States Ave', \
	14:'Virginia Ave', \
	15:'Pennsylvania RR', \
	16:'St James Pl', \
	17:'Community Chest', \
	18:'Tennessee Ave', \
	19:'New York Ave', \
	20:'Free Parking', \
	21:'Kentucky Ave', \
	22:'Chance', \
	23:'Indiana Ave', \
	24:'Illinois Ave', \
	25:'B. & 0. RR', \
	26:'Atlantic Ave', \
	27:'Ventnor Pl', \
	28:'Water Works', \
	29:'Marvin Gardens', \
	30:'Go To Jail!', \
	31:'Pacific Ave', \
	32:'North Carolina Ave', \
	33:'Community Chest', \
	34:'Pennsylvania Ave', \
	35:'Short Line RR', \
	36:'Chance', \
	37:'Park Place', \
	38:'Luxury Tax', \
	39:'Broadway' \
}

class board:
	cccards=['go0','go10']+[None]*14
	chcards=['go0','go10','go11','go24','go39','go5','nxu','bk3']+['nxr']*2+[None]*6
	chances=[7,22,36]
	ccs=[2,17,33]
	def __init__(self):
		# define board
		if v: print "setting up the board"
		if v: print "putting out the chance deck"
		self.chance=deck(self.chcards)
		if v: print "putting out the community chest"
		self.cc=deck(self.cccards)
	def getSquare(self,sq):
		# given a square's index, get instructions
		if sq==30:
			# go to jail
			if v: print "go to jail!"
			return 'go10'
		elif self.chances.__contains__(sq):
			if v: print "draw chance!"
			return self.chance.draw()
		elif self.ccs.__contains__(sq):
			if v: print "draw community chest!"
			return self.cc.draw()
		else:
			return None

class dice:
	def __init__(self,n=6):
		# create 2 dice with n sides
		if v: print "getting two %d-sided dice" % n
		self.sides=n
		random.seed()
	def roll(self):
		# roll the dice, return value
		self.d1=random.randint(1,self.sides)
		self.d2=random.randint(1,self.sides)
		if v: print "rolled a %d and a %d for %d" % (self.d1,self.d2,self.d1+self.d2)
		return self.d1+self.d2
		
class player:
	def __init__(self,aDice,aBoard):
	# create a player at go
		if v: "starting new player on Go"
		self.pos=0
		self.mydice=aDice
		self.myboard=aBoard
	def go(self):
		# roll the dice and get your move
		if v: print "rolling..."
		self.thisRoll=self.mydice.roll()
		self.pos=(self.pos+self.thisRoll)%40
		if v: print "moving to square %d (%s)" % (self.pos,snames[self.pos])
		self.doWhat=self.myboard.getSquare(self.pos)
		if self.doWhat:
			if v: print "oops, gotta " + self.doWhat
			if self.doWhat[:2]=='go':
				self.pos=int(self.doWhat[2:])
			elif self.doWhat=='nxr':
				self.pos=((self.pos+5)%40)/10*10+5
			elif self.doWhat=='nxu':
				if self.pos>12 and self.pos<29: self.pos=28
				else: self.pos=12
			elif self.doWhat=='bk3':self.pos=(self.pos-3)%40
			if v: print "now on square %d (%s)" % (self.pos,snames[self.pos])
		return self.pos
		
class deck:
	def __init__(self,cardset):
	# shuffle deck, set index to -1 (so first draw will pick card 0)
		self.index=-1
		self.cards=[]
		if v: print "shuffling deck"
		while len(cardset)>0:
			self.cards.append(cardset.pop(random.randint(0,len(cardset)-1)))
	def draw(self):
	# get a card
		self.index=(self.index+1)%len(self.cards)
		if v: print "drawing card %d" % self.index
		return self.cards[self.index]

class game:
	def __init__(self,player1):
	# initialize the game
		if v: print "setting up the game"
		self.player=player1
		self.rolls=0
		self.freq=[1]+[0]*39
	def play(self,n):
	# play a game of n rolls
		while self.rolls<n:
			if v: print "roll # %d" % self.rolls
			self.newpos=self.player.go()
			self.freq[self.newpos]+=1
			self.rolls+=1
		return self.freq

def monopolize(n):
	dragonslayers=dice()
	trumpplaza=board()
	matty=player(dragonslayers,trumpplaza)
	endersgame=game(matty)
	counts=endersgame.play(n)
	for i in range(0,len(counts)):
		print '%d : %d' % (i,counts[i])

def mtest(n):
	dragonslayers=dice(4)
	trumpplaza=board()
	matty=player(dragonslayers,trumpplaza)
	endersgame=game(matty)
	counts=endersgame.play(n)
	for i in range(0,len(counts)):
		print '%d : %d' % (i,counts[i])
