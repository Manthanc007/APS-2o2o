n=int(input())
#l=[int(.5*i*(i+1)) for i in range(0,(10**5)+1)]
while(n>0):
    n=n-1
    x=int(input())
    r=(-1+(1+8*x)**0.5)/2
    if(r-int(r)==0.0):
        print(int(r))
    else:
        print(-1)
    
