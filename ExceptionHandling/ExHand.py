'''
an event that occurs during the execution of a program to disrupt its normal flow

try:
    block
except:
    block
finally:
    block

''' 

# try:
#     val1=int(input("Enter num1: "))
#     val2=int(input("Enter num2: "))
#     div=val1/val2
#     print(div)
# except:
#     print("Error Occured !")
# finally:
#     print("Welcome to Luminar12")

# try:
#     val1=int(input("Enter num1: "))
#     val2=int(input("Enter num2: "))
#     div=val1/val2
#     print(div)
# except Exception as e:
#     print("Error Occured !")
#     print(e)
# finally:
#     print("Welcome to Luminar12")

# try:
#     val1=int(input("Enter num1: "))
#     val2=int(input("Enter num2: "))
#     div=val1/val2
#     print(div)
# except ZeroDivisionError:
#     print("division by zero not possible !")
# except ValueError:
#     print("enter valid input")
# except Exception as e:
#     print(e)
# finally:
#     print("Welcome to Luminar12")

try:
    val1=int(input("Enter num1: "))
    val2=int(input("Enter num2: "))
    div=val1/val2
    print(div)
except:
    print("Error Occured !")
else:
    print("No error occured: ") # else blcok work if no error occured if error !work
finally:
    print("Welcome to Luminar12")