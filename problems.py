from functools import reduce

#----------PALINDROME-----------

# inp=input("enter a string: ")

# res=inp[::-1]
# if res == inp:
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

# a=[1,2,3] #--> gloabl scope <--

# def fun():
#     global b #--> to make global scope of the local variable
#     print("from fun",a)
#     b=[1,2,3] #--> local scope <--
# fun()
# print(b)

# for i in a:
#     print(i)

# if True:
#     print(a)



# for i in range(5,0,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(1):
#         print("*",end=" ")
#     print()

# student=[
#     {"name":"Amal","age":20,"Score":180},
#     {"name":"Vimal","age":19,"Score":120},
#     {"name":"Anu","age":18,"Score":140},
#     {"name":"Anna","age":22,"Score":180},
# ]

# the below can be simplified using 
# lst=[]
# for i in student:
    # x=i["name"]
    # lst.append(x)
    # above or below same
    # lst.append(i["name"])

# print(lst)
    
# the above THIS
# res = map(lambda a:a["name"],student)
# print(list(res))



student=[
    {"name":"Amal","age":20,"Score":180,"course":"BSC CS"},
    {"name":"Vimal","age":19,"Score":120, "course":"BSC CS"},
    {"name":"Anu","age":18,"Score":140, "course":"BCA"},
    {"name":"Anna","age":22,"Score":180, "course":"MCA"},
]
# sum=0
# for i in student:
#     sum=sum+i["Score"]
# print(sum)


# sum=reduce(lambda a,b: a+b["Score"],student,0)
# print(sum)

#WAP to print names of student from BSC CS
# for i in student:
#     if i["course"]=="BSC CS":
#         print(i["name"])

# res=map( lambda a:a["course"]=="BSC CS",student )
# print(list(res))

#WAP to find avg age of students from BSC cs

# len_var=len(student)
# total=reduce(lambda a,b:a+b["age"],student,0)
# print(f"average age ={total/len_var}")

#WAP to find list of students whose age <20

res=filter(lambda a:a["age"]<20,student)
print(list(res))

#WAP to find find student with least score



# print(reduce(lambda a,b:a if a["Score"]<b["Score"] else b,student))


