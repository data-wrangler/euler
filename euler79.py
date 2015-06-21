"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
import random

keylog=open('keylog.txt','r')
master_keys=[]
for row in keylog:
	master_keys.append(row.strip("\n"))
keylog.close()

# pull a random key
def randkey(keylist):
	return keylist.pop(int(random.random()*(len(keylist))))

# take first key
def simpletest(mykeys):
	keys=list(mykeys)
	password=[]
	while len(keys)>0:
		thiskey=randkey(keys)
		# check whether password already matches
		current_index=0
		for digit in list(thiskey):
			try:
				current_index+=password[current_index:].index(digit)
			except:
				password.insert(current_index+1,digit)
				current_index+=1
	return ''.join(password)

def bettertest(mykeys):
	keys=list(mykeys)
	password=[]
	while len(keys)>0:
		thiskey=randkey(keys)
		current_index=0
		# check whether password already matches
		thispass=[None,None,None]
		i=0
		for digit in list(thiskey):
			try:
				current_index+=password[current_index:].index(digit)
				thispass[i]=current_index
			except:
				pass
			i+=1
	
def validate(mypassword,mykeys):
	for key in mykeys:
		current_index=0
		failure=False
		locations=[]
		for digit in list(key):
			try:
				current_index+=mypassword[current_index:].index(digit)
				locations.append(current_index)
			except:
				failure=True
		if failure:
			print "failed! {0!s} not in {1!s}".format(key,mypassword)
		else:
			print str(mypassword)
			print " "*locations[0]+key[0]+" "*(locations[1]-locations[0]-1)+key[1]+" "*(locations[2]-locations[1]-1)+key[2]

# cases:
# 1. match -> do nothing
# 2. at least one number missing 
# 	a. 1st number missing -> insert at beginning
#	b. 2nd number missing -> insert between 1st and 2nd number
#	c. 3rd number missing -> insert between last number and end

# 7316828090 == 10
# 73162890 == 8