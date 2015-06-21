""" Euler 67: tree traversal with maximum sum

same solution as euler 18.

preceding shellwork:
$ cat euler67_tree.py | sed 's/^/t.append([/;s/$/])/;s/ /,/g' > euler67_tree.py
"""
from euler67_tree import t

maxpath=[]
maxpath.append([t[0][0]])
for i in range(1,len(t)):
	maxpath.append([])
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
