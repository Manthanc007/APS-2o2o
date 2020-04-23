import sys
def maxsum(l,size):
    m1=-sys.maxsize-1
    m2=0
    c1=0
    c2=0
    for i in range(0,size):
        m2=m2+l[i]
        #c1=i
        if(m1<m2):
            c2=i
            m1=m2
        if(m2<0):
            m2=0
    c3=c2
    summ=m1        
    while(summ>0): 
        summ=summ-l[c3]
        c3=c3-1
        c1=c1+1
    del l[c2-c1+1:c2+1]
    print(m1)
t=int(input())
l=list(map(int,input().split()))
count=0
for i in range(0,len(l)):
    if(l[i]<0):
        count=count+1
if(count==0):
    print(sum(l))
    print(0)
elif(count==len(l)):
    print(max(l))
    l.sort()
    del l[-1]
    if(len(l)!=0):
        print(max(l))
    else:
        print(0)
else:
    maxsum(l,len(l))
    if(len(l)==0):
        print(0)
    else:
        maxsum(l,len(l))
