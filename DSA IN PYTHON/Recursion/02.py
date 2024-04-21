# Calculate sum of frist N natural numbers..-------------------**
# def sumN(n):
#     if n==1:
#         return 1
#     s = sumN(n-1) + n
#     return s
# print(sumN(10))

# Calculate N odd natural numbers----------------------------**

# def sumOd(n):
#     if n == 1:
#         return 1
#     return sumOd(n-1) + 2*n-1
# print(sumOd(5))

## Calculate N Even natural numbers----------------------------**

# def evenN(n):
#     if n == 1:
#         return 2
#     return 2*n + evenN(n-1)
# print(evenN(10))

# Calculate fact-----------------------------------------------**
# def suM(n):
#     if n == 0:
#         return 1
#     return n * suM(n-1)
# print(suM(9))

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# print(fact(9))

# calculate square n numbers----------------------------***

# def squar(n):
#     if n == 1:
#         return 1
#     return n*n + squar(n-1)
# print(squar(5))


# def printN(n):
#     if n == 1:
#         return 1
#     return n*n + printN(n-1)
# print(printN(5))