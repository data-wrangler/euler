"""
Euler 74: Digit Factorial Chains

The number 145 is well-known for the property that the sum of the factorial of its digits is equal
to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back up
to 169; it turns out there are only three such loops that exist:
169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 872

It is not difficult to prove that every starting number will eventually get stuck in a loop. For
example,

69 -> 363600 -> 1454 -> 169 -> 36301 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain
with a starting number below one million is sixty terms.

how many chains, with a starting number below one million, contain exactly sixty non-repeating 
terms?

-----

any numbers that share the same set of digits also have the same digit factorial sum.

i can dictionary the facts, then sort the digits of any given number and dictionary the sorted 
digits. has to be as string, though, because zeroes have a factorial of one. 

would it also work to dictionary the length of a known chain once we find it and search those 
first?

the chances are good that it will be one combination of digits that gets the sixty, then i just 
need to know how many distinct permutations of that number -- somewhere south of 720.

"""

fdict={0:1,1:1,2:2}

def fact(n):
	try:
		return fdict[n]
	except:
		fdict[n]=n*fact(n-1)
		return fdict[n]

_=fact(9)

dfdict={'0':1,'1':1}

for k,v in fdict.iteritems():
    dfdict[str(k)]=v

def digit_fact(n):
    ln=list(str(n).replace('0','1'))
    ln.sort
    sn=''.join(ln)
    try:
        return dfdict[sn]
    except:
        dfact=0
        for d in ln:
            dfact+=dfdict[d]
        dfdict[sn]=dfact
        return dfact

def df_cycle(n):
    if n==145:
        return 1
    dfs=[n,digit_fact(n)]
    while digit_fact(dfs[-1]) not in dfs:
        dfs.append(digit_fact(dfs[-1]))
    return len(dfs)

max_df_cycles=0
for i in range(1,1000000):
    dfc=df_cycle(i)
    if dfc>=60:
            max_df_cycles+=1
            print i,dfc

print max_df_cycles

# 402