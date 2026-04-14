#Lambda functions (anonymous functions) are favorite in interview because they test your ability ti write clean,
# "Pythonic" code. In automation you'll mostly use them with map(), filter(), and sort()
 #1 LIST TRANSFORMATION basics
# nums = [1,2,3,4,5]
# squared = list(map(lambda x: x**2, nums))
# print(squared)
# # the map() function is used to apply a specfic function to every item in  iterable (list, tuple etc) and return a map object (an iterator). The lambda function is used to define the function that will be applied to each item in the iterable. In this case, the lambda function takes an argument x and returns x**2, which is the square of x. The map() function applies this lambda function to each item in the nums list, resulting in a new list of squared values.
# #map (function, interable)
# # without map() you would need a for loop. with map(), it's one line

# numbers = [1,2,3,4,5]
# def square(x):
#     return x * x
# result = map(square, numbers)
# print(list(result))

# names = ["anil", "sunil", "manil"]
# upper_names = list(map(lambda name: name.upper(), names))
# print(upper_names)
# files = ["file1.txt", "file2.txt", "file3.txt"]
# python_files = list(filter(lambda f: f.endswith(".txt"), files))
# print(python_files)


tests = [
    {"name": "Login", "duration": 45},
    {"name": "Checkout", "duration": 120},
    {"name": "Search", "duration": 15}
]

tests.sort(key = lambda t: t["duration"])
print(tests)

#conditional logic in lambda advanced
#write a lambda function that takes a number and returns "High" if it is greater than 100, and "Low" otherwise
check_level = lambda x: "High" if x > 100 else "Low"
print(check_level(150))  # Output: "High"
print(check_level(50))   # Output: "Low"

#why use lambda at all ?
# in an interview if they ask "when shouls you not use a lambda ?" your answer should be:
#readability: it the logic is more than one line or very complex, use a regulat def function
#reusability : lambda are meant to be "throw-away" functions. if you nedd to call it from multiple places, a named function is better


#note: A lambda cannot contain statements like print(), pass, raise, or pass, inside  the expression. it must be a mathematical or logical expression that results in a vvalue.
