#----------PALINDROME-----------

inp=input("enter a string: ")

res=inp[::-1]
if res == inp:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
