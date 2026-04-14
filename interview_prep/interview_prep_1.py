# #write a program to swap to numbers .
# a , b = 10 ,20
# b , a = a , b
# print(a , b)
# #write a program  to reverse a number
# num =1234
# rev = 0
# while num > 0 :
#     rem = num %10 # 4,3,2,1
#     rev = rev *10 + rem # 4, 43, 432, 4321
#     num = num //10 ## 123
# print(rev) 
# #write a program to revese a string
# s  ="ABCD"
# rese_Str = s[::-1]
# print(rese_Str)
#write a program for fibonacci series
# n = #
# write a program to fine a string is a palindrome or not ?
# s = "madam"
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
#write a program to find the numbers in given range ?
# input = 
# num = int(input("enter a number range:"))
# primes = []
# for i in range(2, num+1):
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         primes.append(i)
# print(primes)

#write a program to find weather the given number is prime NUmber or not?
# num = int(input("enter a number:"))
# if num > 1:

#     for i in range(2 ,int(num**0.5)+1):
#         if num % i ==0:
#             print(num , "is not a prime number")
#             break
#     else:  
#         print(num , "is a prime number")
# # """The Optimized Loopfor i in range(2, int(num**0.5) + 1):This is the "smart" part of the code. Instead of checking every number from 2 all the way up to num, it only checks up to the square root of the number.Why the square root? > If a number $n$ has a factor larger than its square root, it must also have a corresponding factor smaller than the square root. For example, if $n = 36$, its square root is 6. Factors are $(2 \times 18)$, $(3 \times 12)$, $(4 \times 9)$, and $(6 \times 6)$. Notice that once you pass 6, you are just repeating factors you already found."""
# # write a program to find the factorial of a number?
# num = int(input("enter a number:"))
# factorial = 1
# for i in range(1 , num+1):
#     factorial *= i
# print(factorial)

# write a program to check number is armstrong number ?
# num = int(input("enter a number:"))
# target = len(str(num))
# results = 0
# temp = num
# while temp > 0:
#     rem  = temp %10
#     results +=rem ** target
#     temp //=10
# if results == num:

#     print("num is an armstrong numer")
# else:
#     print("not an armstrog number")

#write a program to count number of digits in a number ?
# num = 1234
# count = len(str(num))
# print(count)
#write a program to find the number of even or odd?
# num = int(input("enter a number :"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")
#write a program to find the largest number 
# a = 10
# b = 20
# c = 30
# list = [a, b, c]
# print(max(list))
#write a program to generate random number and string?
# import random
# import string
# number = random.randint(1,100)
# letters = string.ascii_letters
# random_string = ''.join(random.choice(letters) for i in range(8))
# print(number, random_string)
#write a program to find the sum of elements in array?
# a = [1,2,3,4]
# print(sum(a))
# write a program to pint even and odd number in array?
# import array as arr
# arr = [1,2,3,4,5,6]
# for i in arr:
#     if i%2 == 0:
#         print(i,"EVEN number")
#     else:
#         print(i,"odd numbers")
# write a program to check 2 arrays are equal or not ?
# import array as arr
# arr1 = [1,2,3,4]
# arr2 = [1,2,3,4]
# if arr1 == arr2:
#     print("The arrays are identical")
# else:
#     print("The arrays are different")    
#write a program to find the max an min element in array?
# arr = [3,4,5,6]
# print(max(arr))
# print(min(arr))
# print()
#write a program to find the Duplicate number in array?
# arr = [3,4,5,6,6]
# n = len(arr)
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             print(arr[i],"is duplicate")
        # else: 
        #     print("no duplicate")
#write a program to find the second largest number in an array?
# arr = [6,6,6,6,6,6]
# unique_list = sorted(list(set(arr)))
# if len(unique_list) >=2:
#     print("second largest element is" ,unique_list[-2])
# else:
#     print("Array doesn't have a seconf largest element")
#write a program to remove all the white spcae in a string?
# string = "Follow Code yatra"
# results = string.replace(" ","")
# print(results)
# results = ''
# for char in string :
#     if char != " ":
#         results += char
# print(results)
# write a program to count words in a string?
# string = "Follow Code yatra"
# list = string.split()
# # count_of_word = len(list)

# # print(count_of_word)
# list_1 = list[::-1]
# print(list_1)
# # results.replace(",", "")

# results = " ".join(list_1)
# results.replace(",", "")
# print(results)

#write a program to remove junk or special charactor in a string?
# string = "!@$5Follow Code Yatra"
# junk = "!@$5"
# clean_String = ""
# for char in string:
#     if char not in junk:
#         clean_String +=char
# print(clean_String)

# write a program to search an element in Array(Linear search)?
# arr = [1,2,3,4,5,6,7,8,9]
# if 4 in arr:
#     print("element is exist")
# target = 4
# found =False
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(f"element {target} funt at index{i}")
#         found = True
#         break
# if not found :
#     print("element does not exist")
#Write a Program to Search an Element in Array (Binary Search).
# n = len(arr)
# left = 0
# right = n - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         print(f"Element {target} found at index {mid}")
#         found = True
#         break
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if not found:
#     print("Element not found")
# Write a Program to Search an Element in Array (Binary Search)
# arr = [1,2,3,4,5,6,7,8,9]
# target = 6
# def binary_search(arr, target):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid-1
#     return -1
# result = binary_search(arr, target)
# if result != -1:
#     print(f"element {target} found at index {result}")
# else:
#     print("element does not exist")

# write a program to srt elements in array (buHow do you handle a missing key in a dictionary?bble sort (imp))selection sort, insertion sort, merge sort, quick sort, heap sort.

#get() methods
# user = {"name":"Alice"}
# age = user.get("age")
# # print(age)
# age = user.get("age", 25)
# print(age)
# print(user)
# inventory = {"apples": 10, "banana":5}
# inventory["oranges"] = 20
# if "oranges" in inventory:
#     print(inventory["oranges"])
# else :
#     print("out of stock")
#dict.setdefault():
# setdefault() when you want to retrive a value, but if it doesn't exist, you want to insert it into the dictionary right then and there.
# counts = {"apples": 1}
# orange_count = counts.setdefault("banana",0)
# print(counts)
#collections.defaultdict: automated handling:
# if you are building a dictionary (like a counter or a list grouper)and expect missing keys frequently, defaultdict isthe cleanest choice. you define a " default factory" (like int, list, or str) at the start
# from collections import defaultdict
# #every missing key will  automatically start as empty list[]
# groups =defaultdict(list)
# groups["admins"].append("alice")
# print(groups)

# numbers= [1,2,2,4,4,4,5,6,7,8,9,9]
# # new_list = list(set(numbers))
# new_list = list(dict.fromkeys(numbers))
# # for i in list:
# #     if i not in new_list:
# #         new_list.append(i)
# print(new_list)
