n=int(input())
l1=[]
l2=[i for i in range(1,n+1)]
l2=set(l2)
while(n>0):
    n=n-1
    l=[int(x) for x in input().split()]
    for i in range(0,len(l)):
        l1.append(l[i])
l1=set(l1)
final=l2.difference(l1)
final=list(final)
if(len(final)==0):
    print(-1)
else:
    for i in range(0,len(final)):
        print(final[i])
    
    
    
