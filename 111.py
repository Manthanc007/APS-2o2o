T=int(input())
for _ in range(T):
    (N,M)=list(map(int,input().split()))
    l=[]
    flag=0
    for i in range(N):
        l.append(input())
    print(l)
    if N>2:
        if '.' not in l[0]:
            print("YES")
        else:
            if l[0].endswith("#."):
                print("NO")
            elif l[0].startswith(".#"):
                print("NO")
            elif '#.#' in l[0]:
                print("NO")
            else:
                print("YES")
    else:
        if '.' not in l[0]:
            print("NO")
        elif '#' in l[0]:
            print("NO")
        elif '#' not in l[0]:
            print("YES")
            
