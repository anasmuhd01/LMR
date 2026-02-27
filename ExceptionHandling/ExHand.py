'''
an event that occurs during the execution of a program to disrupt its normal flow

try:
    block
except:
    block
finally:
    block

''' 

try:
    val1=int(input("Enter num1: "))
    val2=int(input("Enter num2: "))
    div=val1/val2
    print(div)
except:
    print("Error Occured !")
finally:
    print("Welcome to Luminar12")