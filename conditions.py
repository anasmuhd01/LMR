a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
# if a>b and a>c:
#     print(a,"is big")
# elif b>c:
#     print(b,"is big")
# else:
#     print(c,"is big")

if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
elif b>c:
    print("b is greater")
else:
    print("c is greater")