import random, msvcrt
from colorama import init, Fore, Back
init(autoreset=True)

def Greeting():
    print(Fore.MAGENTA + "Welcom To The Dice Rolling Games!")
    return input("Enter User Name : ").capitalize()

def GameStart():
    print(Fore.LIGHTYELLOW_EX + "Which Game you want to play Double Or Score??")
    game_mode = input("Enter Game Mode : ").capitalize()
    # game_mode = "Score"
    MainGame(game_mode) 
    
def MainGame(game_mode):
    print(Fore.LIGHTCYAN_EX + "Press any key to roll the dice again, Q for exit")
    if game_mode not in ["Double","Score"]:
        print("Please check your input")
        GameStart()
    else:
        if game_mode == 'Double':
            CheckDouble(chance,score)
            PlayAgain()
        else:
            CheckScore(chance,score)
            PlayAgain()
        
        
def CheckDouble(chance,score):
    print(Fore.GREEN + "Game Double Start....")
    while chance > 0:
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        print(dice_1,dice_2 ,end="\n")
        if dice_1 == dice_2:
            if dice_1 == 6 and dice_2 == 6:
                print(Fore.GREEN + f'You Make it Double!!! {"\n"}Your Score : {score}')
                break
            else:
                score = score + 1
        key = msvcrt.getch()     
        if key in [b'q', b'Q']:
            print(Fore.LIGHTRED_EX + f"You Quit the game {"\n"}Your Score : {score}")
            break
        else:
            chance -= 1
    else:
        print(Fore.RED + f"You couldn't make Double{"\n"}Your Score : {score}{"\n"}Try Again !!")
        
def CheckScore(chance,score):
    print(Fore.GREEN + "Game Score Start....")
    while chance > 0:
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        print(dice_1,dice_2 ,end="\n")
        if dice_1 == dice_2:
            score += dice_1
            if dice_1 == 6 and dice_2 == 6:
                score += dice_1*2
        else:
            score += dice_1+dice_2
        key = msvcrt.getch()     
        if key in [b'q', b'Q']:
            print(Fore.LIGHTRED_EX + f"You Quit the game {"\n"}Your Score : {score}")
            break
        else:
            chance -= 1
    else:
        print(f'Your Score : {score}')
        FeedBack(score)

def FeedBack(score):
    percentage = score / 5 * 100
    if percentage >= 80:
        print(Fore.LIGHTMAGENTA_EX + f"Excellent! {name}")
    elif percentage >= 50:
        print(Fore.LIGHTRED_EX + f"Good Job! {name}")
    elif percentage >= 30:
        print(Fore.LIGHTBLUE_EX + f"Well Played! {name}")
    else:
        print(Fore.CYAN + f"Try Again! {name}")

def PlayAgain():
    ask_play = input("Do you want to play More?? : ").capitalize()
    if ask_play == 'Yes':
        GameStart()
    else:
        print(Fore.CYAN + f"Thanks For Coming, {name}")
        exit()
       
#Main Funtion
chance = 5
score = 0
name = Greeting()
GameStart()

