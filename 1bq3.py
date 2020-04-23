t=int(input())
while(t>0):
    t=t-1
    n,k=map(int,input().split())
    n1=n
    k1=k
    l=[]
    while(k1>1):
        if(n%k!=0):
            firstn=int(n/k)+1 
        elif(k==2):
            firstn=int(n/2)+1
        else:
            firstn=int(n/k)
        l.append(firstn)
        n=n-firstn
        k1=k1-1
    l.append(n)
    if(n1==(k*(k+1)/2)):
        print('0')
    elif(n1<(k*(k+1)/2)):
       print('-1')
    elif(k>=n1):
       print('-1')
    else:
       l1=[i*i-i for i in l]
       p=1
       for i in l1:
          p*=i
       print(p%((10**9)+7))
                  
       
