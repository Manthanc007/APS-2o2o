t=int(input())
while(t>0):
    t=t-1
    m,n,k=map(int,input().split())
    matrix=[[input().split() for i in range(m)] for j in range(n)]
    print(matrix)
