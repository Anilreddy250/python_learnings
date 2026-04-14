def changescase(func):
    def myinner():
        return func().upper()
    return myinner
@changescase
def myfunction():
    return "Helloe_eorld"
print(myfunction())

# def countdown(n):
#     if n<=0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)

# class Outer:
#   def __init__(self):
#     self.name = "Outer"

#   class Inner:
#     def __init__(self):
#       self.name = "Inner"

#     def display(self):
#       print("Hello from inner class")

# outer = Outer()
# inner = outer.Inner()
# inner.display()
