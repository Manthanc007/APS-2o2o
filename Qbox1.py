from sys import stdin, stdout
l=list('cmanthan007')
t=int(stdin.readline())
while(t>0):
    t=t-1
    s=input()
    s=list(s.lower())
    le=len(s)
    count=0
    for i in range(0,le):
        if(s[i]==l[i]):
            count=count+1
        else:
            break
    if(count==0):
        stdout.write('cmanthan007'+'\n')
    if(count==1):
        stdout.write('manthan007'+'\n')
    if(count==2):
        stdout.write('anthan007'+'\n')
    if(count==3):
        stdout.write('nthan007'+'\n')
    if(count==4):
        stdout.write('than007'+'\n')
    if(count==5):
        stdout.write('han007'+'\n')
    if(count==6):
        stdout.write('an007'+'\n')
    if(count==7):
        stdout.write('n007'+'\n')
    if(count==8):
        stdout.write('007'+'\n')
    if(count==9):
        stdout.write('07'+'\n')
    if(count==10):
        stdout.write('7'+'\n')
    if(count==11):
        stdout.write('FOLLOWED'+'\n')
    
    
