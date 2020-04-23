t=int(input())
while(t>0):
    t=t-1
    n,p=map(int,input().split())
    l=list(map(int,input().split()))
    l2=[l[i] for i in range(0,len(l))]
    pr='NO'
    l2.append(p)
    for i in range(0,len(l)):
        if(p%l[i]!=0):
            pr='YES'
        else:
            l[i]=0
    if(pr=='NO' and len(l)==1):
        print(pr)
    if(pr=='NO' and len(l)>1):
        pr1='NO'
        for i in range(0,len(l2)-1):
            if(pr1=='NO'):
                if(l2[i+1]%l2[i]==0):
                    pr1='NO'
                else:
                    index=i
                    index2=i+1
                    l2[i]=int(p/l2[i])-int(l2[i+1]/l2[i])
                    l2[i+1]=1
                    del l2[-1]
                    pr1='YES'
                    for i in range(0,len(l2)):
                        if(i!=index and i!=index+1):
                            l2[i]=0
        if(pr1=='NO'):
            print(pr1)
        else:
            print(pr1,*l2)     
    if(pr!='NO'):
        res = [ind for ind, val in enumerate(l) if val != 0]
        mini=l[res[0]]
        l[res[0]]=int(p/l[res[0]])+1
        for i in range(0,len(l)):
            if(i!=res[0]):
                l[i]=0        
        print(pr,*l)
