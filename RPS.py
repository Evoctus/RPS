from random import randint

selections = ("Rock", "Paper", "Scissors")

verify = 1

counter = 1
while verify == 1:
    playerwin = 0
    computerwin = 0
    rounds = int(input("How many rounds would you like to play: 1-10?"))
    while rounds < 0 or rounds > 10:
        rounds = int(input("How many rounds would you like to play: 1-10?"))
    counter = 1
    while counter >= 1:
        computer = selections[randint (0,2)]
        print ("Round:")
        print (counter)
        player = input ("Rock, Paper, Scissors?")
        if player == computer:
            print ("Tie")
        elif player == "Rock":
            if computer == "Paper":
                print ("YOU LOSE NERD! Paper covers Rock up")
                computerwin = computerwin + 1
            else:
                print ("You win! Rock crushes Scissors")
                playerwin = playerwin + 1
        elif player == "Paper":
            if computer == "Scissors":
                print ("YOU LOSE NERD! Scissors cuts right through Paper")
                computerwin = computerwin + 1
            else:
                print ("You win! Paper covers Rock up")
                playerwin = playerwin + 1
        elif player == "Scissors":
            if computer == "Rock":
                print ("YOU LOSE NERD! Rock crushes Scissors")
                computerwin = computerwin + 1
            else:
                print ("You win! Scissors cuts right through Paper")
                playerwin = playerwin + 1
        else:
            print ("I cannot understand you! Please ensure that you have proper capitalization!")
            counter = counter - 1
        
        counter = counter + 1
        
        print ("Player:")
        print (playerwin)
        print ("Computer:")
        print (computerwin)
        
        while counter == rounds + 1:
            verify = 0
            if playerwin < computerwin:
                print ("Game over! Computer wins!")
            elif playerwin == computerwin:
                print ("Game over! Tie!")
            else:
                print ("Game over! Player wins!")
            player = input ("Play again? Yes/No:")
            if player == "Yes":
                verify = 1
                counter = 0
                rounds = 0
            elif player == "No":
                counter = -1
            else:
                print ("I cannot understand you! Please ensure that you have proper capitalization!")
                counter = rounds + 1
                
