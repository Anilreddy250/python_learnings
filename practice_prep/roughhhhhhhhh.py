# # import array as arr
# # a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
# # print(a.pop())
# # print(a.pop(3))
# # a.remove(1.1)
# # print(a)


# # def simpleGeneratorFun():
# #     yield 1            
# #     yield 2            
# #     yield 3            
# # # Driver code to check above generator function
# # for value in simpleGeneratorFun(): 
# #     print(value)

# # def fib(limit):
# #     # Initialize first two Fibonacci Numbers 
# #     a, b = 0, 1
# #     # One by one yield next Fibonacci Number
# #     while a < limit:
# #         yield a
# #         a,b =b, a+b
# # # Create a generator object
# # x = fib(5)

# # # Iterating over the generator object using next
# # print(next(x))  # In Python 3, use next() instead of .next()
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))

# # # Iterating over the generator object using for
# # # in loop.
# # print("\nUsing for in loop")
# # for i in fib(5):
# #     print(i)

# # class Employee:
# #     def __init__(self, name):
# #         self.name = name
# # E1=Employee("abc")

# # # print(E1.name)
# # print(E1.name)

# # class Employee:
# #     def sudha(self, name, age,salary):
# #         self.name = name
# #         self.age = age
# #         self.salary = salary
# #         print(name,age, salary)
# # e1 = Employee()
# # e1.sudha("XYZ", 23, 20000)
# # E1 is the instance of class Employee.
# # __init__ allocates memory for E1.
# # print(e1.name)
# # print(e1.age)
# # print(e1.salary)
# # print(results)/

# # class Car:
# #     def __init__(self):
# #         self.__updateSoftware()
# #     def drive(self):
# #         print('driving')
# #     def __updateSoftware(self):
# #         print('updating software')
# # redcar = Car()
# # redcar.drive()

# # class Employee:
# #     def __init__(self, name, salary):
# #         self.name = name            # Public
# #         self._department = "HR"     # Protected (by convention)
# #         self.__salary = salary      # Private (mangled)

# # emp = Employee("Alice", 50000)

# # print(emp.name)           # Works: "Alice"
# # print(emp._department)    # Works: "HR" (but IDEs might warn you)
# # # print(emp.__salary)     # Raises AttributeError
# # print(emp._Employee__salary) # Works: 50000 (The "consenting adult" bypass)



# # def hello_decorator(func):
# #     # inner1 is a Wrapper function in 
# #     # which the argument is called
# #     # inner function can access the outer local
# #     # functions like in this case "func"
# #     def inner1():
# #         print("Hello, this is before function execution")
# #         # calling the actual function now
# #         # inside the wrapper function.
# #         func()
# #         print("This is after function execution")
# #     return inner1
# # # defining a function, to be called inside wrapper
# # def function_to_be_used():
# #     print("This is inside the function !!")
# # # passing 'function_to_be_used' inside the
# # # decorator to control its behavior
# # function_to_be_used = hello_decorator(function_to_be_used)
# # # calling the function
# # function_to_be_used()


# # def decorator(**kwargs):
# #     def outer(func):
# #         def inner(*args, **kw):
# #             print("Inside decorator")
# #             print("I like", kwargs["like"])
# #             return func(*args, **kw)
# #         return inner
# #     return outer

# # @decorator(like="python")
# # def func():
# #     print("inside actual function")

# # # Call the function
# # func()

# class my_decorator(object):
#     def __init__(self, f):
#         print("inside my_decorator.__init__()")
#         f() # Prove that function definition has completed
#     def __call__(self):
#         print("inside my_decorator.__call__()")
# @my_decorator
# def aFunction():
#     print("inside aFunction()")
# print("Finished decorating aFunction()")
# aFunction()


# data = (10,20,30,40,50)
# start,*middle, end = data
# print(start)
# print(middle)
# print(end)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
# res = list(set(sum(d.values(), [])))
# print(res)

# Umesh@asteralabs.com