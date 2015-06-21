"""
Euler 55: Lychrel Numbers

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

"""

def is_palindromic(n):
    sn=str(n)
    is_palindrome=True
    for i in range(len(sn)/2):
        if sn[i] != sn[len(sn)-i-1]:
            is_palindrome=False
            break
    return is_palindrome

def reverse(n):
    sn=str(n)
    rn=''
    for i in range(len(sn)):
        rn+=sn[len(sn)-1-i]
    return int(rn)

def lychrel_iterate(n):
    is_lychrel=True
    i=0
    while i<50 and is_lychrel:
        i+=1
        n=n+reverse(n)
        if is_palindromic(n):
            is_lychrel=False
    return [is_lychrel,i]

def bf_lychrel_test(n):
    n_lychrels=0
    for i in range(1,n+1):
        [is_lychrel,j]=lychrel_iterate(i)
        if is_lychrel:
            print "{0!s}: {1!s} in {2!s} iterations".format(i,is_lychrel,j)
            n_lychrels+=1
    print "{0!s} lychrel numbers found betweel 1 and {1!s}".format(n_lychrels,n)

bf_lychrel_test(10000)

# 249