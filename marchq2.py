t=int(input())
cmp='aeiou'
while(t>0):
    t=t-1
    n=int(input())
    l=[]
    l1=[]
    while(n>0):
        n=n-1
        s=input()
        s=set(s)
        s=''.join(s)
        l.append(s)
    n=len(l)
    for i in range(0,n-1):
        for j in range(i+1,n):
            p=l[i]+l[j]
            p=set(p)
            p=''.join(p)
            if(set(p)==set(cmp)):
                l1.append(p)
    print(len(l1))
    
