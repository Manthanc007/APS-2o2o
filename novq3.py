n,q,k=map(int,input().split())
a=list(map(int,input().split()))
s=str(input())
s=list(s)
while(q>0):
    q=q-1
    if(s[0]=='!'):
        t=a[-1]
        del a[-1]
        a.insert(0,t)
        s=s[1:]   
    else:
        a.insert(0,0)
        a.append(0)
        a1=[]
        a2=[]
        #print(a)
        for i in range(len(a)):
            if(a[i]==0):
                a1.append(i)        
        #print(a1)  
        for i in range(len(a1)-1):
            r=a1[i+1]-a1[i]-1
            a2.append(r)
        #print(a2)
        if(max(a2)>=k):
            print(k)
        else:
            print(max(a2))
        del a[0]
        del a[-1]
        s=s[1:]
            

