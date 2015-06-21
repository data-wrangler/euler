"""
Euler 68: Magic 5-gon Ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, each line adding to nine.

      4
       \
        3
       / \
      1---2---6
     /
    5

working clockwise, and starting from the group of three with the numerically lowest external node, 
(4,3,2 in this example), each solution can be described uniquely. For example, the above solution
can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight
solutions in total.

Total   Solution Set
    9   4,2,3; 5,3,1; 6,1,2
    9   4,3,2; 6,2,1; 5,1,3
   10   2,3,5; 4,5,1; 6,1,3
   10   2,5,3; 6,3,1; 4,1,5
   11   1,4,6; 3,6,2; 5,2,4
   11   1,6,4; 5,4,2; 3,2,6
   12   1,5,6; 2,6,4; 3,4,5
   12   1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon
ring is 432621513
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17- digit
strings. What is the maxiumum 16-digit string for a "magic" 5-gon ring?

# Ugh I can't ascii this thing but it's like the 3 one above with five.

-----

ok, I need to map this to a more linear puzzle, starting with three.

it's two arrays of three for the outer and inner rings, arranged clockwise for convention.

o=[a,b,c]
i=[d,e,f] -->

      a
       \
        d
       / \
      f---e---b
     /
    c

such that:
a+d+e == b+e+f == c+f+d
or o[n]+i[n]+i[(n+1)%3] == k for all n<3

nb: this is rotationally symmetric to:
[b,c,a],[e,f,d]
[c,a,b],[f,d,e]

aha: and when they say "16 digit solutions" vs 17, they mean the ten must be in the outer ring,
which drops the solution space from 10!/5 to 9!

i am guessing that the outer ring contains the high numbers and the inner ring the low? this 
drops the solution space size even further but also makes it impossible to find a solution above
6549...  so I'm going to leave it out of assumtions but lodge the bet.

let's try it for threes and see if it scales up cleanly. it should.
"""

from itertools import permutations,combinations
import qa
v=qa.v
srt=qa.srt()

n=5

if v:first_tick=tick=qa.tick("finding solutions for a magic {0!s}-gon".format(n))

gon_numbers=range(1,n*2+1)
this_perm=0
solutions=[]

outer_gons=[]

for outer_digits in combinations(gon_numbers,n):
    srt.tick("outer gon creation")
    for other_digits in permutations(outer_digits[1:]):
        outer_gon=[outer_digits[0]]
        outer_gon+=other_digits
        outer_gons.append(outer_gon)
    srt.tock("outer gon creation")

for outer_gon in outer_gons:
    for inner_gon in permutations([x for x in gon_numbers if x not in outer_gon],n):
        gon=outer_gon+list(inner_gon)
        
        total=[0]*n
        total[0]=gon[0]+gon[n]+gon[n+1]
        all_the_same=True
    
        srt.tick("solution testing")
        for i in range(1,n):
            total[i]=gon[i]+gon[i+n]+gon[n+(i+1)%n]
            if total[i]!=total[0]:
                all_the_same=False
                break
        srt.tock("solution testing")
    
        if all_the_same:
            srt.tick("solution append")
            this_solution=[]
            for i in range(n):
                this_solution+=[gon[i],gon[i+n],gon[n+(i+1)%n]]
            solutions.append(''.join([str(j) for j in this_solution]))
            if v:tick=qa.tock(tick,"permutation {0!s}:{1!s} is a solution with total {2!s}".format(this_perm,solutions[-1],total[0]))
            srt.tock("solution append")
        this_perm+=1

srt.tick("solution print")
print "Solutions:"
best_solution=0
for solution in solutions:
    best_solution=max(best_solution,int(solution))
    print solution
print "Greatest Solution: {0!s}".format(best_solution)
srt.tock("solution print")

if v:_=qa.tock(first_tick,"completed")
srt.summary()

"""
2015-06-18 20:35:56: finding solutions for a magic 5-gon
2015-06-18 20:35:56: permutation 69:18102107379496568 is a solution with total 19 in 0.006505 seconds
2015-06-18 20:35:56: permutation 2869:11085864693972710 is a solution with total 19 in 0.024828 seconds
2015-06-18 20:35:58: permutation 218949:16103104548782926 is a solution with total 17 in 1.462079 seconds
2015-06-18 20:35:58: permutation 221749:11069627285843410 is a solution with total 17 in 0.018347 seconds
2015-06-18 20:35:59: permutation 412623:27858434106101917 is a solution with total 17 in 1.28292 seconds
2015-06-18 20:35:59: permutation 414565:28797161103104548 is a solution with total 17 in 0.017583 seconds
2015-06-18 20:36:00: permutation 504069:2594936378711015 is a solution with total 16 in 0.631259 seconds
2015-06-18 20:36:00: permutation 506869:2951051817673439 is a solution with total 16 in 0.017935 seconds
2015-06-18 20:36:00: permutation 530227:24105101817673934 is a solution with total 16 in 0.169978 seconds
2015-06-18 20:36:00: permutation 532551:21049436378715110 is a solution with total 16 in 0.014874 seconds
2015-06-18 20:36:01: permutation 722949:6357528249411013 is a solution with total 14 in 1.291969 seconds
2015-06-18 20:36:01: permutation 725749:6531031914842725 is a solution with total 14 in 0.018391 seconds
Solutions:
18102107379496568
11085864693972710
16103104548782926
11069627285843410
27858434106101917
28797161103104548
2594936378711015
2951051817673439
24105101817673934
21049436378715110
6357528249411013
6531031914842725
Greatest Solution: 28797161103104548
2015-06-18 20:36:01: completed in 4.956937 seconds
Summary statistics for 4 tracked subroutines:
solution testing: 725760 calls, 0:00:01.907396 total (avg 2.62813602292e-06 seconds)
outer gon creation: 252 calls, 0:00:00.004951 total (avg 1.96468253968e-05 seconds)
solution append: 12 calls, 0:00:00.000619 total (avg 5.15833333333e-05 seconds)
solution print: 1 calls, 0:00:00.000085 total (avg 8.5e-05 seconds)

"""