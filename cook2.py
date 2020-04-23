from sys import stdin, stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    n1=n
    half=int(n/2)
    l=[int(x) for x in stdin.readline().split()]
    m=max(l)
    l2=[i for i,j in enumerate(l) if j==m]
    #print(l2)
    if(len(l2)==len(l)):
        print(0)
    else:
        l3=[min(l2),max(l2)]
        count=0
        #if((l3[0]>=half) and (l3[1]>=half)):
        #    count=count+1
        while(n>0):
            n=n-1
            l3[0]=(l3[0]+1)%n1
            l3[1]=(l3[1]+1)%n1
            
            if((l3[0]>=half) and (l3[1]>=half)):
                count=count+1
        print(count)
        
            
