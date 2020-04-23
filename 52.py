def leap(year):
    if(year%100!=0 and year%4==0):
        return True
    elif(year%100==0 and year%400==0):
        return True
    else:
        return False
test=int(input())
l1=[0 for i in range(400)]
din=4
for i in range(1,400):
    l=leap(i)
    if((l and din==6) or ( l==False and din==0) or (l==False and din==6)):
        l1[i]=l1[i-1]+1
    else:
        l1[i]=l1[i-1]
    if(l):
        din=(din+2)%7
    else:
        din=(din+1)%7
while(test>0):
    test=test-1
    me1,ye1=map(int,input().split())
    me2,ye2=map(int,input().split())
    r=0
    if(ye1<ye2):
        if(ye1%400!=0 and me1<=2 and l1[(ye1%400)]-l1[(ye1-1)%400]==1):
            r+=1
        if(ye2%400!=0 and me2>=2 and l1[(ye2%400)]-l1[(ye2-1)%400]==1):
            r+=1
        if((ye1+1)//400<(ye2-1)//400):
            x=((ye1+1)%400)
            if(x!=0 and l1[x]-l1[x-1]==1):
                r+=101-l1[x]+1
            else:
                r+=101-l1[x]
            x=((ye2-1)//400)-(((ye1+1)//400)+1)
            r+=(x*101)
            x=(ye2-1)%400
            r+=l1[x]
        else:
            for i in range((ye1+1)%400,((ye2-1)%400)+1):
                if(i==0):
                    pass
                elif(l1[i]-l1[i-1]==1):
                        r+=1
    else:
        if(ye1%400>0 and me1<=2 and me2>=2 and l1[ye1%400]-l1[(ye1-1)%400]==1):
            r+=1
    print(r)
                    
            
