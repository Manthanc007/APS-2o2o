t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort()
    u=0
    for i in range(0,n):
        u=u+min(l1[i],l2[i])
    print(u)
        
        
        
