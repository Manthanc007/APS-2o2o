N,c=map(int,input().split())
y=N//2
l=1
r=N
while(r-l!=1):
    print(1,y,flush=True)
    i=int(input())
    if(i==0):
        l=y
        y=(y+r)//2
    if(i==1):
        r=y
        if(y==2):
            y=0
        else:
            y=(l+y)//2
        print(2)
x=y+1
print(3,x,flush=True)
