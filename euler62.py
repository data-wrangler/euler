"""
Euler 62: Cubic Permutations

The cube 41063625 (345**3) can be permuted to produce 2 other cubes:
         56623104 (384**3)
         66430125 (405**3)
         
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are 
also cube. 

Find the smallest cube for which exactly five permutations of its digits are also cube.
"""

from itertools import permutations
import bisect

def dedupe(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def bisearch(x,search_list):
    i=bisect.bisect_left(search_list,x)
    if i != len(search_list) and search_list[i]==x:
        return True
    else:
        return False
        
def unique_sorted_permutations(i):
    p=[int(''.join(x)) for x in permutations(str(i))]
    p=dedupe(p)
    p.sort()
    return p

"""
so I need to go by number of digits at a time. or more realistically, by cubes through each power of ten.

generate list of cubes
for cube:
    unique sorted permutations
    search cubes in permutations
    if n matches
        return cube
        break
"""

import qa
v=qa.v
srt=qa.srt()

i=3
cube_list=[j**3 for j in range(10**i,10**(i+1))]
found_it=False
target_count=5

"""
if v:first_tick=tick=qa.tick("finding cubes with {0!s} permutations between {1!s} and {2!s}".format(target_count,cube_list[0],cube_list[-1]))

for n,cube in enumerate(cube_list):
    srt.tick("permuting")
    cube_permutations=unique_sorted_permutations(cube)
    srt.tock("permuting")
    
    # srt.tick("intersecting")
    # cube_count=len(set(cube_list).intersection(cube_permutations))
    # srt.tock("intersecting")

    cube_count=0

    if len(cube_permutations)>=len(cube_list):
        for test_cube in cube_list:
            srt.tick("searching permutations")
            if bisearch(test_cube,cube_permutations):
                cube_count+=1
            srt.tock("searching permutations")
    else:
        for test_cube in cube_permutations:
            srt.tick("searching cubes")
            if bisearch(test_cube,cube_list):
                cube_count+=1
            srt.tock("searching cubes")

    if cube_count==target_count:
        found_it=True
    if found_it:
        print set(cube_list).intersection(cube_permutations)
        break
    if v and n%10**i==0:tick=qa.tock(tick,"{0!s} cubes tested".format(n))

if v:_=qa.tock(first_tick,"completed")
srt.summary()
"""
"""
generating permutations takes too long. what if I just took the list of cubes, sorted each cube string, and looked for duplicates?
"""

if v:first_tick=tick=qa.tick("sorting cube digits and finding one with {0!s} permutations between {1!s} and {2!s}".format(target_count,cube_list[0],cube_list[-1]))

sorted_cube_list=[]

for cube in cube_list:
    srt.tick("sorting cube digits")
    cube_digits=list(str(cube))
    cube_digits.sort()
    sorted_cube_list.append(int(''.join(cube_digits)))
    srt.tock("sorting cube digits")

srt.tick("deduping")
deduped_cube_list=dedupe(sorted_cube_list)
srt.tock("deduping")

for sorted_cube in deduped_cube_list:
    srt.tick("counting")
    cube_count=sorted_cube_list.count(sorted_cube)
    srt.tock("counting")
    if cube_count>=target_count:
        if v:tick=qa.tock(tick,"found one!")
        for cube, digits in zip(cube_list,sorted_cube_list):
            if digits==sorted_cube:
                print cube

if v:_=qa.tock(first_tick,"completed")
srt.summary()

"""

2015-06-18 14:09:53: found one! in 0.235303 seconds
127035954683
352045367981
373559126408
569310543872
589323567104

"""