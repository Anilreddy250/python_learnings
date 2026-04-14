# class Robot:
#     def __init__(self,name):
#         self.name = name
#         print(f"Robot {self.name} is online")
#     def __del__(self):
#         print(f"Robot {self.name} is shutting down")
# bot = Robot("R2d2")
# del both

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def __str__(self):
#         return f"{self.title} by {self.author}"
# my_book = Book("1984", "Grorge Orwell")
# print(my_book)

# class Wallet:
#     def __init__(self,balance):
#         self.balance = balance
#     def __add__(self, other):
#         return Wallet(self.balance + other.balance)
# W1 = Wallet(50)
# W2 = Wallet(30)
# W3 = W1 + W2
# print(W3.balance)

class Team:
    def __init__(self, members):
        self.members = members
    def __len__(self):
        return len(self.members)
    def __getitem__(self, index):
        return self.members[index]
avegers = Team(["Iron man","Thor", "Hulk"])
print(len(avegers))
print(avegers[0])
    