import sys
from sys import stdin, stdout
def maxSum(arr, n, k):
    res = 0
    for i in range(k):
        res += arr[i] 
    curr_sum = res 
    for i in range(k,n):
        curr_sum += arr[i] - arr[i-k] 
        res = max(res, curr_sum)
    return res
def minSum(arr,n,k):
    win_sum=0
    min_window = sys.maxsize
    for i in range(0,n):
        win_sum+=arr[i]
        if(i+1>=k):
            if(min_window>win_sum):
                min_window=win_sum
                last=i
            win_sum=win_sum-arr[i+1-k]
    return(sum(arr[last-k+1:last+1]))        
                
t=int(stdin.readline())
while(t>0):
    t=t-1
    n,q=map(int,input().split())
    l=[int(x) for x in stdin.readline().split()]
    le=len(l)
    while(q>0):
        q=q-1
        k=int(stdin.readline())
        MIN=minSum(l,le,k) 
        MAX=maxSum(l,le,k) 
        print(MAX,MIN)
