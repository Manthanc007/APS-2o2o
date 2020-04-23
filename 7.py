import math
t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    count=0
    flag=0
    x.sort()
    y.sort()
    for i in range(0,n-1):
        if(x[i]==0):
            count+=(n-1)*m
            flag=1
        else:
            for j in range(i+1,n):
                dist=x[j]-x[i]
                a=math.sqrt(((math.pow(dist,2))-(math.pow(x[i],2))+(math.pow(x[j],2)))/2)
                #print(a)
                if(a-int(a)==0):
                    for k in range(0,m):
                        if(abs(y[k])==a):
                            count=count+1
            for i in range(0,m-1):
                if(flag!=1 and y[i]==0):
                    count+=n*(m-1)
                else:
                    for j in range(i+1,m):
                        dist=y[j]-y[i]
                        a=math.sqrt(((math.pow(dist,2))-(math.pow(y[i],2))+(math.pow(y[j],2)))/2)
                        if(a-int(a)==0):
                            for k in range(0,n):
                                if(abs(x[k])==a):
                                    count=count+1
    print(count)
                    
                
