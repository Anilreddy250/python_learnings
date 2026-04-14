# Object-Oriented Programming (OOP) is a major focus in Python interviews, especially for roles involving automation and system design. Here are some of the most common and challenging OOP interview questions, categorized by their level of difficulty.

# ---

# ## 1. The "Basics" with a Twist
# These questions test if you understand the core mechanics of how Python handles classes.

# ### Q: What is the difference between Class Variables and Instance Variables?
# * **Answer:** * **Class Variables:** Defined inside the class but outside any methods. They are shared by all instances of the class. If you change a class variable, it changes for everyone.
#     * **Instance Variables:** Defined inside the `__init__` method using `self`. They are unique to each object.
# * **Problem:** If you have a class `Car` with a class variable `wheels = 4`, what happens if you run `my_car.wheels = 5`? Does it change the wheels for all cars?
#     * **Ans:** No. It creates a new **instance variable** for `my_car` that "shadows" the class variable. Other car objects will still have 4 wheels.

# ### Q: Why do we use `super().__init__()`?
# * **Answer:** It allows a subclass to call the constructor of its parent class. This ensures that the parent’s setup logic (like initializing certain attributes) is executed before the child adds its own logic.

# ---

# ## 2. Intermediate: Inheritance & Logic
# These questions focus on how classes interact and share code.

# ### Q: What is the "Diamond Problem" and how does Python solve it?
# * **Answer:** The Diamond Problem occurs in multiple inheritance when a class inherits from two classes that both inherit from the same "grandparent." 
# * **Solution:** Python uses **MRO (Method Resolution Order)** and the **C3 Linearization** algorithm. You can check the order by calling `ClassName.mro()`. It ensures that no class is visited twice and the most specific version of a method is called first.

# ### Q: Difference between Composition and Inheritance?
# * **Answer:**
#     * **Inheritance ("Is-a"):** A `Dog` *is an* `Animal`. You gain all features of the parent.
#     * **Composition ("Has-a"):** A `Car` *has an* `Engine`. You include an instance of another class as an attribute.
# * **Interview Tip:** Generally, "prefer composition over inheritance" because it makes code less rigid and easier to test.

# ---

# ## 3. Advanced: Pythonic OOP
# These questions separate beginners from experts by focusing on Python's unique "Magic Methods."

# ### Q: What is "Duck Typing"?
# * **Answer:** "If it walks like a duck and quacks like a duck, it's a duck." In Python, we don't check the type of an object; we check if it has the required method. 
# * **Example:** If two different classes both have a `.drive()` method, a function can call `.drive()` on either one without caring which class it belongs to.

# ### Q: What are `@classmethod` and `@staticmethod`?
# | Decorator | Receives | Use Case |
# | :--- | :--- | :--- |
# | **`@classmethod`** | `cls` (the class) | Factory methods (creating objects in a special way). |
# | **`@staticmethod`** | Nothing | Utility functions that relate to the class but don't need its data. |

# ---

# ## 4. Coding Problem: The "Bank Account"
# **Problem:** Create a `BankAccount` class that supports `deposit`, `withdraw`, and `get_balance`. Then, create a `SavingsAccount` that inherits from it but adds an `interest_rate` and a method to `apply_interest`.

# **Solution:**
# ```python
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance  # Protected attribute

#     def deposit(self, amount):
#         self._balance += amount
#         return self._balance

#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("Insufficient funds")
#         else:
#             self._balance -= amount
#         return self._balance

# class SavingsAccount(BankAccount):
#     def __init__(self, balance, interest_rate):
#         super().__init__(balance)
#         self.interest_rate = interest_rate

#     def apply_interest(self):
#         self._balance += self._balance * self.interest_rate
#         return self._balance

# # Interview Check:
# # - Did you use super()? 
# # - Did you handle the "insufficient funds" logic?
# ```

# ---

# ## 5. Coding Problem: Managing a Fleet (Real-world Scenario)
# **Problem:** Imagine you are automating mobile device testing (like your Appium work). Create a base class `Device` and two subclasses `AndroidDevice` and `IOSDevice`. Each should have a method `launch_app()`, but the implementation should be different for each.

# **Why they ask this:** This tests **Polymorphism**. You can have a list of different devices and call `.launch_app()` on all of them in a loop, and they will each behave correctly based on their specific class.

# ---

# ### Would you like me to dive deeper into "Magic Methods" (like `__str__` or `__call__`) which often come up in senior-level interviews?

# class BankAccount:
#     def __init__(self, balance = 0): #protected attribute
#         self._balance = balance 
#     def deposit(self, amount):
#         self._balance += amount
#         return self._balance
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("Insufficient funds")
#         else:
#             self._balance -= amount
#         return self._balance
# class SavingsAccount(BankAccount):
#     def __init__(self, balance, interest_rate):
#         super().__init__(balance)
#         self.interest_rate = interest_rate
#     def apply_interest(self):
#         self._balance +=self._balance * self.interest_rate
#         return self._balance
# savings = SavingsAccount(1000, 7)
# savingamount = savings.apply_interest()
# savingamount = savings.deposit(1000)
# savingamount = savings.withdraw(8000)
# print(savingamount)

