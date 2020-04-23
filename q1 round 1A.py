t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    sum=0
    while(n>0):
        n=n-1
        word=input()
        l=list(word)
        if(l[0]=='d'):
            sum=sum+.2
            if(l[1]=!'d' or 'f'):
                sum=sum+.2
            elif(l[1]=='d'):
                sum=sum+.1
            elif(l[1]=='f'):
                sum=sum+.4
            else:
                sum=sum
        if(l[0]=='f'):
            sum=sum+.2
            if(l[1]=!'d' or 'f'):
                sum=sum+.2
            elif(l[1]=='d'):
                sum=sum+.4
            elif(l[1]=='f'):
                sum=sum+.1
            else:
                sum=sum
                
           
        
             
