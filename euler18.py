""" Euler 18: tree traversal with maximum sum
What path down the tree yields the maximum total?
 0: 75
 1: 95 64
 2: 17 47 82
 3: 18 35 87 10
 4: 20 04 82 47 65
 5: 19 01 23 75 03 34
 6: 88 02 77 73 07 63 67
 7: 99 65 04 28 06 16 70 92
 8: 41 41 26 56 83 40 80 70 33
 9: 41 48 72 33 47 32 37 16 94 29
10: 53 71 44 65 25 43 91 52 97 51 14
11: 70 11 33 28 77 73 17 78 39 68 17 57
12: 91 71 52 38 17 14 91 43 58 50 27 29 48
13: 63 66 04 68 89 53 67 30 73 16 69 87 40 31
14: 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
t=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
t[0]=[75]
t[1]=[95,64]
t[2]=[17,47,82]
t[3]=[8,35,87,10]
t[4]=[20,4,82,47,65]
t[5]=[19,1,23,75,3,34]
t[6]=[88,2,77,73,7,63,67]
t[7]=[99,65,4,28,6,16,70,92]
t[8]=[41,41,26,56,83,40,80,70,33]
t[9]=[41,48,72,33,47,32,37,16,94,29]
t[10]=[53,71,44,65,25,43,91,52,97,51,14]
t[11]=[70,11,33,28,77,73,17,78,39,68,17,57]
t[12]=[91,71,52,38,17,14,91,43,58,50,27,29,48]
t[13]=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
t[14]=[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

"""
from any point t[i][j] (the jth element at depth i) a traversal can go 
to t[i+1][j] or t[i+1][j+1]. 
starting at level 2, it is only necessary to remember the highest-valued 
path to get to each point at that depth.
at the next depth, alg should evaluate all paths to get from the last depth 
to itself, and only remember the maximal path.
nodewise: each node should examine the two paths that could have been taken 
to it and store the larger.
"""

maxpath=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

maxpath[0].append(t[0][0])
for i in range(1,len(t)):
	for j in range(0,len(t[i])):
		if j==0:
			left=0
		else:
			left=maxpath[i-1][j-1]+t[i][j]
		if j==len(t[i])-1:
			right=0
		else:
			right=maxpath[i-1][j]+t[i][j]
		maxpath[i].append(max(left,right))
print max(maxpath[len(maxpath)-1])
