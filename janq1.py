t=int(input())
while(t>0):
    t=t-1
    s=input()
    l=[]
    l=list(s)
    i=0
    l.insert(len(l),' ')
    l.insert(0,' ')
    s=''.join(l)
    if ' not ' in s:
        print('Real Fancy')
    else:
        print('regularly fancy')
