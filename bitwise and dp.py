cost=[3,2,7
      5,1,3
      2,7,2]
t=max(cost)+1
n=3
dp=[0,t,t
    t,t,t
    t,t,t]
x1=[]
def  countSetBits(n): 
    count = 0
    while (n):
        count +=n&1
        n >>= 1
    return count
mask=[i for i in range(0,2**n)]
for i in range(0,2**n):
    x=countSetBits(mask[i])
    x1.append(x)
for i in range(1,2**n):
    for j in range(0,3):
        if (i&(1<<j)):
            dp[
    
    
    
#To be Completed
    
    
