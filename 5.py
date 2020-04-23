import datetime
from datetime import date
t=int(input())
def leapyear(year): 
    return(((year % 4 == 0) and
             (year % 100 != 0)) or
             (year % 400 == 0))          
while(t>0):
    t=t-1
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    if(m1>2 and m2<2):
        febcount=y2-y1-1
        yearlist=[i for i in range(y1+1,y2)]
    if(m1<=2 and m2>=2):
        febcount=y2-y1+1
        yearlist=[i for i in range(y1,y2+1)]
    if(m1<=2 and m2<2):
        febcount=y2-y1
        yearlist=[i for i in range(y1,y2)]
    if(m1>2 and m2>=2):
        febcount=y2-y1
        yearlist=[i for i in range(y1+1,y2+1)]
    #print(febcount,yearlist)
    d1=1
    ll=len(yearlist)
    for i in range(0,ll):
        d=datetime.date(yearlist[i],2,d1)
        m=d.strftime("%A")
        if(m=='Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'):
            yearlist[i]=0
        if(m=='Saturday'):
            yearlist[i]=yearlist[i]
        if(m=='Sunday'):
            yearlist[i]=yearlist[i]
    print(yearlist)
    
#every 823 years there is a february with 4 weekdays of each
