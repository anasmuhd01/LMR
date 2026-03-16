# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
    
# res=factorial(5)
# print(res)
# print("--------------")
# print(factorial(7))

#----POSITIONAL ARGS-----
# def positional_args(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)

# positional_args(10,20,30)

#----KEYWORD ARGS---------
# def keyword_args(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)

# keyword_args(c=10,a=20,b=30)

#-----ARBITRARY ARGUMENTS--------------------------------------
#----- " * " is given to the parameter inside the function ----
#----- value will store in a tuple-----------------------------


# def arb_args(*a):
#     print("a=",a)

# arb_args(10,20,30)


# def arb_args(*a,b):
#     print("a=",a)
#     print("b=",b)

# arb_args(10,20,30,b=435)

# def arb_args(a,*b):
#     print("a=",a)
#     print("b=",b)

# arb_args(10,20,30,435)

#---- ARBITRARY KEYWORD ARGUMENT---------
#---- " ** " WILL BE USED AND STORED INSIDE A DICTIONARY---

# def arb_key_args(a,**b):
#     print("a=",a)
#     print("b=",b)

# arb_key_args(a=10,b=20,c=30)

#------------------------------------------------------------

# def both_args(*arg,**kwargs):
#     print("args=",arg)
#     print("kwargs=",kwargs)

# both_args(10,20,30,a=10,b=20,c=30)

#-----DEFAULT ARGUMENTS-------------------------------------
# def default_args(a,b=0):
#     print("A=",a)
#     print("B=",b)

# default_args(10,20)
# print("--------------------")
# default_args(10)


def rec_function(count):
    if count!=0:
        print("Recursive Function")
        rec_function(count-1)

rec_function(5)

# def factorial(n):
#     if n ==1:
#         return 1
#     else:
#         return n* factorial(n-1)
    

# print(factorial(5))


# var1 = lambda a,b:a+b
# print(var1(10,20))

# fact = lambda n:1 if n==1 else n*fact(n-1)
# print(fact(5))


#! pass by value and pass by reference note

