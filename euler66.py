"""
Euler 66: Diophantine Equations

Consider quadratic diophantine equations of the form:

    x**2 - Dy**2 == 1

For example, when D=13, the minimal solution is 649**2 - 13*180**2 == 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions for D = {2,3,5,6,7} we obtain the following:

3**2 - 2*2**2 == 1
2**2 - 3*1**2 == 1
9**2 - 5*4**2 == 1
5**2 - 6*2**2 == 1
8**2 - 7*3**2 == 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained 
when D=5.

Find the value of D<=1000 in minimal solutions of x for which the largest value of 
x is obtained.

-----

for each value of d, I want to find the minimal value of x with a solution,
then compare minimal solutions across D to find the one with the largest minimum.

how do I find minimal integer-valued solutions?
1) iteratively
2) formulaically -- eg, the quadratic formula
3) set theory
4) probabilistic/numerical methods

iteratively is easy/slow: for x, for y, check. fuck that.
formulaically, this maps poorly to the quadratic formula because of the y**2; square 
roots and integer testing don't mesh well, but that could be a solid piece of input 
into a more probabilistic or numerical approach.
set theory has a lot of promise. i know that for all D, y<x, and I could approach this 
as a problem on the set of squares rather than integers, which makes it much smaller
and implies faster testing.

x2 - Dy2 == 1
x2 - 1 == Dy2
given x2 in squares, find maximal y2<(x2-1)/d, check if it's exact.



"""

import prime
import bisect
import math
import qa
v=qa.v
srt=qa.srt()

if v:first_tick=qa.tick("Generating primelist...")

p=prime.primeListDb(10000)

if v:tick=qa.tock(first_tick,"Prime list generated")

if v:tick=qa.tick("Generating squares...")
squares=[]

for s in range(100000):
    squares.append(s**2)

if v:tick=qa.tock(tick,"{0!s} initial squares generated".format(len(squares)))

def closest_square(y):
    i=bisect.bisect_right(squares,y)
    if i<len(squares):
        return squares[i-1]
    else:
        i=len(squares)
        while squares[-2]<y:
            squares.append(i**2)
            i+=1
        return closest_square(y)

if v:tick=qa.tick("Starting tests...")

for d in range(1,100):
    if d in squares:
        if v:tick=qa.tock(tick,"{0!s} is square, no solutions.".format(d))
        continue
    if v:tick=qa.tock(tick,"finding solutions of x2 - {0!s}y2 == 1".format(d))
    # x=step = prime.pconstruct([f/2 if f>1 else f for f in prime.pfact(d,p)],p)
    # print "minimum step for {0!s} is {1!s}".format(d,step)
    x=int(math.sqrt(d))
    step=1
    sol=0
    found_solution=False
    while not found_solution and sol < x**2:
        sol=closest_square((x**2-1)/d)
        if x**2-d*sol==1:
            found_solution=True
            if v:tick=qa.tock(tick,"{0!s}**2 - {1!s}*{2!s}**2 == 1".format(x,d,squares.index(sol)))
        x+=step

"""
ok, I was wrong on the x2 =0 mod d theory.

so now I'm just testing everything, which I don't think I need to do, and it's hanging at 61.

according to wolfram alpha, integer solutions for 61 are:
x=1/2(-(1766319049-226153980*math.sqrt(61))**n-(1766319049+226153980*math.sqrt(61))**n)
y=((1766319049-226153980*math.sqrt(61))**n-(1766319049+226153980*math.sqrt(61))**n)/(2*sqrt(61))

so minimally x=1766319049, y=226153980

and that's before they're squared!

Yeah, that's why this one is so hard.

So let's reframe the question: can I map this to a more convenient geometry to facilitate 
solution-finding, or is the plane mandatory for the whole "integer solutions" thing?

right, okay, 
    x**2 - Dy**2 == 1
    (x+sqrt(d)*y)(x-sqrt(d)*y) == 1

there are no integer solutions for D is square: 
    (x+iy)(x-iy)==1
because no two integers multiply to get one.

right. solutions indicate i am mutiplying something by its reciprocal. namely:
    (x+sqrt(d)*y)==1/(x-sqrt(d)*y)
which is only possible when x-sqrt(d)*y<1

"""