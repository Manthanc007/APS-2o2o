t=int(input())
while(t>0):
    t=t-1
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    while(k>0):
        a.sort(reverse=True)
        a[0]=1
        k=k-1
    if(sum(i*i for i in a)<=sum(i for i in a)):
        print('YES')
    else:
        print('NO')
