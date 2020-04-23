n,m=map(int,input().split())
l=list(map(int,input().split()))
t=0
result=[0 for i in range(0,n)]
result.insert(0,1)
while(t<m):
    #print(t)
    for i in range(l[t],n+1):
        result[i]=result[i]+result[i-l[t]]        
    t=t+1
print(result[-1])
    
   0 1 2 3 4
1  [1,1,1,1,1]  
2  [1 1 2 2 3]
3  [1 1 2 3 4]
