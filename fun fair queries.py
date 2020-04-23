n,m=map(int,input().split())
l=list(map(int,input().split()))
while(m>0):
    m=m-1
    a,b=map(int,input().split())
    print(min(l[a:b+1]))
