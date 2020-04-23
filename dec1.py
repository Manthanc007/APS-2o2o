N,c=map(int,input().split())
coins=1000
l=[]
while(coins>0):
    l.append(N/2)
    N=int(N/2)
    N=int((N/2+N)/2)
    
    
    
   
    print('1 '+ str(y[0]),flush=True)
   
    coins=coins-1
    i=int(input())
    if(i==1):
        l.append(N)
        print('2',flush=True)
        coins=coins-c
    if(i==0):
        break
print('3 ' + str(min(l)),flush=True)
        
        
      
            


