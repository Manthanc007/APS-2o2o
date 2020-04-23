def prec(c):
    if(c=='^' or c=='&' or c=='|'):
        return 1
    else:
        return -1
def inToPost(s):
    stack=[]
    stack.append('N')
    l=len(s)
    news=""
    for i in range(0,l):
        if(s[i]=='#'):
            news=news+s[i]
        elif(s[i]=='('):
            stack.append('(')
        elif(s[i]==')'):
            while(stack[-1]!='N' and stack[-1]!='('):
                c=stack[-1]
                stack.pop()
                news=news+c
            if(stack[-1]=='('):
                c=stack[-1]
                stack.pop()
        else:
            while(stack[-1]!='N' and prec(s[i])<=prec(stack[-1])):
                c=stack[-1]
                stack.pop()
                news=news+c
            stack.append(s[i])
    while(stack[-1]!='N'):
        c=stack[-1]
        stack.pop()
        news=news+c
    return news
            
def aandfunc(*args):
    tem=[[0,0,0,0],[0,1,2,3],[0,2,2,0],[0,3,0,3]]
    an=[0,0,0,0]
    for i in range(0,len(tem)):
        for j in range(0,len(tem[0])):
            an[tem[i][j]]=an[tem[i][j]]+(a[i]*b[j]);
    
    return an

def xxorfunc(a[],b[]):
    tem=[[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]]
    an=[0,0,0,0]
    for i in range(0,len(tem)):
        for j in range(0,len(tem[0])):
            an[tem[i][j]]=an[tem[i][j]]+(a[i]*b[j]);
    return an

def oorfunc(a[],b[]):
    tem=[[0,1,2,3],[1,1,1,1],[2,1,2,1],[3,1,1,3]]
    an=[0,0,0,0]
    for i in range(0,len(tem)):
        for j in range(0,len(tem[0])):
            an[tem[i][j]]=an[tem[i][j]]+(a[i]*b[j]);
    return an
def evalpost(exp):
    stack=[]
    for i in range(
            
    
