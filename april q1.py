n=int(input())
l=list(map(int,input().split()))
l=list(set(l))
l.sort(reverse=True)
if(len(l)==1):
    print(0)
else:
    print(l[1]%l[0])
