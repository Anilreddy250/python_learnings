# import re
# txt = "the rain in spain"
# # x =re.search("^the.*spain$", txt)
# x =re.search("the", txt)

# if x :
#  print ("yes, we have a match")
# else:
#  print ("not a match")

# data = [1,2,3,4,5,6,7,8]
# size =6
# chunks = [data[i:i + size] for i in range(0,len(data), size)]
# print(chunks)

# forbidden_words = {"spam", "ads", "virus"}

# def is_clean(sentence):
#     words = sentence.lower().split()
#     for word in words:
#         if word in forbidden_words:
#             return False
#         return True
# print(is_clean("This is a virus"))

# A = [[1,2],[3,4]]
# B = [[5,6],[7,8]]
# results = [[0,0],[0,0]]

# for i in range(len(A)): #rows of A
#     print(i)
#     for j in range(len(B[0])): #colums of b
#         print(j)
#         for k in range(len(B)): #rows of B / cols of A
#             print(k)
#             results[i][j] += A[i][k] *B[k][j]
# print(results)

#second largest numbet without sort():
# nums = [10,20,4,45,99,45]
# first = second = float('-inf')

# for n in nums:
#     if n> first:
#         second = first
#         first = n
#     elif n> second and n != first:
#         second = n
# print(f"second larget is:{second}")

#swap "Anil Reddy" to "Reddy ANil"

# name = "Anil Reddy"
# words = name.split() #['Anil', 'Reddy']
# reversed_name = words[1] + ' ' + words[0]
# print(reversed_name)

#orint even and odd numbers.

# numbers = range(1, 11)
# evens = [n for n in numbers if n %2 == 0]
# odds = [n for n in numbers if n%2 != 0]
# print(f"even number : {evens} and odds :{odds} ")

# 10/0 Error type
# diving zero raises a ZeroDivisionError
# print(10/0)

# Differense between is and ==
# a = [1,2]
# b = [1,2]
# print(a ==b)
# print( a is b)

# coding qns for oops ?
# class Employee:
#     def __init__(self, name, salary):
#         self.name =name
#         self.__salary = salary #encaplulation(Prive variable)
#     def work(self):
#         return f"{self.name} is working"
# class Developer(Employee):
#     def work(self):
#         return f"{self.name} is working" 
# dev = Developer("Anil", 50000)
# print(dev.work())

#what is anagram?
# def is_anagram(s1, s2) :
#     return sorted(s1.lower()) == sorted(s2.lower())
# print(is_anagram("listen", "silent"))

#read csv and print Specfic columns ?

# import csv

# with open("data.csv", mode= 'r') as file :
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], row['salary'])

# reverse content of a file??
# with open('test.txt', 'r') as f:
#     lines = f.readlines()
# with open('test.txt', 'w') as f:
#     for line in reversed(lines):
#         f.write(line)

# longest palindrome in a string ??

# class Solution:
#     def longestPalindrome(self, s ):
#         res = "" 
#         res_len = 0
#         for i in range(len(s)):
#             #check for odd length palindromes(e.g "aba")
#             l ,r = i, i
#             while l>=0 and r< len(s) and s[l] == s[r] :
#                 if (r-l +1) > res_len:
#                     res = s[l:r+1]
#                     res_len = r - l +i
#                 l -=1
#                 r +=1
#                 #check for even length palindrome(eg. "baab")
#             l ,r = i, i+1
#             while l>=0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > res_len:
#                     res = s[l:r+1]
#                     res_len = r-l+1
#                 l-=1
#                 r+=1
#         return res
# results = Solution()
# ans = results.longestPalindrome("babaab")
# print(ans)          

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >=len(s):
#             return s
#         #initialize a lit of strings for each row
#         rows = [""] * numRows
#         current_row = 0
#         going_down =False
#         for char in s :
#             rows[current_row] += char
#             #if we are at the top or bottom row, reverse direction
#             if current_row ==0 or current_row == numRows -1:
#                 going_down = not going_down
#             current_row +=1 if going_down else -1
#         return ''.join(rows)       
b = [1,2,3,4,5] *2
print(b)