# def decorator(fn):
#     def inner(v1,v2):
#         if v1>v2:
#             return fn(v1,v2)
#         else:
#             return fn(v2,v2)
#     return inner



# @decorator
# def sum(a,b):
#     print(a-b)

# sum(5,10)


def validNum(fn):
    def inner(n):
        if n>0:
            return fn(n)
        else:
            print("Invalid Number")
    return inner

@validNum
def displayNum(n):
    for i in range(n):
        print(i)

displayNum(-1)