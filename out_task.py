# n = int(input())
# arr = map(int, input().split())
# # print(list(arr))

# y=list(arr)

a=[4,2,1,8,5,5]

# fi=a[0]

# for i in a:
#     if fi < i:
#         fi = i
    
# print(fi)
# a.remove(fi)
# fi=a[0]
# for i in a:
#     if fi < i:
#         fi= i
# print(fi)

# print(sorted(set(a))[-2])

pythonstudents = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# z=dict(pythonstudents)
# # print(z)
# x=[]
# for i in z:
#     x.append(z[i])

# print(x)

# min_score=min(x)

# # for name,score in z.items():
# #     if score== min_score:
# #         print(name)

# a={name:score for name,score in z.items() if score!= min_score }
# # print(a)
# y=[]
# for i in a:
#     y.append(a[i])

# low_mark_sorted =min(sorted((y)))
# # print(low_mark_sorted)
# ne=[]
# for i in a:
#     if low_mark_sorted == a[i]:
#         ne.append(i)

# final=sorted(ne)
# for i in final:
#     print(i)




students = [] 


scores = sorted(set(score for name, score in pythonstudents)) 
second_lowest = scores[1] # Step 2: print names alphabetically 
for name in sorted(name for name, score in pythonstudents if score == second_lowest): print(name)






    


    


    

