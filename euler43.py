"""
Euler 43 - Substring Divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

1. start with a list of all 3-digit numbers numbers divisible by 17
2. remove all numbers with duplicated digits.
3. for all remaining numbers, find any digits from the remaining set of unused digits that can be added to the left of the leftmost two digits to create a number divisible by 13.
4. continue through the primes

"""
import copy

nums=[17*i for i in range(100/17+1,1000/17+1)]
my_nums=[]

for num in nums:
	my_digits=num.__str__()
	if my_digits[0]!=my_digits[1] and my_digits[0]!=my_digits[2] and my_digits[1]!=my_digits[2]:
		my_nums.append(num.__str__())

all_digits=list('1234567890')
some_primes=[1,2,3,5,7,11,13]
	
def make_new_list(old_list, divisible_by):
	new_list=[]
	for candidate in old_list:
		available_digits=copy.deepcopy(all_digits)
		for x in list(candidate): available_digits.remove(x)
		for digit in available_digits:
			if int(digit+candidate[:2])%divisible_by==0:
				new_list.append(digit+candidate)
	return new_list

new_list=my_nums

while len(some_primes) > 0 and len(new_list) > 0:
	old_list=new_list
	print "starting list:"
	print old_list
	this_prime=some_primes.pop()
	print "checking next iteration for divisibility by {0!s}".format(this_prime)
	new_list = make_new_list(old_list,this_prime)
	print "new list:"
	print new_list


