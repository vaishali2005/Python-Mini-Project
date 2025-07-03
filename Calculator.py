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
    
def AddRemove(o1,o2,para):
    expression.remove(o2)
    expression.remove(o1)
    expression.remove(o)                
    for z in expression:
        if  z not in new_exp:
            new_exp.append(z)
    new_exp.append(para)       
operators = ['()', '**', '/', '*', '+', '-']
# expression = []
expression = [4.0, '*', 9.0, '+', 6.0, '/', 3.0]
operand, operator = 0,''

print(expression)
# print(expression[0],expression[6])
new_exp = []
for o in operators:
        if o in expression:
            match o:
                case '**':
                    o1 = expression[expression.index(o)-1]
                    o2 = expression[expression.index(o)+1]
                    para = o1  ** o2
                    AddRemove(o1,o2,para)
                    break
                case '/':
                    o1 = expression[expression.index(o)-1]
                    o2 = expression[expression.index(o)+1]
                    para = o1  / o2
                    AddRemove(o1,o2,para)
                    # break
                case '*': 
                    o1 = expression[expression.index(o)-1]
                    o2 = expression[expression.index(o)+1]
                    para = o1  * o2
                    AddRemove(o1,o2,para)
                    # break
                case '+':
                    o1 = expression[expression.index(o)-1]
                    o2 = expression[expression.index(o)+1]
                    para = o1  + o2
                    AddRemove(o1,o2,para)
                    break
                case '-':
                    o1 = expression[expression.index(o)-1]
                    o2 = expression[expression.index(o)+1]
                    para = o1  - o2
                    AddRemove(o1,o2,para)
                    break
print(new_exp)
# print(expression)
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
# print("Enter your calculation")
# exp1 = float(input())
# operator = input()
# exp2 = float(input())
# cal = Calculator()
# match operator:
#     case '+':
#         print(exp1 + exp2)
#     case '-':
#         print(exp1 - exp2)
#     case '*':
#         print(exp1 * exp2)
#     case '/':
#         print(exp1 / exp2)
#     case '**':
#         print(exp1 ** exp2)





# while True:
#     if operator == '=':
#         break
#     else:
#         operand = float(input())
#         expression.append(operand)
#         operator = input()
#         expression.append(operator)