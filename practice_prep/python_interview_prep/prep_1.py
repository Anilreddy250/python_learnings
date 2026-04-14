# try: pass
#     #part which might casue an error
# except TypeError:pass
#     #what happens when error occurs
# else: pass
# # what happens if there is no exception
# finally: pass
#     #executed after try and except always executed 
# def sun(a,b,c=10):
#     return a+b+c
# print(sun(10,12,c=12))

# from multiprocessing import process
# from turtle import pd
# import csv

# for chunk in pd.read_csv('data.csv', chunksize=1000):
#     process(chunk)
# pd.read_csv('data.csv', sep='\t', iterator=True, chunksize=1000)

# with open("log.txt") as infile:
#     for line in infile:
#         # do_something_with(line)
#         print(line)
#search  function as generator, effective for retuurning some set as result functionality lile "load 10 more items"
# def search_Result(keyword):
#     while keyword in dataset:
#         yield matched_data
# search_object = search_Result('keyword')
# search_object.__next__()
# mygenerator = (x*x for x in range(3, 6))
# while mygenerator ==36 :
#     print(mygenerator.__next__())
# print(mygenerator.__next__())
# try: 
#     pass
# except (TypeError,IndexError, RuntimeError) as error:
#     print(error)

# def enclosing_function(defined_value, some_operation=10):  
#     def nested_function():
#         some_operation = 10
#         return defined_value + some_operation
#     return nested_function
# closure_function = enclosing_function(50, 60)
# print(closure_function())
# # defined_value = 20
# # some_operation = 10

# def make_multipilier(n):
#     def multiplier(x):
#         return x*n
    
#     return multiplier
# times2 = make_multipilier(2)
# times3 = make_multipilier(3)
# print(times2(10))
# print(times3(10))

# def make_bold(fn ):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
# @make_bold
# @make_italic
# def index():
#     return "hello world"
# print(index())
example_list = [0,1,2,3,4,5,6,7,8,9]
# lsy = example_list[::3] # returns [0,3,6]
# print(lsy)

# print([x for x in example_list if example_list.index(x)%3 ==0])
# i = 0
# while i< len(example_list):
#     print(example_list[i])
#     i+=3

# class A:
#     def process(self):
#         print('A')
        
# class B(A):
#     pass
    
# class C(A):
#     def process(self):
#         print('C')

# class D(B,C):
#     pass
    
# obj = D()
# obj.process()
# D -> B -> C -> A -> object 
# note: a class can't  not e called before its superclass in resolving MRO. super Calss has to be called after derived calss.
# what is monkey patching? how to use it in python ?
# class OriginalClass:
#     def method(self):
#         return "original method"
# #monkey patching
# def new_method(self):
#     return "Pathched method"
# #patching the class methos
# OriginalClass.method = new_method
# #using the patching code
# obj = OriginalClass()
# print(obj.method())

# class Circle:
#     no_of_circles = 0
#     def __init__(self, radius):
#         self.radius = radius
#         print(Circle.no_of_circles)
#         Circle.no_of_circles +=1
#     @staticmethod
#     def square(num):
#         return print(num**2)
#     @classmethod
#     def getCircleCount(cls):
#         return print(cls.no_of_circles)
# c1 = Circle(5)
# c2 = Circle(10)
# Circle.getCircleCount()
# Circle.square(4)
# import sys

# # Demonstrating reference counting in Python
# a = "Geek"
# ref_count_a = sys.getrefcount(a)
# print(f"Reference count of 'a': {ref_count_a}")

# b = "Geek"
# ref_count_b = sys.getrefcount(b)
# print(f"Reference count of 'b': {ref_count_b}")

# # Both point to the same object due to string interning
# print(f"\na is b: {a is b}")
# print(f"id(a) == id(b): {id(a) == id(b)}")

# # Create another reference to demonstrate count increase
# c = a
# print(f"\nAfter c = a, reference count of 'a': {sys.getrefcount(a) - 1}")  # -1 to exclude the function call reference

# from collections import deque
# arr = [1,2,3,4,5,6,7]
# d =2
# # n = len(arr)
# # # reversed first d elements
# # arr[:d] = reversed(arr[:d])
# # print(arr[:d])
# # # reversed remaining elements
# # arr[d:] = reversed(arr[d:])
# # print(arr[d:])

# # arr.reverse()
# # print(arr)
# # res = deque(arr)
# # res.rotate(-d)
# # print(list(res))
# res = arr[d:] + arr[:d]
# print(res)

# a = 7
# b =13
# # print(max(a,b))
# # print(min(a,b))
# # print(list(map(lambda x, y: (x, y), [a], [b])))
# # print(a if a>b else b)
# num = [a,b]
# num.sort()
# print(num[-1])

# import math
# n =6
# print(math.factorial(n))


# import numpy as np 
# n =6
# if n>=0:
#     print(np.prod(range(1, n+1)))
# else:
#     print("factorial is not defined for negative numbers")
# n =6
# factorial =1
# # factorial_of_n = int()
# if n>=1:
#     for i in range(1, n+1):
#         factorial *=i
#         print(factorial)

# a = [1,2,3,4,5,6,7,8]
# n =3
# res = [a[i:i + n] for i in range(0,len(a),n)]
# print(res)
# import time
# COUNT = 50000000
# def countdown(n):
#     while n > 0:
#         n -=1
# start =time.time()
# countdown(COUNT)
# print('Time taken:', time.time() - start)

# arr = [6,5,4,3]
# n = len(arr)
# incr = all(arr[i]<=arr[i+1] for i in range(n-1))
# decr = all(arr[i]>=arr[i+1] for i in range(n-1))
# print(incr or decr)

# a = [8,2,3,4,5,6,7,1]
# res =1
# for i in a:
#     res +=i
# print(res)
# a[0],a[-1] = a[-1],a[0]
# print(a)
# res = min(a)
# a.sort()
# res = a[0]
# for val in a:
#     if val < res:
#         res = val

# print(res)

def function(i):
    # i = 5# Example value for i
    for i in range(i):

        if  i >= 0:
            print("one")
    # print("one
function(6)


