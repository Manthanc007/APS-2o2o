t=int(input())
while(t>0):
    t=t-1
    r,c,k=map(int,input().split())
    if((r==1 and c==1) or (r==1 and c==8) or (r==8 and c==1) or (r==8 and c==8)):
        total=4+9*(k-1)
    elif((r==1) or (c==8) or (r==8) or (c==1)):
        total=6+9*(k-1)
    else:
        total=9*k
    print(total)    
        
     
        
        
    
