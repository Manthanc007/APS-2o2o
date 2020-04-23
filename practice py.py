'''t=input()
t=list(t)
n=4
while(n>0):
    n=n-1
    k=max(t,key=t.count)
    print(k)
    while k in t:
        t.remove(k)'''
'''
l=input()
l=list(l)
if((l[0]=='4' or l[0]=='5' or l[0]=='6') and len(l)==19 and l[4]=='-' and ):
    print('true')
else:
    print('False')'''
import re

PATTERN = "([4-6]{1})([0-9]{3}-?)([0-9]{4}-?){2}([0-9]{4})"


def is_valid_creditcard(sequence):
    for i, n in enumerate(sequence):
        try:
            if (sequence[i], 
                sequence[i+1], 
                sequence[i+2],
                sequence[i+3]
            ) == (n, n, n, n):
                return False
        except IndexError:
            pass
    return bool(re.match(PATTERN, sequence))
sequence=input()
is_valid_creditcard(sequence)
