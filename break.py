from sys import stdin, stdout
t,s=map(int,input().split())
if(s==1):
    while(t>0):
        t=t-1
        n=int(stdin.readline())
        a=[int(x) for x in stdin.readline().split()]
        b=[int(x) for x in stdin.readline().split()]
        a.sort()
        b.sort()
        l=set()
        l.add(a[0])
        count=0
        for i in range(0,n):
            if(a[i]<b[i] and count==0 and (a[i] in l)):
                l.add(a[i])
                l.add(b[i])
                count=0
            else:
                count=1
                break
        if(count==0):
            stdout.write("YES"+'\n')
        else:
            stdout.write("NO"+'\n')                
if(s==2):
    while(t>0):
        t=t-1
        n=int(stdin.readline())
        a=[int(x) for x in stdin.readline().split()]
        b=[int(x) for x in stdin.readline().split()]
        a.sort()
        b.sort()
        l=set()
        l.add(a[0])
        count=0
        for i in range(0,n):
            if(a[i]<b[i] and count==0 and (a[i] in l)):
                l.add(a[i])
                l.add(b[i])
                count=0
            else:
             #   while(
                if(a[i]>=b[i]):
                    #Defender gives up
                    b=b+a[0:i+1]
                    a=a[i+1:]
                else:
                    #attacker gives up    
                count=1
                a=a[i:
                break 
        if(count==0):
            stdout.write("YES"+'\n')
        else:
            
        
