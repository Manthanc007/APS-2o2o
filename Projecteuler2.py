t=int(input())
n=t
mat=[]
new=[]
while(t>0):
    t=t-1
    l=list(map(int,input().split()))
    mat.append(l)
    
#print(mat)
sum=0
new=[[0 for x in range(0,n)] for x in range(0,n)]
new[0][0]=mat[0][0]
for i in range(1,n):
    new[i][0]=new[i-1][0]+mat[i][0]
for j in range(1,n):
    new[0][j]=new[0][j-1]+mat[0][j]
for i in range(1,n):
    for j in range(1,n):
        new[i][j]=mat[i][j]+min(new[i-1][j],new[i][j-1])
        
print(new[-1][-1])        
    
    
    
           
