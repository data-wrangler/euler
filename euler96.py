"""
Euler 96: Su Doku

Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300

"""

p1=['003020600',\
'900305001',\
'001806400',\
'008102900',\
'700000008',\
'006708200',\
'002609500',\
'800203009',\
'005010300']

solves=[]

class sudoku:
	def __init__(self,puzzle):
		self.grid=[]
		self.couldBe=[]
		self.unsolved=[]
		for cell in puzzle:
			self.grid.append(int(cell))
		cindex=0
		for cell in self.grid:
			if cell==0:
				self.couldBe.append([1,2,3,4,5,6,7,8,9])
				self.unsolved.append([cindex/9,cindex%9])
			else:
				self.couldBe.append(None)
			cindex+=1
		print "Starting Grid:"
		self.printGrid()
		print "Starting Unsolved:"
		print self.unsolved
		print ""
	def getCell(self,r,c):
		# return the value of cell (r,c)
		return self.grid[r*9+c]
	def getRow(self,r):
		# return row r as a list
		if r>8: return None
		return self.grid[r*9:((r+1)*9)]
	def getCol(self,c):	
		# return column c as a list
		if c>8: return None
		col=[]
		for i in range(c,81,9):
			col.append(self.grid[i])
		return col
	def getBox(self,r,c):
		# return values in box (r,c), r,c in (0,2)
		if r>2 or c>2:return None
		box=[]
		for i in range(r*3,(r+1)*3):
			for j in range(c*3,(c+1)*3):
				box.append(self.grid[i*9+j])
		return box
	def printGrid(self):
		# prints the sudoku grid all pretty-like
		r=0;c=0
		row=''
		for cell in self.grid:
			row+=str(cell)
			c=(c+1)%9
			if c==0:
				print row
				row=''
				r+=1
				if r%3==0 and r<9:
					print '---|---|---'
			elif c%3==0:
				row+="|"
	def printUnsolved(self):
		# prints a list of unsolved squares and what they could be
		print "Unsolved:"
		for [r,c] in self.unsolved:
			print "(%d,%d) - %s" % (r,c,self.couldBe[r*9+c])
	def solvePass(self):
		# winnow couldbe list for unsolved squares
		# then solve squares with only one couldBe entry
		if len(self.unsolved)==0:
			return None
		self.solved=0
		self.updated=0
		for [r,c] in self.unsolved:
			thisRow=set(self.getRow(r))
			thisCol=set(self.getCol(c))
			thisBox=set(self.getBox(r/3,c/3))
			cb_was=len(self.couldBe[r*9+c])
			self.couldBe[r*9+c]=list(set(self.couldBe[r*9+c]).difference(thisRow).difference(thisCol).difference(thisBox))
			if len(self.couldBe[r*9+c])<cb_was:self.updated+=1
			if len(self.couldBe[r*9+c])==1:
				self.grid[r*9+c]=self.couldBe[r*9+c][0]
				self.couldBe[r*9+c]=None
				self.unsolved.remove([r,c])
				self.solved+=1
		return self.solved+self.updated
	def solve(self):
		counter=0
		i=0
		self.last81=[0]*80+[1]
		while 1:
			print "Pass %d" % counter
			# self.printGrid()
			self.printUnsolved()
			e=1
			while e>0:
				e=self.solvePass()
				print e
				self.last81=self.last81[1:]+[e]
			if e==0:
				if counter%4==0:o=self.onlyOptionRow(i)
				elif counter%4==1:o=self.onlyOptionCol(i)
				elif counter%4==2:o=self.onlyOptionBox(i/3,i%3)
				else: i=(i+1)%9
			elif e==None: break
			print self.last81[-10:]
			print sum(self.last81)
			if sum(self.last81)==0:
				print "Deadlocked!"
				break
			counter+=1
		print "Final"
		self.printGrid()
		solves.append(self.getCell(0,0)*100+self.getCell(0,1)*10+self.getCell(0,2))
	def onlyOption(self,cellset):
		# solve squares where they're the only place that number can occur in a row/box
		rall=[itm for lst in [self.couldBe[i] for i in cellset] if lst for itm in lst]
		# print rall
		rlist=[]
		for item in set(rall):
			if rall.count(item)==1:
				rlist.append(item)
		# print rlist
		self.solved=0
		for j in rlist:
			for k in cellset:
				if self.couldBe[k]:
					if self.couldBe[k].__contains__(j):
						self.couldBe[k]=None
						self.grid[k]=j
						self.unsolved.remove([k/9,k%9])
						self.solved+=1
						break
		return self.solved
	def onlyOptionRow(self,r):
		thisRow=range(r*9,(r+1)*9)
		res=self.onlyOption(thisRow)
		return res
	def onlyOptionCol(self,c):
		thisCol=range(c,81,9)
		res=self.onlyOption(thisCol)
		return res
	def onlyOptionBox(self,r,c):
		thisBox=[i*9+j for i in range(r*3,(r+1)*3) for j in range(c*3,(c+1)*3)]
		res=self.onlyOption(thisBox)
		return res
			


""" Swaps. The theory is sound, coming back to it.
	def findSwaps(a):
		swaps=[]
		for i in range(0,len(a)):
			if (a[:i]+a[i+1:]).__contains__(a[i]):
				foundwhere=(a[:i]+a[i+1:]).index(a[i])
				if foundwhere>=i: foundwhere+=1
				swaps.append([i,foundwhere])
			else:
				foundwhere=None
		return swaps
	def findSwapsRow(self,r):
		# return row r as a list
		if r>8: return None
		testRow=self.couldBe[r*9:((r+1)*9)]
		rowSwaps=findSwaps(testRow)
		print rowSwaps
		for swap in rowSwaps:
			for i in range(0,9):
				if swap.__contains__(i):
					pass
				if self.couldBe[r*9+i]:
					print "before: "+ self.couldBe[r*9+i].__str__()
					self.couldBe[r*9+i]=list(set(self.couldBe[r*9+i]).difference(set(self.couldBe[r*9+r[0]])))
					print "after: "+ self.couldBe[r*9+i].__str__()
	def findSwapsCol(self,c):	
		# return column c as a list
		if c>8: return None
		col=[]
		for i in range(c,81,9):
			col.append(self.grid[i])
		return col
	def findSwapsBox(self,r,c):
		# return values in box (r,c), r,c in (0,2)
		if r>2 or c>2:return None
		box=[]
		for i in range(r*3,(r+1)*3):
			for j in range(c*3,(c+1)*3):
				box.append(self.grid[i*9+j])
		return box
"""

sudokutxt=open("sudoku.txt","r")

def getPuzzles(f):
	puzzles=[]
	i=-1
	for row in f.readlines():
		if row.__contains__('Grid'):
			puzzles.append('')
			i+=1
		else:
			puzzles[i]+=row.replace('\r\n','')
	return puzzles


puzzles=getPuzzles(sudokutxt)

for puzzle in puzzles:
	p=sudoku(puzzle)
	p.solve()
print solves
print sum(solves)

"""
5
41
42
46
47
48
49
"""