def pr(list):
    for i in range(0,len(l)-1,2):
        print(l[i],l[i+1])
t=int(input())
while(t>0):
    t=t-1
    x,y=map(int,input().split())
    l=[1,7,2,8,8,2,7,1,4,4,1,1,2,2,1,3,3,1,4,2,5,1,1,5,4,8,8,4,6,6,8,8,7,7,6,8,8,6]
    lodu=19
    if(x==4 and y==4):
        print(lodu)
        pr(l)
    elif(x==y and x!=4):
        print(lodu+1)
        print(4,4)
        pr(l)
    elif(x+y==8 and x!=4):
        print(lodu+1)
        print(4,4)
        pr(l)
    else:
        print(lodu+2)
        print(int((x+y)/2),int((x+y)/2))
        print(4,4)
        pr(l)
        
