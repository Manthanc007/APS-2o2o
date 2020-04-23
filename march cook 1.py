from sys import stdin, stdout
import itertools
t=int(stdin.readline())
while(t>0):
    x=0
    y=0
    t=t-1
    n=int(stdin.readline())
    l=input()
    l=''.join(i for i, _ in itertools.groupby(l))
    i=0
    l=list(l)    
    for i in range(0,len(l)):
        if(i==0):
            if(l[i]=='L'):
                x=x-1
            if(l[i]=='R'):
                x=x+1
            if(l[i]=='U'):
                y=y+1
            if(l[i]=='D'):
                y=y-1    
        elif(l[i]=='L' and l[i-1]!=l[i] and l[i-1]!='R'):
            x=x-1
        elif(l[i]=='R'and l[i-1]!=l[i] and l[i-1]!='L'):
            x=x+1
        elif(l[i]=='U'and l[i-1]!=l[i] and l[i-1]!='D'):
            y=y+1
        elif(l[i]=='D'and l[i-1]!=l[i] and l[i-1]!='U'):
            y=y-1
        else:
            pass
    print(x,y)        
      
