from sys import stdin, stdout
t=int(input())
while(t>0):
    t=t-1
    n,q=map(int,input().split())
    l=[2 if((bin(int(x)).count('1'))%2==0) else 1 for x in stdin.readline().split()]
    even=l.count(2)
    odd=l.count(1)
    while(q>0):
        q=q-1
        p=bin(int(stdin.readline())).count('1')
        ev=even
        od=odd
        if(p%2==0):
            ev=ev
            od=od
        else:
            temp=od
            od=ev
            ev=temp
            
        stdout.write(str(ev)+' ')
        stdout.write(str(od)+'\n')
        
        
            
        
        
        
        
        
                 
            
        


