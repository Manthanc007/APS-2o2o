import random

print (' Hello What is your name')
name =input()

print ('Let start the secret no. guessing game'+ str(name))
secretnumber=random.randint(1,100)

for guessestaken in range(1,10):

 guess=input()

if secretnumber < guess:
 print('Todha kam guess kijiye')
elif secretnumber > guess:
 print('Todha zyada guess kijiye')
else:
     if guess == secretnumber:
 print('Good job' + name + guessestaken)
else :
 print('Ans is' + secretnumber)

