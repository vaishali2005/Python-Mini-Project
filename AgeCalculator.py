import datetime
print("Welcome To Age Calculator")
DOB = input("Enetr your date of birth (YYYY-MM-DD) : ")

#user define date to int 
# def DateConverter(d):
#     dob = d + '-'
#     date = ''
#     list_dob = []
#     for x in dob:
#         # print(x)
#         if x != '-':    
#             date += x
#         else: 
#             list_dob.append(int(date))
#             date = ''
#     print(list_dob)

#date to int converter by suing built in function
def DateInt(dob):
    return  map(int,dob.split("-"))

def YMD(dates):
    year, month, day = DateInt(dates)
    return datetime.date(year,month,day)
 
today = str(datetime.date.today())

bd1 = YMD(DOB)
bd2 = YMD(today)
age = (bd2 - bd1).days

y = age // 365
rd = age % 365
m = rd // 30
d = rd % 30

print(f"Your Age is {y}{"\n"}You live for {y} Years, {m} Months and {d} days")