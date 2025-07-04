import random

computer = random.choice([1 , 2 , 3])
userStr = input("Enter your choice : ")
Dicti = {"s" : 1 , "p" : 2 , "se" : 3}
revDicti = {1 : "stone" , 2 : "paper" , 3 : "secisor"}

user = Dicti[userStr]

print(f'User choose {revDicti[user]}\nComputer choose {revDicti[computer]}')

if(computer == user):
    print("Draw")
else:
    if(computer == 1 and user == 2):
        print("You win")
    elif(computer == 1 and user == 3):
        print('You lose')
    elif(computer == 2 and user == 1):
        print('you lose')
    elif(computer == 2 and user == 3):
        print('You win')
    elif(computer == 3 and user == 1):
        print('You won')
    elif(computer == 3 and  user == 2):
        print('You lose')
    else:
        print('something with wrong')