t=int(input())
while(t>0):
    t=t-1
    n,a,b=map(int,input().split())
    i=list(map(int,input().split()))
    l1=[]
    l2=[]
    l=[]
    l=[ u for u in i if(u%b==0 or u%a==0)]
    if(a==b):
        if(len(l)==0):
            print('ALICE')
        else:
            print('BOB')
    else:
        l1=[u for u in l if(u%a==0)]
        l2=[u for u in l if(u%b==0)]
        #print(l1,l2)
        for p in l2[:]:
            if p in l1:
                l2.remove(p)
        #print(l1,l2)
        if(len(l)==0):
            print('ALICE')
        elif(len(l1)<len(l2) or len(l1)==len(l2)):
            print('ALICE')
        else:
            print('BOB')














            
'''
    if(b>a and b%a==0):
        if(len(l)==0):
            print('ALICE')
        else:
            print('BOB')
    if(a>b and a%b==0):
        if(len(l)==0):
            print('ALICE')
        else:
            print('BOB')
        
       if(a%b!=0 or b%a!=0):
            if(i%a==0):
                l1.append(i)
            if(i%b==0):
                l2.append(i)
        if(leen(l1)==0 or (len(l1)==len(l2))):
            print('ALICE')
        elif(len(l1)>len(l2)):
            print('BOB')
        else:
            print('ALICE')
           '''
        
        
        
        
