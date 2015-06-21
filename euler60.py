"""
Euler 60: Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating 
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four 
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce 
another prime.
"""

import prime
from itertools import combinations, permutations
import time

print time.strftime("%H:%M:%S")+" Generating primelist..."

pl=prime.primeListDb(5761456) # up to 100 million

print time.strftime("%H:%M:%S")+" Prime list generated."

"""
ok, so let's start with four digit primes and replicate the initial experiment.

given any four primes, how many combinations of them are there?

a,b,c,d
    ab,ac,ad
    ba,bc,bd
    ca,cb,cd
    da,db,dc
12= 4*3

(sidenote, then for five primes there are 20)

the brute force approach would be iteratively taking combinations of primes and testing if their 
concatenations were prime until failure

starting from the bottom up means that the first success is the lowest sum. how far should we have 
to go to get this answer?

what number primes are each of the four?
3 = p2
7 = p4
109 = p29
673 = p122

how does the list of iterations grow?
1,2,3,4
1,2,3,5
1,2,4,5
1,3,4,5
2,3,4,5

ok. so let's make a fake lexicon with known placeholders for these primes and see which 
lexicographic combination corresponds to these four.

"""

s='xaxb'+'x'*24+'c'+'x'*92+'d'
q=list(combinations(s,4))
q.index(tuple(['a','b','c','d']))
# 297625

"""
phew, that's a bitch.

would negative definition be easier? identify primes that can be broken into other primes, then look for common factors?
probably not. 

let's try it for all primes up to three digits, comparing to primes up to six digits.

hopefully this will be much faster now that my prime testing is fast.
"""

# define functions for factorial w/ dictionary & nCr
# need these to do skipping

fdict={0:1,1:1,2:2}

def fact(n):
	try:
		return fdict[n]
	except:
		fdict[n]=n*fact(n-1)
		return fdict[n]

def fact_nonrecursive(n):
    return None

def ncr(n,r):
    return fact(n)/fact(r)/fact(n-r)
"""
tick=time.time()
print time.strftime("%H:%M:%S")+" Starting search..."

source_list=pl.getList()[24:168]
source_list.remove(257)
source_list.remove(683)
source_list.remove(103)
source_list.remove(557)
source_combinations=combinations(source_list,5)
ci=0
ti=0

bad_pairs=[]
good_pairs=[]
skip_to=0
c0=0

for combination in source_combinations:
    ci+=1
    red_flags=False
    if combination[0]>c0:
        old_len_bp=len(bad_pairs)
        bad_pairs=[bp for bp in bad_pairs if c0 not in bp]
        new_len_bp=len(bad_pairs)
        print "removed {0!s} bad pairs containing {2!s}, {1!s} remaining.".format(new_len_bp-old_len_bp,new_len_bp,c0)
        c0=combination[0]
    for bp in bad_pairs:
        if len(bp.intersection(combination))==2:
            red_flags=True
            break
    if not red_flags:
        ti+=1
        pi=0
        print "test {2!s} on combination {0!s}: {1!s}".format(ci,combination,ti)
        all_prime=True
        for permutation in permutations(combination,2):
            pi+=1
            if not pl.isPrime(int(''.join([str(x) for x in permutation]))):
                all_prime=False
                bad_pairs.append(set(permutation))
                print "permutation {0!s} is not prime!".format(pi)
                print "added bad pair: {0!s}".format(permutation)
                break
        if all_prime:
            # good_pairs.append(set(permutation))
            print "we have a winner! all permutations of {0!s} are prime.".format(combination)
            for permutation in permutations(combination,2):
                print int(''.join([str(x) for x in permutation]))
            break
# print good_pairs
pl.done()
        
it_took=time.time()-tick
print time.strftime("%H:%M:%S")+" Search Complete"
print "It took {0!s} seconds".format(it_took)
"""

"""
i'm realizing that -- of course -- it's going through the process of eliminating every 
pair of primes. I don't have to check sets of five. I just have to check sets of two, and then 
find a set of five that exists in the functional sets of two.
"""

target_length=5

tick=time.time()
print time.strftime("%H:%M:%S")+" Starting search..."

source_list=pl.getList()[1:1229]
source_list.remove(5)
source_combinations=combinations(source_list,2)
ci=0
pi=0

good_pairs=[]

for combination in source_combinations:
    ci+=1
    if pl.isPrime(int(str(combination[0])+str(combination[1]))) and  pl.isPrime(int(str(combination[1])+str(combination[0]))):
        good_pairs.append(combination)
        pi+=1

pl.done()

print time.strftime("%H:%M:%S")+" Search complete. Found {0!s} prime pairs out of {1!s} combinations".format(pi,ci)
print time.strftime("%H:%M:%S")+" Constructing dictionary..."

link_dict={}
for pair in good_pairs:
    for i in range(2):
        try:
            link_dict[pair[i]].append(pair[(i+1)%2])
        except:
            link_dict[pair[i]]=[pair[i],pair[(i+1)%2]]


print time.strftime("%H:%M:%S")+" Dictionary constructed."

winners=[]
di=0

print time.strftime("%H:%M:%S")+" Testing overlap..."

for k,v in link_dict.iteritems():
    di+=1
    done=False
    print "testing {0!s} combinations in dictionary for {1!s}".format(ncr(len(v)-1,target_length-1),k)
    if len(v)<target_length:
        print "set for {0!s} is too short, skipping it.".format(k)
        continue
    these_combinations=combinations(v,target_length)
    ci=0
    for combination in these_combinations:
        if k in combination:
            ci+=1
            overlap_set=set(link_dict[combination[0]])
            overlap_set.add(long(k))
            i=1
            while i<len(combination) and len(overlap_set)>=target_length:
                overlap_set=overlap_set.intersection(link_dict[combination[i]])
                i+=1
            if len(overlap_set)>=target_length:
                print "we have a winner! {0!s}".format(overlap_set)
                winners.append(overlap_set)

print time.strftime("%H:%M:%S")+" Overlapping complete."

min_sum=1000000
min_winner=winners[0]
# prove it!
for winner in winners:
    pi=0
    # print "testing combination: {0!s}".format(winner)
    all_prime=True
    for permutation in permutations(winner,2):
        pi+=1
        if not pl.isPrime(int(''.join([str(x) for x in permutation]))):
            all_prime=False
            # print "permutation {0!s} is not prime!".format(permutation)
            break
    if all_prime:
        print "confirmed! all permutations of {0!s} are prime.".format(winner)
        print sum(winner)
        if sum(winner) < min_sum:
            min_sum=sum(winner)
            min_winner=winner


print "minimum sum: {0!s}".format(min_sum)
print min_winner
for permutation in permutations(min_winner,2):
    print int(''.join([str(x) for x in permutation]))

it_took=time.time()-tick
print time.strftime("%H:%M:%S")+" Search Complete"
print "It took {0!s} seconds".format(it_took)

"""
minimum sum: 26033
set([6733L, 5701L, 8389L, 5197L, 13L])
67335701
67338389
67335197
673313
57016733
57018389
57015197
570113
83896733
83895701
83895197
838913
51976733
51975701
51978389
519713
136733
135701
138389
135197
20:25:03 Search Complete
It took 746.678045988 seconds
"""