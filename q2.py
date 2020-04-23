from sys import stdin, stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    l=[int(x) for x in stdin.readline().split()]
    k=6
    if(len(l)<=k):
        h=1
    else:
        h=len(l)-k
    for i in range(0,h+1):
        if(sum(l[i:i+k])>1):
            p="NO"
            break
        else:
            p="YES"
    print(p)
