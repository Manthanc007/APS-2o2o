t=int(input())
sums=0
while(t>0):
    maxx=-400
    s1=[0,0,0,0]
    t=t-1
    n=int(input())    
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
    c9=0
    c10=0
    c11=0
    c12=0
    c13=0
    c14=0
    c15=0
    c16=0
    while(n>0):
        n=n-1
        x,y=input().split()
        if(x=='A' and y=='3'):
            c1=c1+1
        if(x=='A' and y=='6'):
            c2=c2+1
        if(x=='A' and y=='9'):
            c3=c3+1
        if(x=='A' and y=='12'):
            c4=c4+1
        if(x=='B' and y=='3'):
            c5=c5+1
        if(x=='B' and y=='6'):
            c6=c6+1
        if(x=='B' and y=='9'):
            c7=c7+1
        if(x=='B' and y=='12'):
            c8=c8+1
        if(x=='C' and y=='3'):
            c9=c9+1
        if(x=='C' and y=='6'):
            c10=c10+1
        if(x=='C' and y=='9'):
            c11=c11+1
        if(x=='C' and y=='12'):
            c12=c12+1
        if(x=='D' and y=='3'):
            c13=c13+1
        if(x=='D' and y=='6'):
            c14=c14+1
        if(x=='D' and y=='9'):
            c15=c15+1
        if(x=='D' and y=='12'):
            c16=c16+1
    matrix=[[c1,c2,c3,c4],
        [c5,c6,c7,c8],
        [c9,c10,c11,c12],
        [c13,c14,c15,c16]]
    for i in range(0,4):
        for j in range(0,4):
            if(i!=j):
                for k in range(0,4):
                    if(k!=i and k!=j):
                        for h in range(0,4):
                            if(h!=i and h!=j and h!=k):
                                #print(i,j,k,h)
                                s1[0]=matrix[0][i]
                                s1[1]=matrix[1][j]
                                s1[2]=matrix[2][k]
                                s1[3]=matrix[3][h]
                                s1.sort(reverse=True)
                                s1[0]=s1[0]*100
                                s1[1]=s1[1]*75
                                s1[2]=s1[2]*50
                                s1[3]=s1[3]*25
                                s1=[-100 if x==0 else x for x in s1]
                                if(sum(s1)>maxx):
                                    maxx=sum(s1)
    print(maxx)
    sums=sums+maxx
print(sums)
