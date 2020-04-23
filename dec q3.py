import math 
N,c=map(int,input().split())
size=int(math.sqrt(N))
y=size
l=1
r=N
while(r-l!=1):
    print(1,y,flush=True)
    i=int(input())   
    if(i==0):
        if(y+size<r):
            l=y
            y=y+size
        else:
            y=y+1
            r=y
    if(i==1):
        if(y+size>N and y<=N%size):
            l=y
            y=y+1
            r=y
            print(r,l,y)
            break
        if(y<=size):
            r=size
            y=(l+r)//2
            r=y
            if(y==2):
                y=1
                break
            print(y)
        else:
            y=(l+r)//2
            r=y
            print(y)
           
           
            
            
x=y        
print(3,x,flush=True)

