t=int(input())
def printFibonacciNumbers(r):   
    f1 = 0
    f2 = 1
    l=[]
    if (r < 1): 
        return
    for x in range(0, r): 
        l.append(f2%10)
        next = f1 + f2 
        f1 = f2 
        f2 = next
    l.insert(0,0)
    del l[-1]
    print(l)
    l=[ l[i] for i in range(0,len(l)) if(i%2!=0)]
    print(l)
    if(len(l)%2==0):
        print(l[-1])
    else:
        middleIndex = (len(l) - 1)//2
        #print(middleIndex)  
        print(l[middleIndex])    
while(t>0):
    t=t-1
    n=int(input())
    if(n==1):
        break;
    printFibonacciNumbers(n)
    
    
    
