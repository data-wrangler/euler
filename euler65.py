"""
Euler 65: 
The square root of 2 can be written as a continued fraction:

sqrt(2) = 1+ 1/ (2+ 1/( 2+ 1/( 2+ 1/( 2+ ... ))))

The infinite continued fraction can be written sqrt(2) = [1;(2)],
(2) indicates that the 2 repeats ad infinitum. In a similar way, 
sqrt(23) = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued
fractions for square roots provide the best rational
approximations. Let us consider the convergents for sqrt(2).

1+1/2 = 3/2
1+1/(2+1/2) = 7/5
1+1/(2+1/(2+1/2)) = 17/12
1+1/(2+1/(2+1/(2+1/2))) = 41/29

Hence the sequence for the first ten convergents of sqrt(2) are:
n= 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, ...
d= 1, 2, 5, 12, 29, 70, 169, 408,  985, 2378, ...

What is most surprising is that the important mathematical
constant,

e=[2;1,2,1,1,4,1,1,6,1, ... ,1,2k,1, ...]

The first ten terms of the sequence of convergents are:
n= 2, 3, 8, 11, 19, 87, 106, 193, 1264, 1457, ...
d= 1, 1, 3,  4,  7, 32,  39,  71,  465,  536, ...

The sum of digits in the numerator of the 10th convergent is 
1+4+5+7=17. 

Find the sum of digits in the numerator of the 100th convergent
of the continued fraction for e.

---

Ok, so I have to back out continued fractions?

I want a function that takes that continued fraction notation and a number of terms
-- so n_terms,starting_int,[set of fractional things] and iterates and returns n,d.

the second part, the iterative part, has to start deep and come back out.
r1: 1/(i+0) -- n1=1,d1=i
r2: 1/(i+[r1]) -- n=d1, d=n1+d1*i
r3: 1/(i+[r2]) ...

"""

def continued_fraction(terms,starting_int,continued_array):
    n=last_n=0
    d=last_d=1
    for i in range(terms,0,-1):
        this_term=continued_array[(i-1)%len(continued_array)]
        n=last_d
        d=last_n+last_d*this_term
        last_d=d
        last_n=n
    n+=d*starting_int
    return n,d

"""
ok, that seems to work.

now I just need to generate the series for e
"""

e_series=[]
i=1
n_iterations=34
while i<=n_iterations:
    e_series+=[1,2*i,1]
    i+=1

n,d=continued_fraction(99,2,e_series)

print n,d

print "digital sum for n:"
ds=0
for k in str(n):
    ds+=int(k)
print ds

# 6963524437876961749120273824619538346438023188214475670667 2561737478789858711161539537921323010415623148113041714756
# digital sum for n:
# 272
