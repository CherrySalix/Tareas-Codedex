import random

computer=random.randint(1,5) #Creates a random number between 1 and 5

print("================================\nRock Paper Scissors Lizard Spock\n================================")
print("\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")
player=int(input("Select a number: ")) #Asks the user to input a number between 1 and 5

if player == computer: #Checks if the user input is equal to the computer's random number
    print("It's a tie!")
elif (player == 1 and (computer == 3 or computer == 4)) or \
     (player == 2 and (computer == 1 or computer == 5)) or \
     (player == 3 and (computer == 2 or computer == 4)) or \
     (player == 4 and (computer == 2 or computer == 5)) or \
     (player == 5 and (computer == 1 or computer == 3)): #checks all winning conditions for the player
    print("Computer chose: ", computer)
    print("You chose: ", player)
    print("You win!")
elif player < 1 or player > 5: #Checks if the user input is out of range
    print("Invalid input! Please select a number between 1 and 5.")
else: #If none of the above conditions are met, the computer wins
    print("Computer chose: ", computer)
    print("You chose: ", player)
    print("Computer wins!")
#Fin