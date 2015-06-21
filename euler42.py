"""Euler 42: Triangle Words

Using similar methodology to 22, word scores.
"""
from euler42_words import words

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

wordscores=[]
for word in words:
	ws=0
	for letter in word:
		ws+=alpha[letter]
	wordscores.append(ws)

tri_cap = max(wordscores)

tris=[1]
i=2
while max(tris) < tri_cap:
	tris.append(int(float(i+1)*(float(i)/2.0)))
	i+=1

count=0
for ws in wordscores:
	if ws in tris: count+=1

print count
