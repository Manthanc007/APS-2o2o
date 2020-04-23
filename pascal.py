list=[1]
n=int(input())
for i in range(n):
    print(list)
    newlist=[]
    new=[]
    newlist.append(list[0])
    for i in range(len(list)-1):
        newlist.append(list[i]+list[i+1])
        if(i%2==0):
            new.append(list[i])
    newlist.append(list[-1])
    list=newlist
print(new)
