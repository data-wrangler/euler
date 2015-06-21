"""
Euler 61: Cyclical Figurate Numbers

Triangle, square, pentagonal, hexagonal, heptagonal and octagonal numbers are all figurate 
(polygonal) numbers and are generated by the following formulae:

Triangle    P3,n = n*(n+1)/2    1, 3, 6, 10, 15, ...
Square      P4,n = n**2         1, 4, 9, 16, 25, ...
Pentagonal  P5,n = n*(3n-1)/2   1, 5, 12, 22, 35, ...
Hexagonal   P6,n = n*(2n-1)     1, 6, 15, 28, 45, ...
Heptagonal  P7,n = n*(5n-3)/2   1, 7, 18, 34, 55, ...
Octagonal   P8,n = n*(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three four-digit numbers: 8128, 2882, 8281, has three interesting properties:
1. the set is cyclic, in that the last two digits of each number is the first two digits of the
next number (including the last number with the first)
2. each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
is represented by a different number in the set.
3. this is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal and octagonal is represented by a different
number in the set.

-----

the set of four digit numbers is small, and its intersection with figurates is smaller still, so
this should be easy.

1. generate lists of four-digit numbers in each figurate set
2. winnow lists iteratively by removing any that don't have extant 2-digit overlaps with elements the preceding/succeeding set.
3. if this yields more than one set, test. 

except they don't have to go in order :/
there are 720 permutations of 345678
the good news is this test ran in .004s

"""
import qa
v=qa.v
srt=qa.srt()

if v:first_tick=qa.tick("finding cyclical figurate sets")

# octagonal hits 4-digit first, so lower bound of i is 19 (oc[19]==1045)
# triangle hits 5-digit last, so upper bound of i is 40 (tr[140]==9870)

if v:tick=qa.tick("generating figurate sets")

clean_fsets=[[],[],[],[],[],[]]

for i in range(19,141):    
    tr_i=i*(i+1)/2
    if tr_i>=10**3 and tr_i<10**4:
        clean_fsets[0].append(tr_i)
    sq_i=i**2
    if sq_i>=10**3 and sq_i<10**4:
        clean_fsets[1].append(sq_i)
    pn_i=i*(3*i-1)/2
    if pn_i>=10**3 and pn_i<10**4:
        clean_fsets[2].append(pn_i)
    hx_i=i*(2*i-1)
    if hx_i>=10**3 and hx_i<10**4:
        clean_fsets[3].append(hx_i)
    hp_i=i*(5*i-3)/2
    if hp_i>=10**3 and hp_i<10**4:
        clean_fsets[4].append(hp_i)
    oc_i=i*(3*i-2)
    if oc_i>=10**3 and oc_i<10**4:
        clean_fsets[5].append(oc_i)

if v:tick=qa.tock(tick,"figurate sets generated")
if v:print "tr: {0!s}".format(len(clean_fsets[0]))
if v:print "sq: {0!s}".format(len(clean_fsets[1]))
if v:print "pn: {0!s}".format(len(clean_fsets[2]))
if v:print "hx: {0!s}".format(len(clean_fsets[3]))
if v:print "hp: {0!s}".format(len(clean_fsets[4]))
if v:print "oc: {0!s}".format(len(clean_fsets[5]))

# ok, got my lists.

def dedupe(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def winnow(first_list,second_list):
    new_first_list=[]
    new_second_list=[]
    for i,fl in enumerate([str(a)[-2:] for a in first_list]):
        for j,sl in enumerate([str(b)[:2] for b in second_list]):
            if fl==sl:
                new_first_list.append(first_list[i])
                new_second_list.append(second_list[j])
    return dedupe(new_first_list), dedupe(new_second_list)

from itertools import permutations

perms=permutations([int(o) for o in '012345'],6)

# map_order=[int(o) for o in '012345']

for map_order in perms:
    if v:tick=qa.tick("testing map order {0!s}".format(map_order))
    fsets=[list(l) for l in clean_fsets]
    wp=0
    last_len=[0]*len(fsets)
    while  last_len!=[len(fsets[i]) for i in range(len(fsets))]:
    
        last_len=[len(fsets[i]) for i in range(len(fsets))]
    
        for i in range(len(fsets)):
            fsets[map_order[i-1]],fsets[map_order[i]] = winnow(fsets[map_order[i-1]],fsets[map_order[i]])

        if v:tick=qa.tock(tick,"winnowing pass {0!s} for map {1!s} completed".format(wp,''.join([str(x) for x in map_order])))
        if v:print "tr:{0!s}->{1!s} sq:{2!s}->{3!s} pn:{4!s}->{5!s} hx:{6!s}->{7!s} hep:{8!s}->{9!s} oct:{10!s}->{11!s}".format(last_len[0],len(fsets[0]),last_len[1],len(fsets[1]),last_len[2],len(fsets[2]),last_len[3],len(fsets[3]),last_len[4],len(fsets[4]),last_len[5],len(fsets[5]))
    
        wp+=1
    if last_len > [0]*len(fsets):
        break

if v:_=qa.tock(first_tick,"completed")
print "tr:{0!s}".format(fsets[0])
print "sq:{0!s}".format(fsets[1])
print "pn:{0!s}".format(fsets[2])
print "hx:{0!s}".format(fsets[3])
print "hp:{0!s}".format(fsets[4])
print "oc:{0!s}".format(fsets[5])

"""

2015-06-18 17:14:05: testing map order (0, 1, 4, 5, 3, 2)
2015-06-18 17:14:05: winnowing pass 0 for map 014532 completed in 0.002571 seconds
tr:96->24 sq:68->7 pn:56->1 hx:48->1 hep:43->1 oct:40->1
2015-06-18 17:14:05: winnowing pass 1 for map 014532 completed in 0.000112 seconds
tr:24->1 sq:7->1 pn:1->1 hx:1->1 hep:1->1 oct:1->1
2015-06-18 17:14:05: winnowing pass 2 for map 014532 completed in 0.000138 seconds
tr:1->1 sq:1->1 pn:1->1 hx:1->1 hep:1->1 oct:1->1
2015-06-18 17:14:05: completed in 0.05395 seconds
tr:[8256]
sq:[5625]
pn:[2882]
hx:[8128]
hp:[2512]
oc:[1281]

"""