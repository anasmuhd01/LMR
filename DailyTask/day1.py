# Reverse a string:
# string1 = 'hellow'
# print(string1[::-1])

# Check palindrome
# print('enter string: ')
# string1 = input()
# pal = string1[::-1]
# if string1 == pal:
#     print("palindrome")
# else:
#     print('not palindrome')

#count vowels 
# vowel = input('enter vowel to check: ')

# if vowel in 'a e i o u AEIOUA':
#     print(f"{vowel} is a vowel ")
# else: 
#     print('not vowel')

# find the largest element
# a=[10,20,21,9]
# largest = a[0]

# for num in a:
#     # print(num)
#     if num > largest:
#         largest = num

# print(largest)

#find the second largest

arr = [10,21,11,35]

first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(first)
print(second)



