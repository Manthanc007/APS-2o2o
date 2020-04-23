t=int(input())
while(t>0):
    t=t-1
    n,k= map(int, input().split())
    l = list(map(int, input().split()))
    l.append(-1) 
    l.sort(reverse=True)
    while(l[k-1]==l[k]):
        k=k+1
    print(len(l[0:k]))
     
