import random 
from colorama import init, Fore, Back
init(autoreset=True)

def Quiz(questions):
    copy_questions = questions[:]
    random.shuffle(copy_questions)
    score = 0
    for question_dict in copy_questions:
        for key, value in question_dict.items():
            print(key)
            for z in value['Options']:
                print(z)
            answer = input("Enter your answer : ").upper() 
            if answer == value["Answer"]:
                score += 1
                print(Fore.GREEN + "Correct")
            else:
                print(Fore.RED + "Incorrect") 
                print(Fore.YELLOW + f"Answer : {value["Answer"]}")
    return score

def Greeting():
    print(Fore.MAGENTA + "Welcom To The Quiz!")
    return input("Enter User Name : ").capitalize()
    
def FeedBack(score):
    percentage = score / len(questions) * 100
    if percentage >= 80:
        print(Fore.LIGHTMAGENTA_EX + "Excellent!")
    elif percentage >= 50:
        print(Fore.LIGHTRED_EX + "Good Job!")
    elif percentage >= 30:
        print(Fore.LIGHTBLUE_EX + "Well Played!")
    else:
        print(Fore.CYAN + "Try Again!")
    
  
questions = [{"what is 2 + 2 ?": {"Options" : ["A. 4", "B. 8", "C. 9", "D. 10"], "Answer" : "A"}},
            {"what is 2^3 ?": {"Options" : ["A. 4", "B. 8", "C. 9", "D. 10"], "Answer" : "B"}},
            {"what is 2 * 25 ?": {"Options" : ["A. 40", "B. 45", "C. 50", "D. 22"], "Answer" : "C"}}
        ]


name = Greeting()

score = Quiz(questions)
print(Fore.LIGHTWHITE_EX + f"{name}, your score : {score}")

FeedBack(score)




