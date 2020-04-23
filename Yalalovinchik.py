from collections import deque
t=int(input())
while(t>0):
    t=t-1
    n=input()
    l=list(n)
    l=deque(l)
    e=len(l)
    l2=l.copy()
    l2=deque(l2) 
    while(e>1):
        e=e-1
        l.rotate(1)
        l2=l2+l
    l2=''.join(map(str,l2))
    r=int(l2)%(10**9+7)
    print(r,flush=True)        
