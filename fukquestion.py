t=int(input())
while(t>0):
    flag=0
    t=t-1
    a=int(input())
    l=list(map(int,input().split()))
    f=[0]
    l1=[]
    l2=[]
    if((len(set(l))==1) or len(l)==len(set(l))):
        print('Poor Chef')
    else:
        l.insert(0,0)
        for i in range(1,len(l)):
            f.append(l[l[i]])
        for i in range(1,len(l)):
            (flag1,flag2)=(0,0)
            if(l[i] in l1):
                flag1=1
            else:
                l1.append(l[i])
            if(f[i] in l2):
                flag2=1
            else:
                l2.append(f[i])
            if (flag2==1 and flag1==0):
                flag=1
                break
            
        if(flag==0):
            print('Poor Chef')
        else:
            print('Truly Happy') 
