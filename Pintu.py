from collections import defaultdict
t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    f=list(map(int,input().split()))
    p=list(map(int,input().split()))
    l=defaultdict(list)
    k=[]
    for key,value in zip(f,p):
        l[key].append(value)
    for i in range(0,max(l)+1):
        if(len(l[i])==0):
            pass
        else:
            s=sum(l[i])
            k.append(s)
    print(min(k))
    
            
