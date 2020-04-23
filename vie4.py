t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    nod=[]
    pr=[]
    po=[]
    a=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41]
    while(n>0):
        n=n-1
        node,pre,post=map(int,(input().split()))
        nod.append(node)
        pr.append(pre)
        po.append(post)
        for i in range(0,len(nod)):
            if(pr[len(nod)-i-1]+a[i]==po[len(nod)-i-1]):
                p=1
            else:
                p=0
    print(p)
        
