import math
def buildsparsetable(arr,n):
    for i in range(0,n):
        lookup[i][0]=arr[i]
    j=1

    while((1<<j)<=n):
        i=0
        while((i+(1<<j)-1)<n):
            if(lookup[i][j-1]<lookup[i+(1<<(j-1))][j-1]):
                lookup[i][j]=lookup[i][j-1]
            else:
                lookup[i][j]=lookup[i+((1<<j-1))][j-1]
            i+=1
        j+=1
def query(arr,l,r):
    j=int(math.log(r-l+1,2.0))
    if(arr[lookup[l][j]]<=a[lookup[R-(1<<j)+1][j]]):
        return a[lookup[l][j]]
    else:
        return a[lookup[r-(1<<j)
arr=[3,4,6,2,5,6,4]
n=len(arr)
maX=n+1
lookup=[[0 for i in range(maX)] for j in range(maX)]
buildsparsetable(arr,n)
