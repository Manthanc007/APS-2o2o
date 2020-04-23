t=int(input())
while t>0:
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    while q>0:
        c=0
        x1,x2,y=map(int,input().split())
        for i in range(0,n-1):
            f1=0
            f2=0
            if ((a[i]<=y and a[i+1]>=y ) or (a[i]>=y and a[i+1]<=y)):
                f1=1
        
            if(f1==1):
                if (i+1>=x1 and i+1<=x2):
                    if (i+2>=x1 and i+2<=x2):
                        f2=1
            if(f2==1):
                c=c+1
        
        print(c) 
        q-=1
    t-=1
