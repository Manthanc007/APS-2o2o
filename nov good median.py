from statistics import median
from itertools import chain, combinations
def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(2, len(ss)+1 ,2)))
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    if(len(set(l))==1):
        print(int((2**len(l))-1)%(10**9+7))
    elif(len(set(l))==len(l)):
         print(int((2**len(l))/2)%(10**9+7))
    else:
         for subset in all_subsets(l):
             if(median(subset) in subset): 
                 count=count+1
         print(int((2**len(l))/2)+(count)%(10**9+7)) 
