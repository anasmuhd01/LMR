from functools import reduce
# a=[12,4,15,67,82,93,109,234]


# em=[]
# for i in a:
#     cube=i**3
#     em.append(cube)

# # print(em)

# def cube(a):
#     return a**3

# a=[12,4,15,67,82,93,109,234]

# res=map(cube,a)
# print(list(res))
# x=lambda a:a**3


# res = map(x,a)

# res = map(lambda a:a**3,a)
# print(list(res))

# res = filter(lambda a:a%2==0,a)

# print(list(res))

# a=["apple","banana","strawbery","kiwi","orange"]

# print(list(filter(lambda s:len(s)>=5,a)))

a=[1,56,71,24,39,103,245]

res= reduce(lambda sum,i: sum+i,a)
print(res)
