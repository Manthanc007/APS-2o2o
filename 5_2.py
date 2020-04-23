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
    if((l and day==6) or ( l==False and day==0) or (l==False and din==6)):
        l1[i]=l1[i-1]+1
    else:
        l1[i]=l1[i-1]
    if(l):
        din=(din+2)%7
    else:
        din=(din+1)%7
while(test>0):
    test=test-1
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    r=0
    if(y1<y2):
        if(y1%400!=0 and m1<=2 and l1[(y1%400)]-l1[(y1-1)%400]==1):
            r=r+1
        if(y2%400!=0 and m2>=2 and l1[(y2%400)]-l1[(y2-1)%400]==1):
            r=r+1
        if(int((y1+1)/400)< int((y2-1)/400)):
            x=((y1+1)%400)
            if(x!=0 and l1[x]-l1[x-1]==1):
                r=r+101-l1[x]+1
            else:
                r=r+101-l1[x]
            x=int((y2-1)/400)-int((y1+1)/400)+1
            r=r+x*101
            x=(y2-1)%400
            r=r+l1[x]
        else:
            for i in range((y1+1)%400,((y2-1)%400)+1):
                if(i==0):
                    pass
                elif:
                    (l1[i]-l[i-1]==1):
                        r=r+1
    else:
        if(y1%400>0 and m1<=2 and m2>=2 and l1[y1%400]-l1[(y1-1)%400]==1):
            r=r+1
    print(r)
                    
            
