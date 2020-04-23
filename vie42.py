n,e=map(int,input().split())
l=[]
vv=e+1
while(e>0):
    e=e-1
    v1,v2=map(int,input().split())
    l.append(v1)
    l.append(v2)
l=set(l)
l=list(l)
s=int(input())
v=int(input())
s=s-1
l=l[s:]+l[0:s]
print(*l[v-1:])

