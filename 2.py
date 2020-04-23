t=int(input())
while(t>0):
    t=t-1
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    print(s%k)
