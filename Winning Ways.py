from sys import stdin, stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    l=[int(x) for x in stdin.readline().split()]
    q=int(stdin.readline())
    while(q>0):
        q=q-1
        a,b=map(int,input().split())
        p=l[a-1:b]
        for i in range(0,len(p)):
            
            
        
