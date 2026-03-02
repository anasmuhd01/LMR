'''
creating an exception for undefined cases or specific case
exception is created from 'Exception' class 
every exceptions are children of built-in class 'Exception'

'raise' keyword is used for raising exception
'''

# class InsufficientBalanceError(Exception):
#     pass

# balance=8000
# withdraw=int(input("Enter Amount: "))
# if balance<withdraw:
#     raise InsufficientBalanceError("withdraw amount greater than balance")

# rem=balance-withdraw
# print(rem)

class InsufficientBalanceError(Exception):
    def __init__(self, bal,withd):
        self.bal=bal
        self.withd=withd
        super().__init__(f"insufficient balance {self.bal} ")

try:
    balance=8000
    withdraw=int(input("Enter Amount: "))
    if balance<withdraw:
        raise InsufficientBalanceError(balance,withdraw)

    rem=balance-withdraw
    print(rem)
except Exception as e:
    print(e)
    print(e.bal) # exception values values can be accessed from the user defined class
