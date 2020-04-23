from sys import stdin, stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n=int(stdin.readline())
    if(n<=3):
        print(1)
        if(n==3):
            print(3,1,2,3)
        if(n==2):
            print(2,1,2)
        if(n==1):
            print(1,1)          
    else:
        print(n//2)
        f=1
        if(n%2!=0):
            print(3,1,2,3)
            f=4
        while(f<=n):
            print(2,f+1,f)
            f=f+2
    
