l=list(map(int,input().split()))
n=int(input())
l1=[]
while(n>0):
    n=n-1
    s=input()
    l1.append(s)
l=''.join(str(i) for i in l)
print(l)
