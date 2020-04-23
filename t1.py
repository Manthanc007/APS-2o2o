n=int(input())
l=list(map(int,input().split()))
l.sort()
alice=l[:len(l)//2]
bob=l[len(l)//2:]
bob.sort(reverse=True)
if(n>2):
    alice=[i*10 for i in alice]
    final=sum(alice+bob)
    print(final,alice,bob)
else:
    print(sum(l))
