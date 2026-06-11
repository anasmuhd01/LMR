# Reverse a string:
# string1 = 'hellow'
# print(string1[::-1])

# Check palindrome
print('enter string: ')
string1 = input()
pal = string1[::-1]
if string1 == pal:
    print("palindrome")
else:
    print('not palindrome')