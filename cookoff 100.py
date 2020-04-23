x=int(input())
while(x>0):
    x=x-1
    t=input()
    t=list(t)
    t=[1 if i!='G' else 0 for i in t]
    t1=[]
    t2=[]
    for i in range(len(t)-1):
        if(t[i]==t[i+1]==0):
            t1.append(i)
        elif(t[i]==t[i+1]==1):
            t2.append(i)
    #print(t1)
    #print(t2)
    if(len(t)>1 and len(set(t))==1):
        print('no')
    elif(len(t1) >1 or len(t2)>1):
        print('no')
    elif(len(t)==1):
        print('yes')
    elif(len(t1)==0 and len(t2)==0):
        print('yes')
    elif(len(t1)==1 and len(t2)==0):
        print('yes')
    elif(len(t1)==0 and len(t2)==0):
        print('yes')
    else:
        if(len(t1)==0):
            t3=t2
            t[t3[0]+1],t[t3[0]+2]=t[t3[0]+2],t[t3[0]+1]
        elif(len(t2)==0):
            t3=t1
            t[t3[0]+1],t[t3[0]+2]=t[t3[0]+2],t[t3[0]+1]
        else:
            if(t1[0]>t2[0]):
                o=t[t2[0]:t1[0]]
            else:
                o=t[t1[0]:t2[0]]
            o.reverse()
            t[t2[0]:t1[0]]=o[0:]
        #print(t3)
        t1=[]
        t2=[]
        for i in range(len(t)-1):
            if(t[i]==t[i+1]==0):
                t1.append(i)
            elif(t[i]==t[i+1]==1):
                t2.append(i)
        #print(t1)
        #print(t2)  
        if(len(t)>1 and len(set(t))==1):
            print('no')
        elif(len(t1)>=1 or len(t2)>=1):
            print('no')
        else:
            print('yes')
        
