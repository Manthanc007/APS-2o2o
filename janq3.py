n,m=map(int,input().split())
l1=list(map(int,input().split()))
minindex=l1.index(min(l1))
l2=list(map(int,input().split()))
maxindex=l2.index(max(l2))
for i in range(0,m):
    print(minindex,i)
for j in range(0,minindex):
    print(j,maxindex)
for j in range(minindex+1,n):
    print(j,maxindex)
