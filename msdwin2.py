from sys import stdout,stdin
from collections import Counter
import math
def nCr(n,r):
    f=math.factorial
    if(n<2):
        pass
    else:
        return(f(n)//f(r)//f(n-r))
        
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    l=[int(x) for x in stdin.readline().split()]
    q=int(stdin.readline())
    while(q>0):
        q=q-1
        a,b=map(int,input().split())
        p=l[a-1:b]
        l2=list(set(p))
        c=Counter(p)
        s=0
        for i in range(0,len(c)):
            n=int(c[l2[i]])
           # print(n)
            if(len(p)==1):
                s=1
            if(n==1 and len(p)!=1):
                s=s
            if(n!=1):
                s=s+nCr(n,2)
        print(s%998244353)
        
        
