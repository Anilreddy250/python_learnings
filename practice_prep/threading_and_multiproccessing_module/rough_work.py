# import threading
# import time
# def task():
#     time.sleep(2)
#     print("Child thread finished!")
# # t =threading.Thread(target=task)
# # t.start()
# # print("Main program dinished")

# t= threading.Thread(target=task)
# t.start()
# t.join()
# print("Main Program Finished!")

# def binary


# data = [("Alice", 25), ("Bob", 30)]
# i = 0
# while i<=2:

#     for name, age in data:
#         i +=1
#         print(f"{name} is {age} years old count{i}")
# def add_item(item, box=[]):
#     box.append(item)
#     return print(box)

# print(add_item(1))
# print(add_item(2))
# from collections import Counter

# # results = string.count()
# # print(results)
# def first_unique_char(s):
#     counts = Counter(s) 
#     for char in s :
#         if counts[char]==1:
#             return f"{char}"
#     return None
# print(first_unique_char(s= "swiss"))
# print(char)
# def first_uniruw_char(s):c
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char, 0) +1
#     for char in s:
#         if counts[char] == 1:
            
#             return char
#             # print(char)
#     return None
# s = "swiss"
# print(first_uniruw_char(s))

# string = "swiss"
# counts = {}
# for char in string:
#     counts[char] = counts.get(char, 0) +1
# res = ""
# for char in string :
#     if counts[char] ==1:
#         # print(char)
#         res =char
#         # break
# print(res)
# print(counts)
# string = "Anil Reddy mokalla"
# counts = {}
# for char in string.lower():

#     counts[char] = counts.get(char,0)+1
#     # print(counts.get(char, 0))
# print(f"{counts[char]}:{counts.get(char,0)+1}")


# List = ["flower", "flow", "flight"]
# length = len(List)
# res = ''
# for i in range(length):
#     for char in List[i]:
#         if char in res==char:
#             res +=char
# print(res)
        

def longest_common_prefix(strs):
    prefix = "" 
    for chars in zip(*strs):
        if len(set(chars)) ==1:
            prefix +=chars[0]
        else:
            break
    return prefix
word = ["flower", "flow", "flight"]
print(longest_common_prefix(word))
