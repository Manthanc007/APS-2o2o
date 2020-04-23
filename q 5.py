from sys import stdin, stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    l=[int(x) for x in stdin.readline().split()]
    l1=[]
    k=len(l)
    total=(k*(k+1))//2
    for i in range(0,k):
        if(l[i]%2==0 and l[i]%4!=0):
            l1.append(1)
        elif(l[i]%2!=0):
            l1.append(0)
        else:
            l1.append(3)
    c=0 
    left=[]
    right=[]
    l2=[i for i in range(0,len(l1)) if(l1[i]==1)]
    for i in range(0,len(l2)):
        p=l2[i]
        if(p!=0):
            while(l1[p-1]==0 and p>0):
                c=c+1
                p=p-1
        left.append(c)
        c=0
    l1.append(1)
    for i in range(0,len(l2)):
        p=l2[i]
        if(p!=len(l1)-1):
            while(l1[p+1]==0 and p<=len(l1)):
                #print(p+1,len(l1)-1)
                c=c+1
                p=p+1
        right.append(c)
        c=0
    #print(l1)
    #print(l2)
    #print(left)
    #print(right)
    bad=0
    for i in range(0,len(left)):
        bad=bad+left[i]+right[i]+left[i]*right[i]
    print(total-bad-len(l2))

