t=int(input())
while(t>0):
    t=t-1
    n,k=map(int,input().split())
    n1=n
    k1=k2=k
    l=[]
    while(k1>2): 
        firstn=int(n/k1)
        k1=k1-1
        while(firstn in l):
            firstn=firstn+1
        n=n-firstn
        l.append(firstn)
    if(k1==2 and n%2==0):
        firstn=int(n/2)+1
        secondn=int(n/2)-1
        while((firstn in l) or (secondn in l)):
            firstn=firstn+1
            secondn=secondn-1
        l.append(firstn)
        l.append(secondn)
        print(l)
    if(k1==2 and n%2!=0):
        firstn=int(n/2)
        secondn=int(n/2)+1
        while((firstn in l) or (secondn in l)):
            firstn=firstn-1
            secondn=secondn+1
        l.append(firstn)
        l.append(secondn)
            
    if(k1==1):
        l.append(n)
    if(n1==(k2*(k2+1)/2)):
        print('0')
    elif(n1<(k2*(k2+1)/2)):
       print('-1')
    elif(k2>=n1):
       print('-1')
    else:
       l1=[i*i-i for i in l]
       p=1
       for i in l1:
          p*=i
       print(p%((10**9)+7))
    '''elif(1 in l):
        l.sort()
        a=l[0]
        a1=l[1]
        while(a1-a==1):
            a=l[i]
            a=l[i+1]'''
                  
       
