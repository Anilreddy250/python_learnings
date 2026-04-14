#python program for compound interest
# A = P(1+R/100)**T
# P = 1200
# R = 5.4
# T = 2
# A = P*(1+R/100)**T

# CI = A- P
# print("Compound Interest is", CI)

# from numpy import power

# import math
# num = int(input("Enter a number:"))
# n = num
# p = len(str(num))
# total = 0
# while n > 0:
#     digit  = n%10
#     total += digit ** p
#     n //= 10
# if total == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# area of circle = pi*r^2
# pi = 3.14
# r = 4
# area = pi*r**2
# print("area of the circle is :", area)

# import math
# r =5 
# area = math.pi *math.pow(r,2)
# print("area of the circle is :", area)

# import numpy as np
# r = 5
# area = np.pi *(r**2)
# print(area)

# x , y =2, 7
# primes = [True] *(y+1)
# #o and 1 are not prime
# primes[0] , primes[1] = False, False
# for i in range(2, int(y**0.5)+1):
#     if primes[i]:
#         for j in range(i*i, y +1, i ):
#             primes[j] = False
# res = [i for i in range (x, y+1)if primes[i]]
# print(res if res else "No")

# x,y =2, 7
# res =[]
# for i in range(x, y+1):
#     if i<=1:
#         continue
#     for j in range(2, i//2+1):
#         if i%j==0:
#             break
#     else:
#         res.append(i)
# print(res if res else "No")

# n = int(input("enter a number :"))  
# if n<=1:
#     print("Not prime")
# else:
#     is_prime = True #Flag variable
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             is_prime = False
#             break
#     print(is_prime)

# from sympy import *

# g1 = isprime(13)
# print(g1)

# def fibonacci_iterative(n):
#     if n<=0:
#         return 0
#     elif n ==1:
#         return 1
#     a, b = 0,1
#     for i in range(2, n+1):
#         a, b =b ,a+b
#     return b
# print(fibonacci_iterative(10))

# def fibnocci_recursive(n):
#     if n<=0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fibnocci_recursive(n-1) + fibnocci_recursive(n-2)
# print(fibnocci_recursive(100))

# n, m = 4,3
# a, b , count = 0, 1, 0
# while True:
#     a, b = b ,a+b
#     if b % m == 0:
#         count +=1
#         if count ==n:
#             print(b)
#             break

# def fun(n,m):
#     fib = [0,1]
#     count = 0
#     while True:
#         fib.append(fib[-1] + fib[-2])
#         if fib[-1] % m ==0:
#             count += 1
#             if count == n :
#                 return fib[-1]
# n , m  = 4, 3
# print(fun(n , m))

# n = 5
# res = int()
# for i in range(1, n+1):
#     # print("*" * i)
#     res += int(i**3)
# print(res)
# from funtoo
# arr = [12,3,4,15]
# # ans = sum(arr)
# # print("sum", ans)
# # t = 0
# # for i in arr:
# #     t +=i
# # print("sum", t)

# t =0 
# for i , val in enumerate(arr):
#     t +=val
# print(t)


# arr = [10, 324, 45, 90, 9800]
# res = max(arr)
# print(res)
# res = arr[0]
# for i in range(1, len(arr)):
#     if arr[i]> res:
#         res = arr[i]
# print(res)

# arr.sort()
# res = arr[-1]
# print(res)
arr = [1,2,3,4,5,6]
d = 2
arr[:] = arr[d:] + arr[:d]
print(arr)