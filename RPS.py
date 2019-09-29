from random import randint

t = ("Rock", "Paper", "Scissors")

d = ("Yes", "No")

computer = t[randint (0,2)]

verify = 1

counter = 1
while verify == 1:
    rounds = int(input("How many rounds would you like to play: 1-10?"))
    while rounds < 0 or rounds > 10:
        rounds = int(input("How many rounds would you like to play: 1-10?"))
    counter = 1
    while counter >= 1:
        print ("Round:")
        print (counter)
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
            counter = counter - 1
        
        counter = counter + 1
        
        while counter == rounds + 1:
            verify = 0
            print ("Game Over")
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
            
        

        
    
            
            
            
                
                
        
        
           
                

   
            
    
