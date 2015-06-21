""" Euler 22: Name Scores
Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the 
alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

shellwork:
$ cat names.txt | awk '{gsub(",","\n"); print}'>names_list.txt
$ cat names_list.txt | sed 's/^/names.append(/;s/$/)/'>euler22_names2.py

"""
from euler22_names2 import names

alpha={'A':1}
alpha['B']=2
alpha['C']=3
alpha['D']=4
alpha['E']=5
alpha['F']=6
alpha['G']=7
alpha['H']=8
alpha['I']=9
alpha['J']=10
alpha['K']=11
alpha['L']=12
alpha['M']=13
alpha['N']=14
alpha['O']=15
alpha['P']=16
alpha['Q']=17
alpha['R']=18
alpha['S']=19
alpha['T']=20
alpha['U']=21
alpha['V']=22
alpha['W']=23
alpha['X']=24
alpha['Y']=25
alpha['Z']=26

namescores=[]
for name in names:
	ns=0
	for letter in name:
		ns+=alpha[letter]
	namescores.append(ns)

totscore=0
for i in range(0,len(namescores)):
	totscore+=(i+1)*namescores[i]
	
print totscore