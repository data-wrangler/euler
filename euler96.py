"""
Euler 96: Su Doku

Grid 01
003 020 600
900 305 001
001 806 400

008 102 900
700 000 008
006 708 200

002 609 500
800 203 009
005 010 300

"""

import qa
v=qa.v
srt=qa.srt()

class sudoku:
    # initialize puzzle from text
    def __init__(self,puzzle):
        self.grid=[int(cell) for cell in puzzle]
        self.unsolved=[i for i,cell in enumerate(self.grid) if cell==0]
        self.couldBe=map(lambda x: [1,2,3,4,5,6,7,8,9] if x == 0 else None,self.grid)
        _=self.updatePass()
        if False:
            print "Starting Grid:"
            self.printGrid()
            print "{0!s} unsolved cells".format(len(self.unsolved))
            print ""

    # return puzzle grid as a string
    def getPuzzle(self):
        return ''.join([str(cell) for cell in self.grid])

    # set puzzle grid from a string
    def setPuzzle(self,puzzle_string):
        for old,new in zip(self.grid,[int(cell) for cell in puzzle_string]):
            if old!=new and old!=0:
                print "New puzzle setting contradicts original puzzle!"
        self.grid=[int(cell) for cell in puzzle_string]

    # return indexes of row r as a list
    def getRow(self,r):
        if r>8: return None
        return range(r*9,(r+1)*9)

    # return indexes of column c as a list
    def getCol(self,c):	
        if c>8: return None
        return [i for i in range(81) if i%9==c]

    # return indexes of box (r,c), r,c in (0,2)
    def getBox(self,r,c):
        if r>2 or c>2:return None
        return [i for i in range(81) if (i/3)%3==c and (i/27)==r]

    # prints the sudoku grid all pretty-like
    def printGrid(self):
        row=''
        for i, cell in enumerate(self.grid):
            row+=str(cell)
            if i%9==8:
                print row
                row=''
                if (i/9)%3==2 and i<80:
                    print '---|---|---'
            elif i%3==2:
                row+="|"
        print row

    # prints a list of unsolved squares and what they could be
    def printUnsolved(self):
        print "Unsolved:"
        for i in self.unsolved:
            print "({0!s},{1!s}) - {2!s}".format(i/9,i%9,self.couldBe[i])

    # winnow couldbe list for unsolved squares
    def updatePass(self):
        updated=0
        for i in self.unsolved:
            thisRow=set([self.grid[x] for x in self.getRow(i/9)])
            thisCol=set([self.grid[x] for x in self.getCol(i%9)])
            thisBox=set([self.grid[x] for x in self.getBox(i/27,(i%9)/3)])
            
            cb_was=len(self.couldBe[i] or [])
            self.couldBe[i]=list(set(self.couldBe[i]).difference(thisRow).difference(thisCol).difference(thisBox))
            if len(self.couldBe[i])<cb_was:
                updated+=1
        return updated

    # solve squares with only one couldBe entry
    # or whose couldBe contains a value that doesn't exist elsewhere in the row/col/box
    def solvePass(self):
        if len(self.unsolved)==0:
            return None
        solved=0
        for i in self.unsolved:
            solution=None
            thisRowCouldBe=set([c for x in self.getRow(i/9) if x!=i and self.couldBe[x] for c in self.couldBe[x]])
            thisColCouldBe=set([c for x in self.getCol(i%9) if x!=i and self.couldBe[x] for c in self.couldBe[x]])
            thisBoxCouldBe=set([c for x in self.getBox(i/27,(i%9)/3) if x!=i and self.couldBe[x] for c in self.couldBe[x]])
            
            if len(self.couldBe[i])==1:
                solution=self.couldBe[i][0]
            elif set(self.couldBe[i]).difference(thisRowCouldBe):
                solution=set(self.couldBe[i]).difference(thisRowCouldBe).pop()
            elif set(self.couldBe[i]).difference(thisColCouldBe):
                solution=set(self.couldBe[i]).difference(thisColCouldBe).pop()
            elif set(self.couldBe[i]).difference(thisBoxCouldBe):
                solution=set(self.couldBe[i]).difference(thisBoxCouldBe).pop()
            
            if solution:
                self.grid[i]=solution
                self.couldBe[i]=None
                self.unsolved.remove(i)
                _=self.updatePass()
                solved+=1
        return solved
    
    def probSolve(self):
        for unsolved_cell in self.unsolved:
            for solution_option in self.couldBe[unsolved_cell]:
                print "trying solution with ({0!s},{1!s}) = {2!s}".format(unsolved_cell/9,unsolved_cell%9,solution_option)
                old_puzzle=self.getPuzzle()
                tryPuzzle=sudoku(old_puzzle[:unsolved_cell]+str(solution_option)+old_puzzle[unsolved_cell+1:])
                trySolution=tryPuzzle.solve()
                if trySolution:
                    self.setPuzzle(trySolution)
                    return self.getPuzzle()
        return None

    def solve(self):
        if v:tick=qa.tick()
        counter=0
        solves=1
        while solves>0:
            solves=self.solvePass()
            counter+=1
        if solves==None: 
            if v:tick=qa.tock(tick,"Solved in {0!s} passes".format(counter))
            return self.getPuzzle()
        if v:tick=qa.tock(tick,"Deadlocked in {0!s} passes".format(counter))
        return None

""" 
New solving methods:

Swaps: identify locations where n cells in the same unit each contain the same n numbers; even if 
these cells contain other numbers that aren't explicitly forced out of them, they can't really take
those values because they are the only place where those values could appear.

2-group push: if the only possible cells in a box for some number are in the same row/col, we can 
eliminate other instances of that number in the couldBe list in that row/col.

Probabilistic: try something and see if it solves, if not go back to where you were. effectively 
recursion.

well, probabilistic solving should take care of the rest.
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


solves=[]
i=1
for puzzle in puzzles:
    print "Puzzle {0!s}".format(i)
    p=sudoku(puzzle)
    this_solve=p.solve()
    if this_solve:
        solves.append(int(this_solve[0:3]))
    else:
        this_solve=p.probSolve()
        if this_solve:
            solves.append(int(this_solve[0:3]))
    i+=1
print solves
print sum(solves)
""""""

"""
[483, 245, 462, 137, 523, 176, 143, 487, 814, 761, 976, 962, 397, 639, 697, 361, 359, 786, 743, 782, 428, 425, 348, 124, 361, 581, 387, 345, 235, 298, 761, 132, 698, 852, 453, 516, 945, 365, 134, 193, 814, 384, 469, 316, 586, 954, 159, 861, 294, 351]
24702
"""