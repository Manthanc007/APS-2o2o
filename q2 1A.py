t=int(input())
while(t>0):
    flag=0
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    d=l.index(max(l))
    l1=l[0:d+1]
    del l[0:d+1]
    for i in range(0,len(l1)):
        l.append(l[i])
    for i in range(0,len(l)-1):
        if(l[i]<=l[i+1]):
            print("YES")
        else:
            print("NO")
      
        
        
    
        
        
        
     
