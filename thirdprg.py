# num=1
# while num<=10:
#     print(num)
#     num=num+1
# print("Loop Ends")

# a=1
# while a<=5:
#     print("hello")
#     a+=1

# a=2
# while a<=10:
#     print(a)
#     a+=2

# num =1
# while num <= 10:
#     if num % 2 == 0:
#         print(num)
#     num = num+1
#----------------------------


# a=1
# total=0
# while a<=100:
#     total+=a
#     a+=1
# print(total)

#------------------------

# inp_val=int(input("enter a number: "))
# total= 1
# while inp_val>=1:

#     total*=inp_val
#     inp_val-=1

# print(total)
#------------------------------
# num=10
# while num>=1:
#     print(num)
#     num-=1
# print("Loop Ends") 

#---------------
# for i in range(1,11,1):
#     print(i)

# for i in range(1,6):
#     print("hello")

# for i in range(5):
#     print("hello")

# for i in range(0,11,2):
#     print(i)

# for i in range(11):
#     if i % 2 == 0:
#         print(i)

# total =0
# for i in range(101):
#     total = total +i
# print(total)

# user_value1= int(input("enter number :"))
# total =1
# for i in range(user_value1,1,-1):
#     total*=i
# print(total)

# total=1
# user_value2= int(input("enter number :"))
# for i in range(1,user_value2+1):
#     total*=i
# print(total)

# for i in range(10,0,-1):
#     print(i)

# user_input=int(input("enter your number: "))
# for i in range(1,11):
#     for j in range(1,11):
#         val=i*user_input

#     print(i,"*",user_input,"=",val)

# user_input=int(input("enter your number: "))
# for i in range(1,11):
#     print(i," * ",user_input,"=",i*user_input)
#-----------------------------------------------------------


# num =12
# rev =0
# while num>0:
#     modv=num % 10 
#     rev = rev * 10 + modv
#     num =num//10
# print(rev,sum)

# ----------> end="" <---------------------#

# n=123
# rev=''
# for i in str(n):
#     rev = i + rev
# print(int(rev))

# def sum_digit(num):
#     total_sum=0
#     while num>0:
#         mod=num%10
#         total_sum+=mod
#         num//=10
#     return total_sum

# n=int(input("enter a number : "))
# print(sum_digit(n))
 

# weight=float(input("enter your weight: "))
# height=float(input("enter your height: "))

# height=height/100
# bmi= weight/(height*height)
# print(bmi)


# if bmi<18.5:
#     print("underweight :")
# elif bmi>18.5 or bmi<24.9:
#     print("normal")
# elif bmi>25 or bmi<29.9:
#     print("over weight")
# elif bmi>30:
#     print("very overweight")
# else:
#     print("wrong data")



# def armstron_number(num):
#     arm_cal =0
#     total_len=len(str(num))
#     while num > 0:
#         mod = num % 10
#         arm_cal = (mod ** total_len) + arm_cal
#         num//=10
#     return arm_cal

# user_input = int(input("enter a number to check: "))
# ret_val = armstron_number(user_input)

# if ret_val == user_input:
#     print("armstrong number:")
# else:
#     print("not armstrong ")


# user_input1=int(input("enter a number "))
# temp=user_input1
# temp1=user_input1
# count = 0
# while temp>0:
#     temp % 10
#     temp =temp // 10
#     count+=1


# sum_of_digits =0
# while temp1 > 0:
#     mod =temp1 % 10
#     sum_of_digits += (mod**count)
#     temp1//=10

# if sum_of_digits == user_input1:
#     print("ARMSTRONG NUMBER ")
# else:
#     print("NOT ARMSTRONG ")


#----------------PRIME NUMBER--------------------------
# user_input = int(input("enter number :"))
# flag=0
# for i in range(2,user_input):
#     if user_input % i == 0:
#         flag =1
#         break
        
# if flag == 0:
#     print("PRIME")
# else:
#     print("NOT PRIME")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# for i in range(10):
#     if i == 4:
#         break
#     print(i)
# else:
#     print("LOOP ENDED ")
#     
     
# for i in range(10):
#     if i == 4:
#         continue
#     print(i)
# else:
#     print("LOOP ENDED ")

# user_input=int(input("enter limit of fibonacci series"))


# n0=0
# n1=1
# for i in range(0,11):
#     n2=n1+n0
#     n1=n0
#     n0=n2
#     print(n2)

# user_input =int(input("enter limit"))
# n0=0
# n1=1

# while  n1+n0 <= user_input:
    
#     n2=n1+n0
#     # if n2>user_input:
#     #     break
#     print(n2)
#     n1=n0
#     n0=n2
    


# user_input =int(input("enter limit: "))
# n0=0
# n1=1

# while n0 <= user_input:
#     print(n0)
#     n0, n1 = n1,n0+n1

# user_input=int(input("enter limit :"))
# n1=0
# n2=1
# while n1 <= user_input:
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3

#^^^^^FIBONACCI^^^^^^^^^^^^^^^^^^^^^^^^

# user_input = int(input("enter limit: "))
# n1=0
# n2=1
# for i in range(user_input):
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3
#-----------------------------------------


