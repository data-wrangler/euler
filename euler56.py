"""
Euler 56: Powerful Digit Sum

A googol (10**100) is a massive number: a one followed by 100 zeroes. 100**100 is almost unimaginably large. one followed by two hundred zeroes. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form n=a**b, a,b<100, what is the maximum sum of digits?

so it'd have to be all nines, right? or as close to that as I could get with an exponent. if we were only considering
natural numbers less than 100**100 it'd be 100**100-1, or 200 9s, or 9*200 = 1800

it'd be really hard to outweigh the sheer force of high numbers here, so I bet I can only check numbers over eighty or so

"""

def digit_sum(n):
    sn=str(n)
    ds=0
    for i in range(len(sn)):
        ds+=int(sn[i])
    return ds
    
def max_digit_sum(start_a,end_a,start_b,end_b):
    max_ds=0
    for a in range(start_a,end_a+1):
        for b in range(start_b,end_b+1):
            ab=a**b
            ds=digit_sum(ab)
            if ds>max_ds:
                max_ds=ds
                print "{0!s}**{1!s} -> {2!s}".format(a,b,ds)

max_digit_sum(80,99,80,99)

"""
80**80 -> 361
80**85 -> 377
80**89 -> 386
80**94 -> 415
81**80 -> 639
81**81 -> 693
81**83 -> 720
81**85 -> 738
81**86 -> 765
81**89 -> 774
81**90 -> 837
81**94 -> 909
82**98 -> 937
89**99 -> 953
94**98 -> 970
99**95 -> 972
"""