"""
The prime number 41 can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

import prime as p

pL=p.primeList()
pL.add_til(1000000)

"""
ok, so I need a function that checks below a number n for strings of primes that add to a prime.

starting with the first, keep adding up primes and tracking the ones that add to a prime until you top 
"""

def prime_strings(n,primes):
    res=[]
    max_res=[0,0,0]
    i=0
    while primes.getList()[i]<n:
        # lists starting with i
        this_list=[primes.getList()[i]]
        j=i+1
        while sum(this_list)<n:
            this_list.append(primes.getList()[j])
            if sum(this_list) in primes.getList() and sum(this_list)<n: 
                print "+".join(map(lambda x: str(x),this_list))+"="+str(sum(this_list))
                res.append([sum(this_list),this_list[0],len(this_list)])
                if len(this_list)>max_res[2]: max_res=[sum(this_list),this_list[0],len(this_list)]
            j+=1
        i+=1
    return [res,max_res]
    
[r,max_res]=prime_strings(1000000,pL)
for [n,start,chain] in r:
    print "{0!s}=sum from {1!s} for {2!s}".format(n,start,chain)
print "max: {0!s}=sum from {1!s} for {2!s}".format(max_res[0],max_res[1],max_res[2])

# max: 997651=sum from 7 for 543