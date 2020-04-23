from sys import stdout,stdin
from collections import Counter
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    l=[int(x) for x in stdin.readline().split()]
    q=int(stdin.readline())
    while(q>0):
        q=q-1
        a,b=map(int,input().split())
        p=set(l[a-1:b])
        p1=list(set(l)^set(p))
        print(p)
        print(p1)
        print("--")
        
        
        
        
        
        
        
