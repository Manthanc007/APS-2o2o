from sys import stdin,stdout
import random
t=int(stdin.readline())
while(t>0):
    t=t-1
    n,m,k=map(int,input().split())
    p=n
    f=0
    d=0
    while(n>0):
        n=n-1
        c=[int(x) for x in stdin.readline().split()]
        if(f<min(c)):
            f=min(c)
        if(d<max(c)):
            d=max(c)
    l=[random.randint(f,d) for i in range(0,p)]
    print(*l)
        
