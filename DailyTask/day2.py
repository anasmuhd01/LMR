# li = [10,21,21,14,10,3]
# print(li)
# print(list(set(li)))

# def odd(n):
#     if (n & 1) == 0:
#         return  f"even number"
#     else:
#         return f"odd number "

# print(odd(15))


# n = 3
# sum =0
# while n!=0:
#     sum += n
#     n=n-1

# print(sum)

def sumn(n):
    if n == 1:
        return 1
    return n + sumn(n-1)

print(sumn(3))