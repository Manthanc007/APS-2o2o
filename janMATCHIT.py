n,m=map(int,input().split())
M=2*m
l=[]
weights=[]
while(M>0):
    M=M-1
    x,y=map(int,input().split())
    l.append(x)
    l.append(y)
while(n>0):
    n=n-1
    we=list(map(int,input().split()))
    weights.append(we)
print(weights[1][0])
      

 
    
    
    
    
    
