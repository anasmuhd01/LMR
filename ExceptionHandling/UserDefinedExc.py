'''
creating an exception for undefined cases or specific case
exception is created from 'Exception' class 
every exceptions are children of built-in class 'Exception'

'raise' keyword is used for raising exception
'''

class InsufficientBalanceError(Exception):
    pass

balance=8000
withdraw=int(input("Enter Amount: "))
if balance<withdraw:
    raise InsufficientBalanceError("withdraw amount greater than balance")

rem=balance-withdraw
print(rem)