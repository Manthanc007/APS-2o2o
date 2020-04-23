from sys import stdout,stdin
t=int(stdin.readline())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    l=[int(x) for x in stdin.readline().split()]
    k=0
    l[0]=[1,l[0]]
    while(m>0):
        count=0
        m=m-1
        x1,x2,y=map(int,input().split())
        
        for i in range(0,len(l)-1):
            if(k!=n):
                l[i+1]=[i+2,l[i+1]]
                k=k+1
            if(((l[i][1]<=y and l[i+1][1]>=y) or (l[i][1]>=y and l[i+1][1]<=y)) and (l[i][0]<=x2 and l[i][0]>=x1 and l[i+1][0]>=x1 and l[i+1][0]<=x2)):
                count=count+1
        print(count)
        k=n
    
