import random

gamechoice = ['Rock', 'Paper', 'Scissors']

#### Init ####

def init():
    player = gamechoice[playerchoice()]
    cpu = computerchoice()

    print(f"\nPlayer {player} : CPU {cpu}\n")

    compare(player,cpu)



#### Player choice

def playerchoice():
    while True:
    
        choice = (input("choose between Rock(r), paper(p), and scissors(s): ")).lower()
        
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


### Actual game ###

def compare(one, two):
    winner = (('Rock','Scissors'), ('Paper','Rock'), ('Scissors','Paper'))

    if (one,two) in winner:
        print("player wins")
    elif(two,one) in winner:
        print("Computer wins")
    else:
        print(" It's a draw, replay\n")
        init()
    

#### Actual game
print("welcome to the rock paper scissors game\n")
init()