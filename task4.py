# 1
# num=int(input("Enter number: "))
# if num%2==0:
#     print(f"{num} is even number!")
# else:
#     print(f"{num} is odd")

# 2
# num=int(input("enter year: "))
# if num%400==0:
#     print("Leap Year")
# elif num%100==0:
#     print("Not leap year")
# elif num%4==0:
#     print("leap year:")
# else:
#     print("Not leap year")

#3
# a=[]
# for i in range(3):
#     value=int(input("enter number: "))
#     a.append(value)

# if a[0]>a[1] and a[0]>a[2]:
#     print(f"{a[0]} is greater")
# elif a[1]>a[2]:
#     print(f"{a[1]} is greater")
# else:
#     print(f"{a[2]} is greater")

#4
# age=int(input("Enter age: "))
# gender=input("Enter gender: (M|F: )")
# days=int(input("Enter working days: "))

# if age>=18 and age<30 and gender=='M':
#     print(f"Wage = {700*days}")
# elif age>=18 and age<30 and gender=='F':
#     print(f"Wage = {750*days}")
# elif age>=30 and age<=40 and gender=='M':
#     print(f"Wage= {800*days}")
# elif age>=30 and age<=40 and gender=='F':
#     print(f"Wage= {850*days}")
# else:print("invalid age: ")


#5
# price_unit=100
# qty=int(input("Enter quantity: "))
# if qty >= 1000:
#     total=price_unit*qty
#     per=total*0.1
#     final=total-per
#     print(f"after discount price : {final}")
# else:
#     print(f"total price: {qty*price_unit}")

#6
# side=[]
# for i in range(3):
#     sides=int(input(f"Enter side {i+1}: "))
#     side.append(sides)

# if side[0] == side[1] == side[2]:
#     print("EQUILATERAL TRIANGLE ")
# elif side[0]==side[1] or side[1]==side[2] or side[2]==side[0]:
#     print("ISOSCELES TRIANGLE ")
# else:
#     print("SCALENE TRIANGLE ")

#7
# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# oper=input("Enter Operation: \n + * / % - \n")

# def math_operations(num1,num2,oper):
#     if oper=="+":
#         return num1+num2
#     elif oper=="-":
#         return num1-num2
#     elif oper=='/':
#         return num1/num2
#     elif oper=='%':
#         return num1%num2
#     elif oper=='*':
#         return num1*num2
#     else:
#         return f"{oper} is not a valid operation:"

# res=math_operations(num1,num2,oper)
# print(res)

#8
# mark=int(input("enter mark: "))
# if mark >80:
#     print("A")
# elif mark >=60 and mark<80:
#     print("B")
# elif mark >=50 and mark<60:
#     print("C")
# elif mark >=45 and mark<50:
#     print("D")
# elif mark >=25 and mark<45:
#     print("E")
# else:
#     print("F")

#9

# city_moun={
#     "Delhi":"Red fort",
#     "Agra":"Taj mahal",
#     "Jaipur":"Jal mahal"
#            }
# city=input("Enter city: ")

# if city in city_moun:
#     print(city_moun[city])
# else:
#     print("Invalid city")

#10

length=int(input("Enter length:"))
bredth=int(input("Enter bredth:"))

if length == bredth:
    print("given values form a square:")
else:
    print("Rectangle: ")
    



