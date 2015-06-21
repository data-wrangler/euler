
from fractions import gcd
import qa
v=qa.v

max_test=20000
reduced_fractions=0

if v:first_tick=tick=qa.tick("calculating phi for integers up to {0!s}".format(max_test))
for i in range(2,max_test+1):
    start_loop_at=1
    end_loop_at=i-1
    step_by=((i+1)%2)+1
    for j in range(start_loop_at,end_loop_at+1,step_by):
        if gcd(i,j)==1:
            reduced_fractions+=1
            this_fractions+=1
    if v and i%10**4==0:tick=qa.tock(tick,"{0!s} reduced proper fractions for denominators less than {1!s}".format(reduced_fractions,i))

print "total {0!s} reduced proper fractions for denominators less than {1!s}".format(len(reduced_fractions),max_test)
#for f in reduced_fractions:
#    print "{0!s}/{1!s}".format(f[0],f[1])
if v:_=qa.tock(first_tick,"completed")