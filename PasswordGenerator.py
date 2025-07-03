from colorama import init, Fore, Back,Style
init(autoreset=True)
import string, random

def IsStrong(password):
    #any(char.isupper() for char in password) and any(char.islower() for char in password) 
    if any(char.isascii() for char in password) and any(char.isdigit() for char in password) and any(char in punctuation for char in password):
        return True
        
# password generator by length
def PasswordGenrator(password_length):
    password = ''
    while password_length > 0:
            random_password = random.choice(password_generat + punctuation)
            password += random_password
            password_length -= 1
    return password

#Check the Strngth of password Week, Medium and Strong
def CheckStrength(password):
    if  len(password) < 6:
        print(Fore.RED + "Password it too poor, Try Again!")
        return False 
    elif len(password) < 9:
        print(Back.WHITE + Fore.BLUE + password)
        print(Fore.RED + "Week")
    else:
        if IsStrong(password):
            print(Back.WHITE + Fore.BLUE + password)
            print(Fore.GREEN + "Strong")
        else:
            print(Back.WHITE + Fore.BLUE + password)
            print(Fore.YELLOW + "Medium")
    
password_generat = string.ascii_letters + string.digits
punctuation = '!@#$%^&*'

password_length = int(input("Enter length of password : "))
password = PasswordGenrator(password_length)
CheckStrength(password)