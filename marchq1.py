t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    l1=[ l[i] for i in range(0,len(l)) if(l[i]<0) ]
    l2=[ l[i] for i in range(0,len(l)) if(l[i]>0) ]
    if(len(l2)==0 or len(l1)==0):
        print(len(l),len(l))
    else:
        print(max(len(l1),len(l2)),min(len(l1),len(l2)))
