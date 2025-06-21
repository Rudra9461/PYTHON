import random
n = random.randint(1,100)
a=-1
guesses = 1

while(a!=n):
    #this is always true as is not in range 
    a = int(input("Guess a number :"))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")    
        guesses +=1

print(f"You have guessed the number correctly number {n} in {guesses} attempts")    