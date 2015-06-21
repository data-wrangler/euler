"""
Euler 72: Counting Fractions

Consider the fraction n/d, where n and d are positive integers. If n<d and gcd(n,d)=1, it
is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d<=1000000?

-----

actually, this is similar enough to the ones about euler's phi function that it's worth doing without
listing elements. 

the number of reduced proper fractions less than n is the sum of their phi functions.

but i worry that calculating phi for a million numbers is still too much, because this time I'd 
actually have to do all of them.

phi(n) and phi(2n) are clearly related. actually, this is true for any unique set of primes in a 
factorization independent of exponent. the result will be different, but the multiplier the same.

is prime factorization the actual sticking point? probably, right? that takes more time than the 
iteration and multiplication. 

"""
import sys
import prime
import qa
v=qa.v
srt=qa.srt()

if v:first_tick=tick=qa.tick("generating prime list")
pl=prime.primeList(82500)
if v:tick=qa.tock(tick,"generated primes up to {0!s}".format(pl.getList()[-1]))


max_n=10**6

"""
print "BRUTE CALCULATION OF PHI"

pf_phi_factor={'1':.5}
total_fractions=0

if v:first_tick=tick=qa.tick("calculating phi for integers up to {0!s}".format(max_n))
for i in range(2,max_n+1):
    ipf_phi=prime.phi(i,pl)
    total_fractions+=ipf_phi
    if v and i%10**4==0:tick=qa.tock(tick,"{0!s} reduced proper fractions for denominators less than {1!s}".format(total_fractions,i))

print "total {0!s} reduced proper fractions for denominators less than {1!s}".format(total_fractions,max_n)
if v:_=qa.tock(first_tick,"completed")
srt.summary()
pl.done()
"""

"""
2015-06-15 10:02:55: 2 has 1.0 fractions (via lookup) in 5e-05 seconds
2015-06-15 10:02:55: 3 has 2.0 fractions (generated) in 7.9e-05 seconds
2015-06-15 10:02:55: 4 has 2.0 fractions (via lookup) in 3.9e-05 seconds
2015-06-15 10:02:55: 5 has 4.0 fractions (generated) in 2.9e-05 seconds
2015-06-15 10:02:55: 6 has 2.0 fractions (generated) in 2.6e-05 seconds
2015-06-15 10:02:55: 7 has 6.0 fractions (generated) in 2.8e-05 seconds
2015-06-15 10:02:55: 8 has 4.0 fractions (via lookup) in 8.7e-05 seconds

1+2+2+4+2+6+4=10+5+6=21 looks good.

304191.0    1000    0.042638
1216587.0   2000    0.092228
2736187.0   3000    0.112385
4863601.0   4000    0.135841
7600457.0   5000    0.167297
10943163.0  6000    0.198106
14895145.0  7000    0.223
19455781.0  8000    0.234499
24621517.0  9000    0.270761
30397485.0  10000   0.275927

4 seconds for 1k
6 seconds for 10k
120 seconds for 100k
est 20 minutes for 1m?
revised est: X20mX X1hX 2.5h+ :( got hung up btw 500K-600K

ok, still too slow, mostly on the prime factorizations. gotta do that faster.
~10 pct faster by ignoring powers, but that's not enough.

let's try a different approach: can I dictionary more? the lookups are so much faster, and so many numbers share low factors.

mapping the existence of prime factors to an integer makes for slightly faster dictionarying, and dramatically faster 
calculation of phi! 
down to .88 seconds for 10K and 48 seconds for 100k and it looks like it scales up better, as well.
"""

print "FAST CALCULATION OF PHI"

# pf_phi_factor={0:tuple([1,1]),1:tuple([1,2])}
total_fractions=0

if v:first_tick=tick=qa.tick("calculating phi for integers up to {0!s}".format(max_n))
for i in range(2,max_n+1):
    # srt.tick('fast factoring')
    # ipf=prime.fast_pfact(i,pl)
    # srt.tock('fast factoring')
    # srt.tick('calc phi')
    # ipf_phi_n,ipf_phi_d=prime.fast_phi(ipf,pl)
    # srt.tock('calc phi')
    # srt.tick('add phi to dict')
    # pf_phi_factor[ipf]=tuple([ipf_phi_n,ipf_phi_d])
    # srt.tock('add phi to dict')
    ipf_phi=prime.faster_phi(i,pl)
    total_fractions+=ipf_phi
    if v and i%10**4==0:tick=qa.tock(tick,"{0!s} reduced proper fractions for denominators less than {1!s}".format(total_fractions,i))

