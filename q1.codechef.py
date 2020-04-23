import sys
t=int(input())
while(t>0):
    p,q,k= map(int,sys.stdin.readline().split())
    m=int((p+q)/k)
    if(m%2==0):
        print('CHEF')
    else:
        print('COOK')
    t=t-1    
       
    
