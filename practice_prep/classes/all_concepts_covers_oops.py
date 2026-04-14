# from abc import ABC, abstractmethod

# # ── Abstraction ── define the contract
# class Staff(ABC):
#     @abstractmethod
#     def get_role(self): pass

#     @abstractmethod
#     def annual_bonus(self): pass

# # ── Inheritance + Encapsulation ──
# class Employee(Staff):
#     company = "Acme Corp"          # class variable (shared)
#     _headcount = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary     # private — encapsulated
#         Employee._headcount += 1

#     # ── @property — controlled access ──
#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, val):
#         if val < 0:
#             raise ValueError("Salary can't be negative")
#         self.__salary = val

#     # ── classmethod ──
#     @classmethod
#     def headcount(cls):
#         return cls._headcount

#     # ── Dunder methods ──
#     def __str__(self):
#         return f"{self.name} @ {self.company}"

#     def __repr__(self):
#         return f"Employee({self.name!r}, {self.__salary})"

#     def __eq__(self, other):
#         return self.name == other.name


# class Manager(Employee):          # Inheritance
#     def get_role(self): return "Manager"
#     def annual_bonus(self): return self.salary * 0.20

# class Developer(Employee):        # Inheritance
#     def get_role(self): return "Developer"
#     def annual_bonus(self): return self.salary * 0.15


# # ── Polymorphism ── same loop, different behaviour
# staff = [Manager("Alice", 120000), Developer("Bob", 95000)]

# for s in staff:
#     print(f"{s}  |  Role: {s.get_role()}  |  Bonus: ₹{s.annual_bonus():,.0f}")

# print(f"Total headcount: {Employee.headcount()}")
# # ```
# # ```
# # Alice @ Acme Corp  |  Role: Manager    |  Bonus: ₹24,000
# # Bob @ Acme Corp    |  Role: Developer  |  Bonus: ₹14,250
# # Total headcount: 2

# def my_function():
#     print("hello from the function")
# my_function()

# def  fahrenheit_to_celisius(fahrenheit):
#     return (fahrenheit - 33) *5/9
# print(fahrenheit_to_celisius(32))

# def get_greeting():
#     return "hello from a function"
# message = get_greeting()
# # print(get_greeting())

# def my_function(fname):
#     print(fname + "refsnes")
# my_function("email")

# def  my_function(*numbers):
#     total = 0
#     for num in numbers:
#         total +=num
#     return total
# print(my_function(1,2,3,4,5,6))

# def my_function(*numbers):
# #   if len(numbers) == 0:
# #     return None
#   max_num = numbers[0]
#   for num in numbers:
#     if num > max_num:
#       max_num = num
#   return max_num

# print(my_function(0))
