t=int(input())
while(t>0):
    t=t-1
    x,y,z=map(int,input().split())
    if(x-y+z==0 or x+y-z==0 or z-x+y==0 or z-x-y==0 or x-y-z==0 or y-x-z==0):
        print('yes')
    else:
        print('no')
