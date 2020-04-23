t=int(input())
while(t>0):
    l=[]
    l1=[]
    j=[]
    j1=[]
    t=t-1
    d=int(input())
    while(d>0):
        d=d-1
        day,p=map(int,input().split())
        l.append(day)
        j.append(p)
    q=int(input())
    while(q>0):
        l2=l.copy()
        j2=j.copy()
        q=q-1
        dead,req=map(int,input().split())
        i=-1
        if(dead<l2[0]):
            print('Go Sleep')
        elif(dead>=l2[-1] and sum(j2)>=req):
            print('Go Camp')
        elif(dead>=l2[-1] and sum(j2)<req):
            print('Go Sleep')    
        else:
            while(dead>=l2[i+1] and i<len(j2)-2):
                i=i+1
            if(i==0 and req<=j2[0]):
                i=1
            dead=l2[i]
            #print(dead,sum(j[0:i+1]),req)
            #print(j2)
            if(sum(j2[0:i+1])>=req):
                print('Go Camp')
            else:
                print('Go Sleep')
            
    
        
