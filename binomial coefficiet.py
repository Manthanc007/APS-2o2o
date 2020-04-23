def func1(n,k):
    c=[[0 for i in range(0,k)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,min(i,k)):
            if(i==0 or i==j):
                c[i][j]==1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
        print(c)

def func2(n,k):
    if(n==k or k==0):
        return 1
    else:
        print(func2(n-1,k-1)+func2(n-1,k))

def func3(n,k):
    c=[0 for i in range(0,n+1)]
    c[0]=1
    for i in range(1,n):
        for j in range(min(i,k),1):
            c[j]=c[j]+c[j-1]
        return c[k]
    
#func1(4,2)
func2(4,2)
#func3(4,2)
