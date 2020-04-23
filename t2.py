n=int(input())
l=list(map(int,input().split()))
count1=0
count2=0
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        count1=count1+1
        if(count1>count2):
            count2=count1
    else:
        count1=0       
print(count2+1)
