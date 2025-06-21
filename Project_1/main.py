'''
1 for snake
-1 for water
0 for gun
'''
# Snake , water , Gun game

# we need to generate a random number among 0 , 1 ,-1 for computer to choose them 

import random 
computer = random.choice([-1 , 0 , 1])
youstr = input("Enter your choice: ")
youDict ={"s": 1 , "w": -1 , "g": 0}
reverseDict ={1:"Snake" , -1:"Water" , 0:"Gun"}

you=youDict[youstr]

#by now we have  2 numbers (variables) , you and computer

print(f"You chose{reverseDict[you]}\n Computer chose {reverseDict[computer]} ")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you ==1):
        print("You win !")

    elif(computer ==-1 and you ==0):
        print("You Lose")  

    elif(computer ==1 and you ==-1):
        print("You lose")  

    elif(computer ==1 and you ==0):
        print("You win !")

    elif(computer ==0 and you ==-1):
        print("You win !")

    elif(computer ==0 and you ==1):
        print("You lose")              
        
    else:
        print("Something went wrong")    