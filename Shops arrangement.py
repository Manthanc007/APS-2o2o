t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    l.insert(0,0)
    q=int(input())
    while(q>0):
        q=q-1
        p=[]
        p=list(map(int,input().split()))
        if(p[0]==0):
            x=p[1]
            y=p[2]
            k=p[3]
            pr=l[x:y+1]
            pr.sort()
            print(pr[k-1])
        if(p[0]==1):
            x=p[1]
            k=p[2]
            l[x]=k
            
        
