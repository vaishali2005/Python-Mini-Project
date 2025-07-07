# from math import sqrt
class Calculator:
    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
    def __add__(self):
        add = self.x + self.y
        return add
    def __sub__(self):
        sub = self.x = self.y
        return sub
    def __mul__(self):
        mul = self.x = self.y
        return mul
    def __truediv__(self):
        div = self.x = self.y
        return div
    def __pow__(self):
        pow = self.x ** self.y
        return pow        
print("Enter your calculation")
exp1 = float(input())
operator = input()
exp2 = float(input())
cal = Calculator()
match operator:
    case '+':
        print(exp1 + exp2)
    case '-':
        print(exp1 - exp2)
    case '*':
        print(exp1 * exp2)
    case '/':
        print(exp1 / exp2)
    case '**':
        print(exp1 ** exp2)