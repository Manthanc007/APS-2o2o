from bisect import bisect
t=int(input())
while(t>0):
    t=t-1
    n,d=map(int,input().split())
    l=[]
    l=[int(i) for i in str(n)]
    l.sort()
    len1=len(l)
    index=bisect(l,d)
    if(index==len(l)):
        l=[str(i) for i in l]
        print(''.join(l))    
    else:
        l=l[0:index]
        len2=len(l)
        o=len1-len2
        while(o>0):
            l.append(d)
            o=o-1
        l=[str(i) for i in l]
        print(''.join(l))
    
    
