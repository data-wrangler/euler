"""
Euler 78: coin partitions

Let p(n) represent the number of different ways in which n coins can be separated 
into piles. For example, five coins can separated into piles in exactly seven 
different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

ok, so combinatorics. 

2:
OO
O O

3:
OOO
OO O
O O O

4:
OOOO
OOO O
OO OO
OO O O
O O O O

"""

def fact(n):
	if n>1:
		f=1
		while n>1:
			f*=n
			n-=1
		return f
	else: 
		return 1

def nCr(n,k):
	if n>k:
		return fact(n)/(fact(k)*fact(n-k))
	else:
		return 0

"""
This can reuse the same logic from 76 re: summations.

"""
factor_dict={1:1, 2:2, 3:3, 4:5}

def get_to(target,with_factors_less_than=None):
    if target==0:
        return[[]]
    elif target==1:
        return [[1]]
    all_solutions=[]
    if not with_factors_less_than or target<with_factors_less_than:
        with_factors_less_than=target
    for i in range(with_factors_less_than,0,-1):
        this_solution=[i]
        for rest_of_solution in get_to(target-i,i):
            all_solutions.append(this_solution+rest_of_solution)
    return all_solutions

def n_get_to(target,with_factors_less_than=None):
    if target==0:
        return 1
    elif target==1:
        return 1
    all_solutions=0
    if not with_factors_less_than or target<with_factors_less_than:
        with_factors_less_than=target
    for i in range(with_factors_less_than,0,-1):
        all_solutions+=n_get_to(target-i,i)
    return all_solutions

def fast_get_to(target,with_factors_less_than=None):
    if target==0:
        return 1
    elif target==1:
        return 1
    all_solutions=0
    set_solution=False
    if not with_factors_less_than or target<=with_factors_less_than:
        try:
            all_solutions=factor_dict[target]
            return all_solutions
        except:
            set_solution=True
            with_factors_less_than=target
    for i in range(with_factors_less_than,0,-1):
        all_solutions+=fast_get_to(target-i,i)
    if set_solution:
        factor_dict[target]=all_solutions
    return all_solutions


import qa
v=qa.v
srt=qa.srt()

target_n=50

if v:first_tick=tick=qa.tick("starting factor finding for n up to {0!s}".format(target_n))
for i in range(1,target_n+1):
    if v:tick=qa.tock(tick,"{0!s} = {1!s} additive paths".format(i, fast_get_to(i)))
if v: _=qa.tock(first_tick,"completed")


"""
ugh, except i'm going to need it to be a lot faster to find one that ends with six zeroes.

time to go back to the mathematical approach. There is definitely a pattern here:
    
1 = 1
2 = 2
3 = 3
4 = 5
5 = 7
6 = 11
7 = 15 -- 7=4+3; 15=s(4)*s(3)
8 = 22 -- 8=6+2; 22=s(6)*s(2)
9 = 30 -- 9=4+3+2; 30=s(4)*s(3)*s(2)
10 = 42 -- 10=5+3+2; 42=s(5)*s(3)*s(2)
11 = 56 == 8*7
12 = 77 -- 12=5+6+1; 77=s(5)*s(6)*s(1)
13 = 101 == both prime.
14 = 135 == 3*5*9
15 = 176 == 2*8*11
16 = 231 == 3*7*11
17 = 297 == 3*9*11
18 = 385 == 5*7*11
19 = 490 == 5*7*14
20 = 627 == 3*11*19
21 = 792 == 8*9*11
22 = 1002 == 2*3*167
23 = 1255 == 5*251
24 = 1575 == 7*9*25
50 = 204226
"""