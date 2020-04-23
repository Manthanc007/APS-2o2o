t=int(input())
while(t>0):
    t=t-1
    n,p=map(int,input().split())
    x=(n//2)+1
    m=n%x
    if(n==1 or n==2):
        total=p*p*p
    else:
        v1=p-n
        v2=p-m
        total=(v1*v1)+(v2*v2)+(v1*v2)
    print(total)
        
    
