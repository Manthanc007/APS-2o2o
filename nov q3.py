l=list(map(int,input().split()))
output=[]
l1=[ 2**i for i in range(2,26)]
a=1
l2=[]
for i in range(len(l1)):
    a=l1[i]-a
    l2.append(a)
l2.insert(0,1)
l2.insert(0,1)
l1.insert(0,2)    
l1.insert(0,0)
l2.insert(0,0)

for i in range(1,len(l)):
    a1=l[i]
    output.append(l2[a1])
    output.append(l1[a1])
for i in range(len(output)):
    print(output[i],end=" ")
