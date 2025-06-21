 # we will get a random value of score and it will auto save also in the txt file of highscore 
# the score i txt file updated automatically as the greater the score we get 

import random   

def game():
    print("you are playing a game ")
    score = random.randint(1 ,62)

    # Fetch the highscore

    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0    

    print(f"Your score : {score}")
    
    if(score>highscore):
         with open("highscore.txt" ,"w") as f:
             f.write(str(score))

        # write this highscore to the file
         
    return score

game()