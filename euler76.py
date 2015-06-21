"""
Euler 76: Counting Summations

It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

-----

2 = 1 + 1
  = (1)
3 = 2 + 1
    1 + 1 + 1
  = (2)
4 = 3 + 1
    2 + 2
    2 + 1 + 1
    1 + 1 + 1 + 1
  = (4)
5 = (6)
6 = 5 + 1
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
  = (10)
7 = 6 + 1
    5 + 2
    5 + 1 + 1
    4 + 3
    4 + 2 + 1
    4 + 1 + 1 + 1
    3 + 3 + 1
    3 + 2 + 2
    3 + 2 + 1 + 1
    3 + 1 + 1 + 1 + 1
    2 + 2 + 2 + 1
    2 + 2 + 1 + 1 + 1
    2 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1 + 1
  = (14)
    
is it the sum of the previous two?
so let's define s(n) = number of ways to sum n

ok, so n can be written as the sum of two integers in n/2 ways, and then we can break down how many
ways one can write sums to this number based on its biggest factor:
(n-1) + 1 -- that's it
(n-2) + 2 -- can be written s(2)+1 ways
(n-3) + 3 -- can be written s(3)+1 ways
(n-4) + 4 -- can be written s(4)+1 ways
...
(n-i) + i where i < n/2 -- can be written s(i)+1 ways

then the question is how many ways can n be written for largest digit i<(n/2)?

largest digit = 
1: 1
2: n/2 -- as 2s, then each 2 except the first broken down
3: 
let's say n === 0 mod 3:
then it can be written 1 way with all 3s
2**(n/3-1) each 3 except the first can be broken down into 2 sets of factors which multiply?
take 15:
15 = 3 + 3 + 3 + 3 + 3
    3 + 3 + 3 + 3 + 2 + 1
    3 + 3 + 3 + 3 + 1 + 1 + 1
    3 + 3 + 3 + 2 + 2 + 1 + 1
    3 + 3 + 3 + 2 + 1 + 1 + 1 + 1
    ...
so that'd be 1 + 2^4?

ugh ok let's try brute force real quick and come back to the functional approach.
er, not so much brute force as recursive.

trying to get to n:
n-1 + 1
n-2 + all the ways to get 2
...
2 + all the ways to get n-2 with numbers less than or equal to 2
1 * n
"""

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


"""
for i in range(1,50):
    i_solutions=get_to(i)
    # print "i={0!s} has {1!s} solutions:".format(i,len(i_solutions))
    
    first_digits=[0]*i
    for sol in i_solutions:
        first_digits[sol[0]-1]+=1
    for first_digit,solutions_count in enumerate(first_digits):
        if solutions_count%i==0:
            print i, len(i_solutions), first_digit+1, solutions_count

now we're getting somewhere.
for factors n > f >= n/2, solutions s(f)=s(n-f)
for factors n/2 > f >1, solutions:
    s(1)=1
    s(2)=n/2
    s(3)=n/3,4; n,12; 2n,24; 3n,36; 4n,48 -- 12n,144
        =3&4,1 12,12 24,48 36,108 48,192
        =(n/12)*n?
    s(4)=n,11; 9n,48
    s(5)=n,15; 15n,32; 26n,39
    s(12)=4n,25; 8n,28; 258n,48
    s(17)=
"""
factor_dict={1:0, 2:1, 3:2}

def fast_get_to(target):
    try:
        return factor_dict[target]
    except:
        solutions=0
        for i in range(with_factors_less_than,0,-1):
            this_solution=[i]
            for rest_of_solution in get_to(target-i,i):
                all_solutions.append(this_solution+rest_of_solution)
        return all_solutions
