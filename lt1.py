t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    a=list(str(a))
    b=list(str(b))
    c=[]
    c=a+b
    c.sort(reverse=True)
    if('0' not in c):
        pr=''.join(c[0]+c[2])
        pr=int(pr)
        del c[2]
        del c[0]
        pr2=''.join(c)
        pr2=int(pr2)
        print(pr+pr2)
        
    
