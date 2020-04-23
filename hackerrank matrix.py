n=int(input())
t=n
mat=[]
sums=[]
while(n>0):
    n=n-1
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(0,t):
    a=mat[i][i]
    b=mat[i][n-1-i]
    c=abs(a-b)
    sums.append(c)
print(sum(sums))
    
