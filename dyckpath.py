import math
from itertools import permutations
n=int(input())
total = math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n))
l=[1,-1]
l2=[l[0] for i in range(0,n)]
l3=[l[1] for i in range(0,n)]
for i in range(len(l3)):
    l2.append(l3[i])
l1=list((permutations(l2)))
l1=set(l1)
l1=list(l1)
l4=[ list(l1[i]) for i in range(0,len(l1))]
l4=[ l1[i] for i in range(0,len(l1)) if l1[i][0]>=0]
print(l4)
