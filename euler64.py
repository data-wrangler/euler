"""
Euler 64: Odd Period Square Roots

All square roots are periodic when written as continued fractions and can be
written in the form:

sqrt(n) = a0 + 1 / ( a1 + 1 / ( a2 + 1 / (a3 + ... )))

For example, let us consider sqrt(23):

sqrt(23) = 4 + sqrt(23) - 4
         = 4 + 1 / ( 1 / sqrt(23) - 4 ))
         = 4 + 1 / ( 1 + ( sqrt(23) - 3 ) / 7)

If we continue we would get the following expansion:

sqrt(23) = 4 + 1 / ( 1 + 1 / ( 3 + 1 / ( 1 + 1 / ( 8 + ... ))))

The process can be summarised as follows:

a0 = 4, 1 / ( sqrt(23) - 4 ) = (sqrt(23) + 4) / 7 = 1 + ( sqrt(23) - 3) / 7
a1 = 1, 7 / ( sqrt(23) - 3 ) = 7*(sqrt(23) + 3) / 14 = 3 + ( sqrt(23) - 3) / 2
a2 = 3, 2 / ( sqrt(23) - 3 ) = 2*(sqrt(23) + 3) / 14 = 1 + ( sqrt(23) - 4) / 7
a3 = 1, 7 / ( sqrt(23) - 4 ) = 7*(sqrt(23) + 4) / 7 = 8 + ( sqrt(23) - 4)
a4 = 8, 1 / ( sqrt(23) - 4 ) = (sqrt(23) + 4) / 7 = 1 + ( sqrt(23) - 3) / 7
a5 = 1, 7 / ( sqrt(23) - 3 ) = 7*(sqrt(23) + 3) / 14 = 3 + ( sqrt(23) - 3) / 2
a6 = 3, 2 / ( sqrt(23) - 3 ) = 2*(sqrt(23) + 3) / 14 = 1 + ( sqrt(23) - 4) / 7
a7 = 1, 7 / ( sqrt(23) - 4 ) = 7*(sqrt(23) + 4) / 7 = 8 + ( sqrt(23) - 4)

It can be seen that the sequence is repeating. For conciseness, we use the 
notation sqrt(23) = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) 
repeats indefinitely.

The first ten continued fractions of (irrational) square roots are:

sqrt(2)=[1;(2)], period=1
sqrt(3)=[1;(1,2)], period=2
sqrt(5)=[2;(4)], period=1
sqrt(6)=[2;(2,4)], period=2
sqrt(7)=[2;(1,1,1,4)], period=4
sqrt(8)=[2;(1,4)], period=2
sqrt(10)=[3;(6)], period=1
sqrt(11)=[3;(3,6)], period=2
sqrt(12)=[3;(2,6)], period=2
sqrt(13)=[3;(1,1,1,1,6)], period=5

Exactly four fractions, for n<=13, have an odd period.

How many continued fractions for n <= 10000 have an odd period?

-----

ok, here's what we need to do:
a0 = 4, 1 / ( sqrt(23) - 4 ) = 1*(sqrt(23) + 4) / 7 = 1 + ( sqrt(23) - 3) / 7
a1 = 1, 7 / ( sqrt(23) - 3 ) = 7*(sqrt(23) + 3) / 14 = 3 + ( sqrt(23) - 3) / 2
a2 = 3, 2 / ( sqrt(23) - 3 ) = 2*(sqrt(23) + 3) / 14 = 1 + ( sqrt(23) - 4) / 7


n[i] = d[i-1] * ( sqrt(23) + n[i-1] )
d[i] = ( sqrt(23) - n[i-1] ) * ( sqrt(23) + n[i-1] ) = 23 - n[i-1]**2

so generating the continued fraction numbers works by inverting fractional
remainders:

of the form:
r = (ni) / (sqrt(x) - di) = a[i+1] + (sqrt(x)-nri)/dri

a0=int(sqrt(x))
d0=a0
n0=1

a1=int(nr0/dr0)
dr0 = x - d0**2
nr0 = d0-(a1*dr0)/n0

n1 = n0-(a1*dr0)/n0
d1 = d*(x - d0**2)

"""
import math
from fractions import gcd

def continued_fraction(continued_array):
    n=last_n=0
    d=last_d=1
    for i in range(len(continued_array),1,-1):
        this_term=continued_array[(i-1)%len(continued_array)]
        n=last_d
        d=last_n+last_d*this_term
        last_d=d
        last_n=n
    n+=d*continued_array[0]
    return n,d

def cf_sqrt(x,terms):
    # print "finding ther first {0!s} terms of sqrt({1!s})".format(terms,x)
    a=[int(math.sqrt(x))]
    d=1
    n=-a[0]
    
    # print "term 0: {0!s} + (sqrt({1!s}) + {2!s})/{3!s}".format(a[0],x,n,d)
    
    for i in range(1,terms):
        try:
            a.append(int(d/(math.sqrt(x)+n)))
        except ZeroDivisionError:
            break
        new_d=(x-n**2)/d
        new_n=-n-(a[i]*(x-n**2))/d
        d=new_d
        n=new_n
        # print "term {0!s}: {1!s} + (sqrt({2!s}) + {3!s})/{4!s}".format(i,a[i],x,n,d)
    return a

# cf_sqrt(2,10)
# cf_sqrt(3,10)
# cf_sqrt(7,10)
# cf_sqrt(8,10)
# cf_sqrt(11,10)
# cf_sqrt(12,10)
# cf_sqrt(23,10)

"""
so now I have to identify cycles.

"""

def cycle_period(a):
    for i in range(1,len(a)/2):
        if a==(a[:i]*(len(a)/i+1))[:len(a)]:
            return i
    return None

terms_to_check=1000
odd_periods=0
unidentified=0

for n in range(1,100):
    n_cf_sqrt=cf_sqrt(n,terms_to_check+1)
    if len(n_cf_sqrt)<terms_to_check+1:
        print "{0!s} is rational -- ends at {1!s} terms".format(n,len(n_cf_sqrt))
    else:
        n_cycle=cycle_period(n_cf_sqrt[1:])
        if n_cycle:
            print "{0!s} has a cycle of {1!s}, sqrt({0!s})={2!s}".format(n,n_cycle,n_cf_sqrt[:n_cycle+1])
            if n_cycle%2==1:
                odd_periods+=1
        else:
            print "{0!s} has no cycles identifiable in {1!s} terms!".format(n,terms_to_check)
            unidentified+=1

print "found {0!s} numbers with odd-period roots".format(odd_periods)
print "found {0!s} numbers without identified cycle periods".format(unidentified)

# found 1322 numbers with odd-period roots
# found 0 numbers without identified cycle periods