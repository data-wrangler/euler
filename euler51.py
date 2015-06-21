"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

import prime

pL = prime.primeList()
#pL.add_til(1000000)
#print "prime list generated up to 1M."

pL.add_til(10000000)
print "prime list generated up to 10M."

"""
ok, so starting with 5-digit primes ~50K containing two of the same number find a set for which eight of ten digit replacements exist.

there are 999 variations of 3 digits, call them xyz, and * is our number to change up.
xyz**
xy*z*
xy**z
x*yz*
x*y*z
x**yz
*xyz*
*xy*z
*x*yz
**xyz

10 permutations, but I can strike the ones with the last digit variable, because there's no way 8/10 are prime, so we're down to 6.

xy**z
x*y*z
x**yz
*xy*z
*x*yz
**xyz

so z is the last digit, and I really only need to check it for primeable last digits, 1379. the others can be any digit.

10*10*4*6*10=24000 total checks.

not too bad.

"""
import itertools

# all permutations of xyz
a=list(itertools.chain.from_iterable(map(lambda l:map(lambda p:p+l,[str(x) for x in range(0,10)]),[str(x) for x in range(0,10)])))
a=list(itertools.chain.from_iterable(map(lambda l:map(lambda p:p+l,a),[str(x) for x in [1,3,7,9]])))

# i'll need something to perform mapping.
def map_array_to_int(input_array,mapping_array):
    output=[]
    for i in range(0,len(mapping_array)):
        output.append(input_array[mapping_array[i]])
    return int(''.join([str(x) for x in output]))

"""
# and here are my possible maps for two digit replacement
maps = [[0,1,3,3,2]
    , [0,3,1,3,2]
    , [0,3,3,1,2]
    , [3,0,1,3,2]
    , [3,0,3,1,2]
    , [3,3,0,1,2]]
"""

# and here are my possible maps for three-digit replacement
maps = [[0,1,3,3,3,2]
, [0,1,3,3,3,2]
, [0,1,3,3,3,2]
, [0,3,1,3,3,2]
, [0,3,1,3,3,2]
, [0,3,1,3,3,2]
, [0,3,3,1,3,2]
, [0,3,3,1,3,2]
, [0,3,3,1,3,2]
, [0,3,3,3,1,2]
, [0,3,3,3,1,2]
, [0,3,3,3,1,2]
, [1,0,3,3,3,2]
, [1,0,3,3,3,2]
, [1,0,3,3,3,2]
, [1,3,0,3,3,2]
, [1,3,0,3,3,2]
, [1,3,0,3,3,2]
, [1,3,3,0,3,2]
, [1,3,3,0,3,2]
, [1,3,3,0,3,2]
, [1,3,3,3,0,2]
, [1,3,3,3,0,2]
, [1,3,3,3,0,2]
, [3,0,1,3,3,2]
, [3,0,1,3,3,2]
, [3,0,1,3,3,2]
, [3,0,3,1,3,2]
, [3,0,3,1,3,2]
, [3,0,3,1,3,2]
, [3,0,3,3,1,2]
, [3,0,3,3,1,2]
, [3,0,3,3,1,2]
, [3,1,0,3,3,2]
, [3,1,0,3,3,2]
, [3,1,0,3,3,2]
, [3,1,3,0,3,2]
, [3,1,3,0,3,2]
, [3,1,3,0,3,2]
, [3,1,3,3,0,2]
, [3,1,3,3,0,2]
, [3,1,3,3,0,2]
, [3,3,0,1,3,2]
, [3,3,0,1,3,2]
, [3,3,0,1,3,2]
, [3,3,0,3,1,2]
, [3,3,0,3,1,2]
, [3,3,0,3,1,2]
, [3,3,1,0,3,2]
, [3,3,1,0,3,2]
, [3,3,1,0,3,2]
, [3,3,1,3,0,2]
, [3,3,1,3,0,2]
, [3,3,1,3,0,2]
, [3,3,3,0,1,2]
, [3,3,3,0,1,2]
, [3,3,3,0,1,2]
, [3,3,3,1,0,2]
, [3,3,3,1,0,2]
, [3,3,3,1,0,2]]

broken=False
# for each permutation of xyz
for [x,y,z] in a:
    # for each possible arrangement of digits
    for mapping_array in maps:
        mapped_numbers=[]
        prime_success=[]
        # check each value of digits for primality
        for i in range(0,10):
            j=map_array_to_int([x,y,z,i],mapping_array)
            # if j<100000: break
            mapped_numbers.append(j)
            prime_success.append(j in pL.getList())
        if prime_success.count(True) >= 8:
            print mapped_numbers
            print prime_success
            broken=True
            break
    if broken:
        break


"""
ok, it's not less than a million. gotta go to six digit numbers.

so now i've got wxyz.

wxy**z
wx*y*z
wx**yz
w*xy*z
w*x*yz
w**xyz
*wxy*z
*wx*yz
*w*xyz
**wxyz

and we're at 10*10*10*4*10*10=400000

oof.

"""

"""
# all permutations of wxyz
b=list(itertools.chain.from_iterable(map(lambda l:map(lambda p:p+l,[str(x) for x in range(0,10)]),[str(x) for x in range(0,10)])))
b=list(itertools.chain.from_iterable(map(lambda l:map(lambda p:p+l,b),[str(x) for x in range(0,10)])))
b=list(itertools.chain.from_iterable(map(lambda l:map(lambda p:p+l,b),[str(x) for x in [1,3,7,9]])))


# and here are my possible maps for two-digit replacement
maps = [[0,1,2,4,4,3]
    , [0,1,4,2,4,3]
    , [0,1,4,4,2,3]
    , [0,4,1,2,4,3]
    , [0,4,1,4,2,3]
    , [0,4,4,1,2,3]
    , [4,0,1,2,4,3]
    , [4,0,1,4,2,3]
    , [4,0,4,1,2,3]
    , [4,4,0,1,2,3]]

# and here are my possible maps for one-digit replacement
maps = [[0,1,2,4,3]
    , [0,1,4,2,3]
    , [0,4,1,2,3]
    , [4,0,1,2,3]]

broken=False
# for each permutation of wxyz
for [w,x,y,z] in b:
    # for each possible arrangement of digits
    for mapping_array in maps:
        mapped_numbers=[]
        prime_success=[]
        # check each value of digits for primality
        for i in range(0,10):
            j=map_array_to_int([w,x,y,z,i],mapping_array)
            mapped_numbers.append(j)
            prime_success.append(j in pL.getList())
        if prime_success.count(True) >= 8:
            print mapped_numbers
            print prime_success
            broken=True
            break
    if broken:
        break
    """

"""
ok... so looking at the question again, I don't think the replacement is limited to 2 digits.

This means I can check 1 digit replacement with the 4-digit list.

Nothing.

And 3-digit on the 3-digit list.

Bingo.

"""

