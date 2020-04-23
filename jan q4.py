t=int(input())
while(t>0):
    t=t-1
    n,m=map(int,input().split())
    matrix=[[0 for i in range(m)] for j in range(n)]
    f=0
    f1=0
    if(n>=3 and m>=3):
        k=4
        for i in range(0,n):
            f=f+1
            if(f==5):
                f=1
            for j in range(0,m):
                if(f<3):
                    matrix[i][j]=(j%4)+1
                else:
                    matrix[i][j]=((j+2)%4)+1     
    elif((n==1 and m>2) or (n==2 and m==2) or (n>2 and m==1)): 
        k=2
        for i in range(0,n):
            for j in range(0,m):
                if(f1<2):
                    matrix[i][j]=1
                    f1=f1+1
                else:
                    matrix[i][j]=2
                    f1=f1+1
                    if(f1==4):
                        f1=0
    elif((n==2 and m>2) or (m==2 and n>2)):
        k=3
        if(n==2):
            for i in range(0,n):
                for j in range(0,m):
                    matrix[i][j]=(j%3)+1
        if(m==2):
            for i in range(0,m):
                for j in range(0,n):
                    matrix[j][i]=(j%3)+1
    else:
        k=1
        for i in range(0,n):
            for j in range(0,m):
                matrix[i][j]=1
                   
                   
                   
            
                   
                   
        
    print(k)
    for v in range(n):
        temp=' '.join(str(i) for i in matrix[v])
        print(temp)
