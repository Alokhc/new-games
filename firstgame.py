import random
x =  input("whats your name")

print("hii " + x)

score=0
print("""-------want to play a game 
rules are simple :
	1. choose a random number between 1 and 5.
	2. then enter if no match with ia you wins only one chance """)
	
y= random.randrange(1, 5)

n= input("enter you number   : ")
print("AI choose : " )
print(y)


if y == n : 
 print('coorect')

 

else:
	print("you loose ")
	
	
	

