import math
from sys import stdin,stdout
t=int(stdin.readline())
while(t>0):
    t=t-1
    n,k=map(int,input().split())
    c=0
    while(n%2==0):
        c=c+1
        n=n//2
    h=math.sqrt(n)
    i=3
    while(i<=h):
        while(n%i==0):
            c=c+1
            n=n//i
        i=i+2
    if(n>2):
        c=c+1
    if(c>=k):
        stdout.write('1'+'\n')
    else:
         stdout.write('0'+'\n')
