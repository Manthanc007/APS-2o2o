def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
re=primes(620000)
l3=re[0:3340]
l2=[]
kernel=re[1:168]
re=re[3340:]
while(len(re)!=0):
    ref=re[0:168]
    re=re[168:]
    for i,v in enumerate(kernel):
         ref.insert(2*i+1,v)
    del ref[-1]
    l2.append(ref)    
del l2[-1]
for i in l2:
    l2=l2+l2[0]
    del l2[0]
l2=l3+l2
t=int(input())
while(t>0):
    t=t-1
    c=int(input())
    l=l2[0:c+1]
    l1=[]
    i=0
    r=l[0]*l[-2]
    while(len(l)!=1):
        p=l[i]*l[i+1]
        del l[0]
        l1.append(p)
    del l1[-1]
    l1.append(r)
    print(*l1,sep=' ')
