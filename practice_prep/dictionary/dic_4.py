# dict1 = {"a":1, "b":2}
# dict2 = {"b":3, "c":4}
# # merged_dict = dict1 | dict2
# # merged_dict = {**dict1, **dict2}
# dict1.update(dict2)
# print(dict1)
# # print(merged_dict)


# joining multiple dictionaries
# list_of_dicts = [{"a":1},{"b":2},{"C":3}]
# combined = {}
# for d in list_of_dicts:
#     combined.update(d)
# print(combined)
# data = "apple banana apple cherry banana apple"
# # list = string.split()
# # print(list)
# # counts = {}
# # for word in list:
# #     # if word in counts:
# #         # counts[word] +=1

# #     counts[word] = counts.get(word, 0)+1
    
# # print(counts)
# from collections import Counter
# counts = Counter(data.split())
# print(counts)

# The Goal: You have a list of students and their grades. Create a dictionary where the keys are the grades and the values are lists of students who got that grade.
# students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'C')]
# from collections import defaultdict
# group_data = defaultdict(list)
# for name , grade in students:
#     group_data[grade].append(name)

# print(dict(group_data))

# students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'C')]
# group_data = {}
# for name , grade in students:
#     group_data.setdefault(grade, []).append(name)
# print(group_data)
#flattening the dictionary _________________________________________
# nested_list = {'user': {'name': 'John', 'address': {'city': 'NY', 'zip': 10001}}}
# def flatten_dict(nested_dict, parent_key='', sep='.'):
#     items = {}
#     for key, value in nested_dict.items():
#         new_key = f"{parent_key}{sep}{key}" if parent_key else key
#         if isinstance(value, dict):
#             #if the value is another dictionary recurse
#             items.update(flatten_dict(value, new_key, sep=sep))
#         else:
#             #if it's a base value, add it to our flat dictionary
#             items[new_key] = value
#     return items
# #tesing the function
# output = flatten_dict(nested_list)
# print(output)

#Dictionary_inversion_logic_______________________________________________
#swap the key and values of a dictinary?
# dict  = {'a': 1, 'b': 2, 'c': 3}
# dict = {'a': 1, 'b': 2, 'c': 1}
# # inverted_dict = {v:k for  k,v in dict.items()}
# # print(inverted_dict)
# inverted = {}
# for k , v in dict.items():
#     inverted.setdefault(v,[]).append(k)
# print(inverted)

# from collections import defaultdict
# data = {'a': 1, 'b': 2, 'c': 1}
# inverted = defaultdict(list)
# for k, v in data.items():
#     inverted[v].append(k)
# print(inverted)

#merging with math(practical)_____________________________________________________
# Dict_A= {'apples': 5, 'oranges': 3}
# Dict_B= {'apples': 2, 'bananas': 10}
# # combined = Dict_A.copy()
# # for item, quatity in Dict_B.items():
# #     combined[item] = combined.get(item,0) + quatity
# # print(combined)


# from collections import Counter
# print(Counter(Dict_A))
# result = Counter(Dict_A) + Counter(Dict_B)

# print(dict(result))

# def print_data(item):
#     if isinstance(item, dict):
#         # We know it's a dict, so we can safely use dict methods
#         for key, value in item.items():
#             print(f"{key}: {value}")
#     else:
#         # If it's just a string or list, do something else
#         print(f"This is not a dictionary, it's a {type(item)}")

# data_1 = {"name": "Gemini", "age": 1}
# data_2 = ["Apple", "Banana"]

# print_data(data_1) # Runs the dict logic
# print_data(data_2) # Runs the 'else' logic

# fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     print(fruit)
#     #enumerate()
# # for index, fruit in enumerate(fruits, start=1):
# #     print(f"position {index}: {fruit}")
# print(list(enumerate(fruits)))

# print(list(map(str.upper, ["a","b"])))
# numbers = range(40)
# # print(list(filter(lambda x : x >10)))
# squared_evens = [x**2 for x in numbers if x % 2 == 0]
# print(squared_evens)

