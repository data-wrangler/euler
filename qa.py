# QA Operations
# All scripts can import these methods and 
#  streamline debugging. the "v" variable
#  can be switched here and will then turn
#  off the verbose qa in all project files.
# Each file should have "v=qa.v"
# 
# Tick is like starting a stopwatch, Tock
#  clicks off a lap. Both handle printing 
#  the specified messages. 
# if v:tick=qa.tick("sorting list")
# > 2012-05-17 10:11:34: sorting list
# if v:tick=qa.tock(tick,"list sorted")
# > 2012-05-17 10:11:36: list sorted in 1.9873 seconds

from datetime import datetime

# v stands for "Verbose mode"
v=True

def tick(msg=None):
	this_tick=datetime.now()
	msg=msg or "starting process"
	print "{0!s}: {1!s}".format(this_tick.strftime("%Y-%m-%d %H:%M:%S"),msg)
	return this_tick

def tock(last_tick,msg=None):
	this_tick=datetime.now()
	msg=msg or "process completed"
	it_took=float((this_tick-last_tick).seconds)+float((this_tick-last_tick).microseconds)/1000000
	print "{0!s}: {1!s} in {2!s} seconds".format(this_tick.strftime("%Y-%m-%d %H:%M:%S"),msg,it_took)
	return this_tick

"""
How would I go about making partial timing functions for subroutines?

eg, in Problem 72 I've got a loop with 5 major operations -- 
1. if i've seen this number before look it up from a dictionary
2. if i haven't, find its prime factorization
    3. reduce prime factorization
    4. calculate phi from prime factorization
    5. add this to the lookup
    
I'd like to know how many times each one is called, and how long each takes.

so the big things I need:
- open-ended naming of subroutines -- has to be part of the call.
- storage of totals by name, so can't just be functions, has to be a class.
- subroutine tick and tock (I can get out of using in-routine variables for timing, no two subs can run simultaneously)
- summary function that returns stats:
    subroutine, calls, total time, avg time

"""
# subroutine timer
class srt(object):
    sr_ticks={}
    sr_calls={}
    sr_times={}
    def __init__(self):
        self.last_tick=datetime.now()
    def tick(self,sub_name):
        self.sr_ticks[sub_name]=datetime.now()
    def tock(self,sub_name):
        this_tick=datetime.now()
        try:
            self.sr_calls[sub_name]+=1
        except:
            self.sr_calls[sub_name]=1
        try:
            self.sr_times[sub_name]+=float((this_tick-self.sr_ticks[sub_name]).seconds)+float((this_tick-self.sr_ticks[sub_name]).microseconds)/1000000
        except:
            self.sr_times[sub_name]=float((this_tick-self.sr_ticks[sub_name]).seconds)+float((this_tick-self.sr_ticks[sub_name]).microseconds)/1000000
        self.sr_ticks[sub_name]=this_tick
    def readable_time(self,time_in_seconds):
        hours, remainder=divmod(time_in_seconds,3600)
        minutes, seconds=divmod(remainder,60)
        return "{0!s}:{1:02d}:{2:09.6f}".format(int(hours),int(minutes),seconds)
    def summary(self):
        print "Summary statistics for {0!s} tracked subroutines:".format(len(self.sr_calls))
        for sr,calls in self.sr_calls.iteritems():
            print "{0!s}: {1!s} calls, {2!s} total (avg {3!s} seconds)".format(sr,calls,self.readable_time(self.sr_times[sr]),self.sr_times[sr]/float(calls))