print "total {0!s} reduced proper fractions for denominators less than {1!s}".format(total_fractions,max_n)
if v:_=qa.tock(first_tick,"completed")
srt.summary()
pl.done()

"""
    try:
        srt.tick('lookup')
        ipf_phi_n,ipf_phi_d=pf_phi_factor[ipf]
        ipf_phi=i*ipf_phi_n/ipf_phi_d
        srt.tock('lookup')
    except:
"""

"""
Finally!

2015-06-18 06:12:59: generating prime list
2015-06-18 06:13:05: generated primes up to 1055363 in 6.157585 seconds
FAST CALCULATION OF PHI
2015-06-18 06:13:05: calculating phi for integers up to 1000000
2015-06-18 06:13:05: 30397485 reduced proper fractions for denominators less than 10000 in 0.468092 seconds
2015-06-18 06:13:06: 121590395 reduced proper fractions for denominators less than 20000 in 0.963431 seconds
2015-06-18 06:13:08: 273571773 reduced proper fractions for denominators less than 30000 in 1.380436 seconds
2015-06-18 06:13:09: 486345715 reduced proper fractions for denominators less than 40000 in 1.777173 seconds
2015-06-18 06:13:12: 759924263 reduced proper fractions for denominators less than 50000 in 2.161471 seconds
2015-06-18 06:13:14: 1094277505 reduced proper fractions for denominators less than 60000 in 2.485583 seconds
2015-06-18 06:13:17: 1489425819 reduced proper fractions for denominators less than 70000 in 2.790947 seconds
2015-06-18 06:13:20: 1945400165 reduced proper fractions for denominators less than 80000 in 3.070844 seconds
2015-06-18 06:13:24: 2462103829 reduced proper fractions for denominators less than 90000 in 3.574252 seconds
2015-06-18 06:13:27: 3039650753 reduced proper fractions for denominators less than 100000 in 3.74735 seconds
2015-06-18 06:13:32: 3677987867 reduced proper fractions for denominators less than 110000 in 4.310161 seconds
2015-06-18 06:13:36: 4377098665 reduced proper fractions for denominators less than 120000 in 4.510732 seconds
2015-06-18 06:13:41: 5136988725 reduced proper fractions for denominators less than 130000 in 5.16888 seconds
2015-06-18 06:13:46: 5957720031 reduced proper fractions for denominators less than 140000 in 5.010683 seconds
2015-06-18 06:13:52: 6839204027 reduced proper fractions for denominators less than 150000 in 5.418616 seconds
2015-06-18 06:13:57: 7781474123 reduced proper fractions for denominators less than 160000 in 5.519419 seconds
2015-06-18 06:14:03: 8784602677 reduced proper fractions for denominators less than 170000 in 5.971139 seconds
2015-06-18 06:14:09: 9848446267 reduced proper fractions for denominators less than 180000 in 6.214879 seconds
2015-06-18 06:14:16: 10973119597 reduced proper fractions for denominators less than 190000 in 6.530823 seconds
2015-06-18 06:14:23: 12158598917 reduced proper fractions for denominators less than 200000 in 6.856299 seconds
2015-06-18 06:14:30: 13404831445 reduced proper fractions for denominators less than 210000 in 6.921568 seconds
2015-06-18 06:14:37: 14711865643 reduced proper fractions for denominators less than 220000 in 7.400839 seconds
2015-06-18 06:14:44: 16079712169 reduced proper fractions for denominators less than 230000 in 7.278552 seconds
2015-06-18 06:14:52: 17508329291 reduced proper fractions for denominators less than 240000 in 7.494914 seconds
2015-06-18 06:15:00: 18997748543 reduced proper fractions for denominators less than 250000 in 8.028322 seconds
2015-06-18 06:15:08: 20548008117 reduced proper fractions for denominators less than 260000 in 8.207885 seconds
2015-06-18 06:15:17: 22158969143 reduced proper fractions for denominators less than 270000 in 8.609944 seconds
2015-06-18 06:15:26: 23830768963 reduced proper fractions for denominators less than 280000 in 8.972062 seconds
2015-06-18 06:15:35: 25563419637 reduced proper fractions for denominators less than 290000 in 8.975402 seconds
2015-06-18 06:15:43: 27356748483 reduced proper fractions for denominators less than 300000 in 8.774161 seconds
2015-06-18 06:15:53: 29210923797 reduced proper fractions for denominators less than 310000 in 9.433735 seconds
2015-06-18 06:16:02: 31125966023 reduced proper fractions for denominators less than 320000 in 9.253195 seconds
2015-06-18 06:16:12: 33101694809 reduced proper fractions for denominators less than 330000 in 9.484364 seconds
2015-06-18 06:16:22: 35138200379 reduced proper fractions for denominators less than 340000 in 10.397594 seconds
2015-06-18 06:16:33: 37235607123 reduced proper fractions for denominators less than 350000 in 10.815737 seconds
2015-06-18 06:16:43: 39393721051 reduced proper fractions for denominators less than 360000 in 10.63449 seconds
2015-06-18 06:16:55: 41612645735 reduced proper fractions for denominators less than 370000 in 11.385521 seconds
2015-06-18 06:17:06: 43892477939 reduced proper fractions for denominators less than 380000 in 11.234826 seconds
2015-06-18 06:17:18: 46232918759 reduced proper fractions for denominators less than 390000 in 11.624254 seconds
2015-06-18 06:17:29: 48634207309 reduced proper fractions for denominators less than 400000 in 11.65754 seconds
2015-06-18 06:17:41: 51096404425 reduced proper fractions for denominators less than 410000 in 11.76403 seconds
2015-06-18 06:17:53: 53619237565 reduced proper fractions for denominators less than 420000 in 12.346758 seconds
2015-06-18 06:18:06: 56202953459 reduced proper fractions for denominators less than 430000 in 12.638111 seconds
2015-06-18 06:18:18: 58847454067 reduced proper fractions for denominators less than 440000 in 11.92425 seconds
2015-06-18 06:18:31: 61552643223 reduced proper fractions for denominators less than 450000 in 12.791399 seconds
2015-06-18 06:18:43: 64318723779 reduced proper fractions for denominators less than 460000 in 12.414686 seconds
2015-06-18 06:18:56: 67145711075 reduced proper fractions for denominators less than 470000 in 12.817352 seconds
2015-06-18 06:19:09: 70033240847 reduced proper fractions for denominators less than 480000 in 12.528518 seconds
2015-06-18 06:19:21: 72981656485 reduced proper fractions for denominators less than 490000 in 12.716335 seconds
2015-06-18 06:19:34: 75991039675 reduced proper fractions for denominators less than 500000 in 12.781649 seconds
2015-06-18 06:19:47: 79060953399 reduced proper fractions for denominators less than 510000 in 13.080516 seconds
2015-06-18 06:20:02: 82191799955 reduced proper fractions for denominators less than 520000 in 14.692408 seconds
2015-06-18 06:20:16: 85383523301 reduced proper fractions for denominators less than 530000 in 14.630514 seconds
2015-06-18 06:20:32: 88635886235 reduced proper fractions for denominators less than 540000 in 15.24169 seconds
2015-06-18 06:20:47: 91949005039 reduced proper fractions for denominators less than 550000 in 14.902732 seconds
2015-06-18 06:21:02: 95323083863 reduced proper fractions for denominators less than 560000 in 15.622331 seconds
2015-06-18 06:21:18: 98757787365 reduced proper fractions for denominators less than 570000 in 15.989801 seconds
2015-06-18 06:21:35: 102253347209 reduced proper fractions for denominators less than 580000 in 17.143751 seconds
2015-06-18 06:21:52: 105809918237 reduced proper fractions for denominators less than 590000 in 16.632993 seconds
2015-06-18 06:22:09: 109426976721 reduced proper fractions for denominators less than 600000 in 17.171223 seconds
2015-06-18 06:22:26: 113104916297 reduced proper fractions for denominators less than 610000 in 17.239463 seconds
2015-06-18 06:22:43: 116843760409 reduced proper fractions for denominators less than 620000 in 16.54163 seconds
2015-06-18 06:23:00: 120643218537 reduced proper fractions for denominators less than 630000 in 17.102516 seconds
2015-06-18 06:23:19: 124503548345 reduced proper fractions for denominators less than 640000 in 19.114797 seconds
2015-06-18 06:23:37: 128424788117 reduced proper fractions for denominators less than 650000 in 17.879703 seconds
2015-06-18 06:23:58: 132406616309 reduced proper fractions for denominators less than 660000 in 20.488563 seconds
2015-06-18 06:24:19: 136449267065 reduced proper fractions for denominators less than 670000 in 21.676816 seconds
2015-06-18 06:24:41: 140552944927 reduced proper fractions for denominators less than 680000 in 21.596691 seconds
2015-06-18 06:25:03: 144717162695 reduced proper fractions for denominators less than 690000 in 22.01573 seconds
2015-06-18 06:25:21: 148942189539 reduced proper fractions for denominators less than 700000 in 18.146408 seconds
2015-06-18 06:25:39: 153228244333 reduced proper fractions for denominators less than 710000 in 18.419381 seconds
2015-06-18 06:25:57: 157574791521 reduced proper fractions for denominators less than 720000 in 17.781374 seconds
2015-06-18 06:26:16: 161982224459 reduced proper fractions for denominators less than 730000 in 18.315904 seconds
2015-06-18 06:26:34: 166450642565 reduced proper fractions for denominators less than 740000 in 18.382623 seconds
2015-06-18 06:26:53: 170979629893 reduced proper fractions for denominators less than 750000 in 18.85695 seconds
2015-06-18 06:27:11: 175569436425 reduced proper fractions for denominators less than 760000 in 18.216197 seconds
2015-06-18 06:27:30: 180220225265 reduced proper fractions for denominators less than 770000 in 18.927414 seconds
2015-06-18 06:27:49: 184931499247 reduced proper fractions for denominators less than 780000 in 18.945571 seconds
2015-06-18 06:28:08: 189703701285 reduced proper fractions for denominators less than 790000 in 19.247677 seconds
2015-06-18 06:28:27: 194536947223 reduced proper fractions for denominators less than 800000 in 19.420382 seconds
2015-06-18 06:28:47: 199430538751 reduced proper fractions for denominators less than 810000 in 19.821637 seconds
2015-06-18 06:29:08: 204385250463 reduced proper fractions for denominators less than 820000 in 20.732849 seconds
2015-06-18 06:29:28: 209400739121 reduced proper fractions for denominators less than 830000 in 20.398624 seconds
2015-06-18 06:29:49: 214476805833 reduced proper fractions for denominators less than 840000 in 20.531864 seconds
2015-06-18 06:30:10: 219613801853 reduced proper fractions for denominators less than 850000 in 20.554759 seconds
2015-06-18 06:30:30: 224811625977 reduced proper fractions for denominators less than 860000 in 20.572862 seconds
2015-06-18 06:30:51: 230070121307 reduced proper fractions for denominators less than 870000 in 20.973465 seconds
2015-06-18 06:31:12: 235389403827 reduced proper fractions for denominators less than 880000 in 21.331869 seconds
2015-06-18 06:31:34: 240769767131 reduced proper fractions for denominators less than 890000 in 21.975959 seconds
2015-06-18 06:31:56: 246210582787 reduced proper fractions for denominators less than 900000 in 21.851272 seconds
2015-06-18 06:32:18: 251712276989 reduced proper fractions for denominators less than 910000 in 21.717725 seconds
2015-06-18 06:32:40: 257274993307 reduced proper fractions for denominators less than 920000 in 21.891956 seconds
2015-06-18 06:33:02: 262898173125 reduced proper fractions for denominators less than 930000 in 21.897407 seconds
2015-06-18 06:33:24: 268582307087 reduced proper fractions for denominators less than 940000 in 22.529799 seconds
2015-06-18 06:33:48: 274327399259 reduced proper fractions for denominators less than 950000 in 23.521025 seconds
2015-06-18 06:34:13: 280132992121 reduced proper fractions for denominators less than 960000 in 25.3537 seconds
2015-06-18 06:34:38: 285999417123 reduced proper fractions for denominators less than 970000 in 25.102021 seconds
2015-06-18 06:35:02: 291926889519 reduced proper fractions for denominators less than 980000 in 24.108149 seconds
2015-06-18 06:35:27: 297914794719 reduced proper fractions for denominators less than 990000 in 24.851777 seconds
2015-06-18 06:35:51: 303963552391 reduced proper fractions for denominators less than 1000000 in 23.842098 seconds
total 303963552391 reduced proper fractions for denominators less than 1000000
2015-06-18 06:35:51: completed in 1366.230553 seconds
"""