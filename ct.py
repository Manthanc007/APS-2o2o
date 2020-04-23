'''def palindrome(seq):
    if(seq == seq[::-1]):
        print('It is a Palindrome')
    else:
        print('It is not a Palindrome')
print('Enter the String')
seq=input()
palindrome(seq)
'''
import math
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    if(a>b):
        if((math.sqrt((a*a)+(b*b)))%1==0.0 or (math.sqrt((a*a)-(b*b)))%1==0.0):
            print('yes')
        else:
            print('no')
    elif(b>a):
        if((math.sqrt((a*a)+(b*b)))%1==0.0 or (math.sqrt((b*b)-(a*a)))%1==0.0):
            print('yes')
        else:
            print('no')
    else:
        print('no')
