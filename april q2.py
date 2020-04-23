t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s,x=map(str,input().split())
    totalc=(n*(n+1))/2
    l=[] 
    l=[pos for pos, char in enumerate(s) if char == x]
    if(len(l)==0):
        print(0)
    else:
        first=l[0]
        last=l[-1]
        ex=n-last-1
        #print(l)
        l=[l[i+1]-l[i]-1 for i in range(0,len(l)-1)]
        l.insert(0,first)
        #print(l)
        l=[(l[n]*(l[n]+1))/2 for n in range(0,len(l))] 
        #print(l)
        print(int(totalc-(ex*(ex+1)/2)-int(sum(l))))

