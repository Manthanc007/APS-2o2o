from sys import stdin, stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    l=[int(x) for x in stdin.readline().split()]
    l.sort()
    s=0
    i=0
    while(n>0):
        n=n-1
        if((l[-1]-i)>0):
            s=s+l[-1]-i
        else:
            s=s+0
            break
        del l[-1]
        i=i+1
    s=s%(10**9+7)
    stdout.write(str(s)+'\n')
    
        
