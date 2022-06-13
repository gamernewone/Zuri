import random

gamechoice = ['Rock', 'Paper', 'Scissors']

#### Init

def init():
    player = gamechoice[playerchoice()]
    cpu = computerchoice()

    print(f"\nPlayer {player} : CPU {cpu}\n")

    compare(player,cpu)



# Player choice

def playerchoice():
    while True:
    
        choice = input("choose between Rock(r), paper(p), and scissors(s): ")
        
        if choice == "r":
            return (0)
        if choice =="p":
            return (1)
        if choice =="s":
            return (2)
        else:
            print("wrong choice, please restart")

### COmputer choice ###
def computerchoice():
    return random.choice(gamechoice)


### Comparaison ######

def compare(one, two):
    if (one == "Rock" and two =="Scissors"):
        print("Player wins")
    elif (two == "Rock" and one =="Scissors"):
        print("Cpu wins")
    elif (one == "Paper" and two =="Scissors"):
        print("Cpu wins")
    elif (two == "Paper" and one =="Scissors"):
        print("Player wins")
    elif (one == "Paper" and two =="Rock"):
        print("Player wins")
    elif (two == "Paper" and one =="Rock"):
        print("Cpu wins")
    else:
        print(" It's a draw, replay\n")
        init()
    

#### Actual game
print("welcome to the rock paper scissors game\n")
init()