from random import randint

t = ("Rock", "Paper", "Scissors")

d = ("Yes", "No")

computer = t[randint (0,2)]

player = False

loop = False

while player == False:
    player = input ("Rock, Paper, Scissors?")
    if player == computer:
        print ("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print ("YOU LOSE NERD! Paper covers Rock up")
        else:
            print ("You win! Rock crushes Scissors")
    elif player == "Paper":
        if computer == "Scissors":
            print ("YOU LOSE NERD! Scissors cuts right through Paper")
        else:
            print ("You win! Paper covers Rock up")
    elif player == "Scissors":
        if computer == "Rock":
            print ("YOU LOSE NERD! Rock crushes Scissors")
        else:
            print ("You win! Scissors cuts right through Paper")
    else:
        print ("I cannot understand you! Please ensure that you have proper capitalization!")
    
    loop = False

    while loop == False:
        player = input ("Continue? Yes or No?")
        if player == "Yes":
            player = False
            loop = True
        elif player == "No":
            break
        else:
            print ("I cannot understand you! Please ensure that you have proper capitalization!")
            player = False
   
            
    
